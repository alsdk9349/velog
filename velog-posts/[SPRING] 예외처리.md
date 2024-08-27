<h1 id="예외-처리-방식">예외 처리 방식</h1>
<ol>
<li>전역 예외 처리 (Global Exception Handling) : 애플리케이션 전반에서 발생할 수 있는 예외를 한 곳에서 관리하는 방식</li>
</ol>
<ul>
<li><p>스프링에서는 @ControllerAdvice와 @ExceptionHandler를 사용합니다.</p>
<ul>
<li>@ControllerAdvice: 모든 컨트롤러에 전역적으로 적용할 수 있는 예외 처리기를 정의합니다.</li>
<li>@ExceptionHandler: 특정 예외가 발생했을 때 실행할 메서드를 지정합니다.</li>
</ul>
</li>
<li><p>예제</p>
<pre><code class="language-java">@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity&lt;String&gt; handleResourceNotFoundException(ResourceNotFoundException ex) {
        return new ResponseEntity&lt;&gt;(ex.getMessage(), HttpStatus.NOT_FOUND);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity&lt;String&gt; handleGlobalException(Exception ex) {
        return new ResponseEntity&lt;&gt;(&quot;Internal Server Error&quot;, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}</code></pre>
</li>
</ul>
<ol start="2">
<li>로컬 예외 처리 (Local Exception Handling) : 특정 컨트롤러에서 발생하는 예외만을 처리하는 방식</li>
</ol>
<ul>
<li><p>@ExceptionHandler 어노테이션을 컨트롤러 클래스 내부에 직접 사용합니다.</p>
<pre><code class="language-java">
    // UserController는 ResourceNotFoundException을 자체적으로 처리
@RestController
public class UserController {

    @GetMapping(&quot;/user/{id}&quot;)
    public User getUserById(@PathVariable String id) {
        // 사용자 조회 로직
        throw new ResourceNotFoundException(&quot;User not found with id &quot; + id);
    }

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity&lt;String&gt; handleResourceNotFoundException(ResourceNotFoundException ex) {
        return new ResponseEntity&lt;&gt;(ex.getMessage(), HttpStatus.NOT_FOUND);
    }
}</code></pre>
</li>
</ul>
<ol start="3">
<li>표준 예외 클래스</li>
</ol>
<ul>
<li>스프링은 RuntimeException을 확장한 다양한 표준 예외 클래스를 제공합니다.</li>
<li>예시<ul>
<li>DataAccessException: 데이터 액세스 계층에서 발생하는 예외를 나타냅니다.</li>
<li>TransactionException: 트랜잭션 관리와 관련된 예외를 나타냅니다.</li>
<li>HttpClientErrorException, HttpServerErrorException: REST 클라이언트에서 발생하는 HTTP 4xx, 5xx 에러를 나타냅니다.</li>
</ul>
</li>
</ul>
<h1 id="custom-예외처리-만들기">Custom 예외처리 만들기</h1>
<ul>
<li><p>예외 던지기</p>
<ul>
<li>던지고 싶은 곳에서 throw new CustomException(ErrorType.NOT_FOUND_USER);<ul>
<li>NOT_FOUND_USER 부분을 원하는 문자로 설정<pre><code class="language-java">public void test(Long Id) {
Optional&lt;User&gt; ou = userRepository.findById(Id);
if ( ou.isPresent() ) {
    // 성공했을 때 로직
}
else {
    throw new CustomException(ErrorType.NOT_FOUND_USER);
}</code></pre>
</li>
</ul>
</li>
</ul>
</li>
<li><p>CustomException.java 만들기</p>
<ul>
<li>RuntimeException 상속</li>
<li>@RequiredArgsConstructor : final 필드를 매개변수로 받는 생성자를 자동으로 생성(여기서는 private final ErrorType errorType;에 적용됨)<pre><code class="language-java">import lombok.Getter;
import lombok.RequiredArgsConstructor;
</code></pre>
</li>
</ul>
<p>@Getter
@RequiredArgsConstructor
public class CustomException extends RuntimeException {</p>
<pre><code>// CustomException 클래스가 발생할 때 함께 전달할 예외의 유형을 정의
  // ErrorType은 예외의 세부 사항을 정의하는 또 다른 클래스
private final ErrorType errorType;

@Override
// 부모 클래스(RuntimeException)의 getMessage() 메서드를 재정의
public String getMessage() {
//  예외가 발생했을 때 사용자에게 보여줄 메시지 반환
// errorType 객체의 getMsg() 메서드를 호출
    return errorType.getMsg();
}</code></pre><p>}
```</p>
</li>
<li><p>ErrorType.java 만들기</p>
<pre><code class="language-java">import lombok.Getter;

@Getter
public enum ErrorType {

    // 여러 개의 에러 정의 가능
    CONTENT_IS_NULL(400, &quot;입력되지 않은 정보가 있습니다.&quot;),
    NOT_FOUND_USER(401, &quot;등록된 사용자가 없습니다.&quot;)

    private int code;
    private String msg;

    ErrorType(int code, String msg) {
        this.code = code;
        this.msg = msg;
    }
}</code></pre>
<h1 id="역할">역할</h1>
</li>
<li><p>유연성과 유지 보수성 향상시킵니다.</p>
</li>
<li><p>안정성과 가독성을 높일 수 있습니다. </p>
</li>
<li><p>적절한 예외 처리를 통해 사용자에게 보다 친화적인 에러 메시지를 제공하고, 시스템의 오류를 효율적으로 관리할 수 있습니다.</p>
</li>
</ul>