<h2 id="1-문제-링크-httpswwwacmicpcnetproblem10844">1. 문제 링크 <a href="https://www.acmicpc.net/problem/10844">https://www.acmicpc.net/problem/10844</a></h2>
<h2 id="2-문제-번호-10844">2. 문제 번호 10844<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/428c5f58-551d-482e-b007-8c27811865f1/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        BigInteger[][] arr = new BigInteger[n+1][10];
        arr[1][0]=BigInteger.ZERO;
        for (int i=1;i&lt;10;i++) {
            arr[1][i]=BigInteger.ONE;
        }
        if (n&gt;1) {
            for (int i=2;i&lt;n+1;i++) {
                arr[i][0]=arr[i-1][1];
                for (int j=1;j&lt;9;j++) {
                    arr[i][j]=arr[i-1][j-1].add(arr[i-1][j+1]);
                }
                arr[i][9]=arr[i-1][8];
            }
        }

        BigInteger res = BigInteger.ZERO;
        for (int i=0;i&lt;10;i++) {
            res = res.add(arr[n][i]);
        }
        System.out.println(res.remainder(BigInteger.valueOf(1000000000)));
    }
}</code></pre>
<h2 id="4-로직">4. 로직</h2>
<ul>
<li>자료형은 int로 해도 안되고 long으로 해도 안돼서 BigInteger를 썼습니다.</li>
<li>BigInteger<pre><code class="language-java">// import
import java.math.BigInteger;
</code></pre>
</li>
</ul>
<p>public class Main {
    public static void main(String[] args) throws IOException {</p>
<pre><code>    // 선언
    BigInteger A = new BigInteger(&quot;10&quot;);
    BigInteger B = new BigInteger(&quot;5&quot;);

    // 0,1,2,10 은 바로 선언 가능
    BigInteger Zero = BigInteger.ZERO;
    BigInteger One = BigInteger.ONE;
    BigInteger Two = BigInteger.TWO;
    BigInteger Ten = BigInteger.TEN;

    // 연산
    BigInteger C = A.add(B); // 더하기
    BigInteger D = A.subtract(B); // 빼기
    BigInteger E = A.multiply(B); // 곱하기
    BigInteger F = A.divide(B); // 나누기 - 몫
    BigInteger G = A.remainder(B); // 나누기 - 나머지

    // 형 변환
    BigInteger H = BigInteger.valueOf(1); // 다른 자료형 -&gt; BigInteger
    String I = A.toString(); // BigInteger -&gt; 문자형
    double J = A.doubleValue(); // BigInteger -&gt; 숫자형(다른 숫자형들도 가능)

    // 비교
    int K = A.compareTo(B); // 1(A가 더 클 때)
    int L = B.compareTo(A); // -1(A가 더 작을 때)
    int M = A.compareTo(BigInteger.valueOf(10)); // 0(같을 때)

}</code></pre><p>}</p>
<p>```</p>
<ul>
<li>먼저 2차원 배열을 만듭니다.</li>
<li>1번 인덱스에 넣는 배열은 1자리 계단수의 1의 자리 수의 개수를 세서 넣습니다.<ul>
<li>예를 들면 1자리 계단수는 1,2,3,4,5,6,7,8,9 이기 때문에 1번 인덱스의 배열은 [0,1,1,1,1,1,1,1,1,1] 형태가 됩니다.</li>
</ul>
</li>
<li>2번 부터는 앞의 배열을 이용해서 만듭니다.<ul>
<li>직전 인덱스의 배열에서 1의 자리가 1인 수에서만 현재 0으로 올 수 있습니다. (arr[i][0]=arr[i-1][1];)</li>
<li>1~8까지는 직전 인덱스의 배열에서 현재의 수보다 1 작은 수, 1 큰 수에서 올 수 있습니다. (arr[i][j]=arr[i-1][j-1].add(arr[i-1][j+1]);)</li>
<li>직전 인덱스의 배열에서 1의 자리가 8인 수에서만 현재 9로 올 수 있습니다. (arr[i][9]=arr[i-1][8];)</li>
</ul>
</li>
<li>n번째 배열까지 만든 후 n번 배열의 요소의 합을 출력합니다.</li>
</ul>