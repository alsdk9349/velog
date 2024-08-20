<h1 id="1-정의">1. 정의</h1>
<p>자바의 삼항 연산자 (ternary operator)는 조건에 따라 두 값 중 하나를 선택할 때 사용하는 간결한 표현식입니다. 삼항 연산자는 조건문을 한 줄로 작성할 수 있게 해줍니다. 표현식으로서 결과를 반환하며, 따라서 변수에 저장하거나 다른 표현식의 일부로 사용할 수 있습니다. 하지만 그 자체로는 문장을 구성할 수 없고, 반환된 값을 사용하여 다른 작업을 해야 합니다.</p>
<h1 id="2-구성">2. 구성</h1>
<pre><code class="language-sql">condition ? expression1 : expression2</code></pre>
<ul>
<li>condition : 평가되는 조건입니다. 이 조건은 true 또는 false로 평가되어야 합니다.</li>
<li>expression1 : 조건이 true일 때 반환되는 값입니다.</li>
<li>expression2 : 조건이 false일 때 반환되는 값입니다.</li>
</ul>
<h1 id="3-예시">3. 예시</h1>
<pre><code class="language-java">public class Main {
    public static void main(String[] args) {
        int N = 15;
        System.out.println((N == 15) ? &quot;A&quot; : &quot;B&quot;); // A
        String result = (N==4) ? &quot;C&quot; : &quot;D&quot;;
        System.out.println(result); // D

        // 중첩 삼항 연산자
        String result2 = (N &gt;= 20) ? &quot;20이상&quot; :
                (N &gt;= 10) ? &quot;10이상 20이하&quot; :
                        &quot;10 미만&quot;;
        System.out.println(result2); // 10이상 20이하
    }
}</code></pre>