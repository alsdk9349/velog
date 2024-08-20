<h2 id="1-문제-링크-httpsschoolprogrammerscokrlearncourses30lessons12916">1. 문제 링크 <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12916">https://school.programmers.co.kr/learn/courses/30/lessons/12916</a></h2>
<h2 id="2-문제-번호-12916">2. 문제 번호 12916<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/79a6ccf4-2027-46ce-85b3-ab39c0126402/image.PNG" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">class Solution {
    boolean solution(String s) {
        boolean answer = true;

        String up = s.toUpperCase();
        int cp = 0;
        int cy = 0;
        char now;
        String result;

        for (int i=0;i&lt;up.length();i++) {
            now = up.charAt(i);
            result = String.valueOf(now);
            if (result.equals(&quot;P&quot;)) {
                cp++;
            } else if (result.equals(&quot;Y&quot;)) {
                cy++;
            }
        }
        if (cp!=cy) {
            answer = false;
        }

        return answer;
    }
}</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li>문자열 내 모든 문자들을 대문자로 바꾸려면 문자열.toUpperCase(); 를 합니다.</li>
<li>String.valueOf(A); 을 하면 A가 String형으로 바뀝니다.</li>
<li>A.equals(B);로 A와 B가 같은 문자열인지 비교할 수 있습니다.</li>
</ul>