<h1 id="1-gmail">1. Gmail</h1>
<ul>
<li>gmail 회원가입 &gt; 로그인 &gt; 계정
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/fb7a68b9-fa81-4d10-bda6-8fa1c8c19466/image.png" /></li>
<li>Google 계정 검색 &gt; &quot;앱 비밀번호&quot; 검색
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/0d6049ab-5eb8-4072-9982-b0ce7c0c3ece/image.png" /></li>
<li>이름 설정 &gt; 만들기
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/159c2e56-de91-4b20-a55c-c9685b1a7bd0/image.png" /></li>
<li>16자리 알파벳 저장
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/ccf6fcba-59e1-4322-8bb8-5ebfe2bc8740/image.png" /></li>
</ul>
<h1 id="2-스프링-프로젝트에-설정-추가">2. 스프링 프로젝트에 설정 추가</h1>
<ul>
<li>build.gradle 파일에 추가<pre><code class="language-java">dependencies {
  implementation 'org.springframework.boot:spring-boot-starter-web'
  implementation 'org.springframework.boot:spring-boot-starter-mail'
}
</code></pre>
</li>
</ul>
<pre><code>- application.properties 파일에 추가
```java
spring.mail.host=smtp.gmail.com
spring.mail.port=587
spring.mail.username= gmail 입력
spring.mail.password= 발급받은 앱 비밀번호(16자리 알파벳) 입력
spring.mail.properties.mail.smtp.auth=true
spring.mail.properties.mail.smtp.starttls.enable=true
spring.mail.properties.mail.smtp.starttls.required=true
</code></pre><h1 id="3-dto-만들기">3. DTO 만들기</h1>
<ul>
<li>인증번호를 받고 싶은 email을 전송하기 위한 DTO<pre><code class="language-java">package com.ssafy.teongbin.mail.dto;
</code></pre>
</li>
</ul>
<p>import lombok.Data;</p>
<p>@Data
public class MailDto {
    private String email;
}</p>
<pre><code>- 인증번호를 받은 후 인증을 요청하기 위한 DTO
```java
package com.ssafy.teongbin.mail.dto;

import lombok.Data;

@Data
public class ApproveRequestDto {
    private String email;
    private String code;
}
</code></pre><h1 id="4-controller-구현">4. Controller 구현</h1>
<pre><code class="language-java">package com.ssafy.teongbin.mail.controller;

import com.ssafy.teongbin.mail.dto.ApproveRequestDto;
import com.ssafy.teongbin.mail.dto.MailDto;
import com.ssafy.teongbin.mail.service.MailService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
public class MailController {

    private final MailService mailService;

    @PostMapping(&quot;/api/v1/user/email&quot;)
    public void MailSend(@RequestBody MailDto mailDto) {
        mailService.sendMail(mailDto);
    }

    @PostMapping(&quot;api/v1/user/verify&quot;)
    public void verifyCode(@RequestBody ApproveRequestDto approveRequestDto) {
        mailService.verifyCode(approveRequestDto);
    }
}</code></pre>
<h1 id="5-service-구현">5. Service 구현</h1>
<ul>
<li>인증번호 mail을 전송하고 검증하기 위한 service<pre><code class="language-java">package com.ssafy.teongbin.mail.service;
</code></pre>
</li>
</ul>
<p>import com.ssafy.teongbin.common.exception.CustomException;
import com.ssafy.teongbin.common.exception.ErrorType;
import com.ssafy.teongbin.mail.dto.ApproveRequestDto;
import com.ssafy.teongbin.mail.dto.MailDto;
import jakarta.mail.MessagingException;
import jakarta.mail.internet.MimeMessage;
import lombok.RequiredArgsConstructor;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;</p>
<p>@Service
@RequiredArgsConstructor
public class MailService {</p>
<pre><code>// JavaMailSender: Spring의 이메일 발송을 위한 템플릿 클래스.
private final JavaMailSender javaMailSender;

private final RedisService redisService;

// 이메일 발신자의 주소를 저장
private static String senderEmail = &quot;발신자 이메일&quot;;
// 인증코드 저장할 정수형 필드
private static int number;

// 임의의 6자리 숫자를 생성하는 코드
public static void createNumber() {
    number = (int)(Math.random()*90000) + 100000;
}

public MimeMessage createMail(String mail) {
    // 인증 코드 생성
    createNumber();
    // MimeMessage 객체 생성
    MimeMessage message = javaMailSender.createMimeMessage();

    try {
        //  발신자 이메일 주소 설정
        message.setFrom(senderEmail);
        // 수신자 설정
        message.setRecipients(MimeMessage.RecipientType.TO, mail);
        // 발송할 이메일 형식 HTML로 작성
        message.setSubject(&quot;이메일 인증&quot;);
        String body = &quot;&quot;;
        body += &quot;&lt;h3&gt;&quot; + &quot;요청하신 인증 번호입니다.&quot; + &quot;&lt;/h3&gt;&quot;;
        body += &quot;&lt;h1&gt;&quot; + number + &quot;&lt;/h1&gt;&quot;;
        body += &quot;&lt;h3&gt;&quot; + &quot;감사합니다.&quot; + &quot;&lt;/h3&gt;&quot;;
        // 위 내용을 HTML 형식으로 설정
        message.setText(body,&quot;UTF-8&quot;, &quot;html&quot;);
    } catch (MessagingException e) {
        // MessagingException을 처리하여 이메일 생성 중 발생할 수 있는 예외 처리
        e.printStackTrace();
    }

    return message;
}

public int sendMail(MailDto mailDto) {
    // 수신자의 이메일 주소를 가져와서 공백 제거
    String mail = mailDto.getEmail().trim();
    // MimeMessage 객체 생성
    MimeMessage message = createMail(mail);
    // 이메일 전송
    javaMailSender.send(message);
    // 인증 코드를 레디스에 저장
    redisService.saveVerificationCode(mail, String.valueOf(number));
    // 생성된 인증 번호를 반환
    return number;
}

// 인증 코드 검증 메소드
public boolean verifyCode(ApproveRequestDto approveRequestDto) {
    // 입력된 이메일을 이용해 Redis에 저장된 코드 저장
    String storedCode = redisService.getVerificationCode(approveRequestDto.getEmail());
    // 입력된 인증코드와 Redis에 저장된 코드가 일치하는지 확인
    if (storedCode != null &amp;&amp; storedCode.equals(approveRequestDto.getCode())) {
        redisService.deleteVerificationCode(approveRequestDto.getEmail());
        return true;
    } else {
        throw new CustomException(ErrorType.FAILED_TO_EMAILVERIFY);
    }
}</code></pre><p>}</p>
<pre><code>- 생성한 인증번호를 Redis에 저장하고 조회하기 위한 service
```java
package com.ssafy.teongbin.mail.service;

import com.ssafy.teongbin.common.exception.CustomException;
import com.ssafy.teongbin.common.exception.ErrorType;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.concurrent.TimeUnit;

@Service
@RequiredArgsConstructor
public class RedisService {

    // Redis와 상호작용하는 Spring의 클래스입니다. 제네릭 타입은 키가 String이고 값이 Object라는 것을 의미
    private final RedisTemplate&lt;String, Object&gt; redisTemplate;

    // 인증 번호 Redis에 저장하는 코드(5는 유효시간(분))
    // email을 키로 해서 code 값을 저장
    public void saveVerificationCode(String email, String code) {
        redisTemplate.opsForValue().set(email, code, 5, TimeUnit.MINUTES);
    }

    // Redis에서 인증 코드를 조회하는 코드
    public String getVerificationCode(String email) {
        Object result = redisTemplate.opsForValue().get(email);
        // email에 해당하는 code가 저장되어있지 않을 경우 에러 발생
        if (result == null) {
            throw new CustomException(ErrorType.NOT_FOUND_STOREDCODE);
        }
        return (String) result;
    }

    // 인증 코드를 Redis에서 삭제하는 코드
    // email에 해당하는 code를 삭제
    public void deleteVerificationCode(String email) {
        redisTemplate.delete(email);
    }
}</code></pre><h1 id="6-postman-으로-요청-보내기">6. POSTMAN 으로 요청 보내기</h1>
<ul>
<li><p>/api/v1/user/email로 인증번호를 발송해주라고 POST 요청 보내기
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/e9347471-ff12-473a-90e0-b196d52baa64/image.png" /></p>
</li>
<li><p>이메일 확인하기
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/5c66f5b1-ab67-48ce-a6ea-bb0e8abda7fb/image.png" /></p>
</li>
<li><p>api/v1/user/verify로 입력한 인증번호를 확인해주라고 POST 요청 보내기
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/e4f3c348-ea1d-4af1-aacd-c123d300d3a9/image.png" /></p>
</li>
</ul>