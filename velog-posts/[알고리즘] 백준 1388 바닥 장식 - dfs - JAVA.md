<h2 id="1-문제-링크-httpswwwacmicpcnetproblem1388">1. 문제 링크 <a href="https://www.acmicpc.net/problem/1388">https://www.acmicpc.net/problem/1388</a></h2>
<h2 id="2-문제-번호-1388">2. 문제 번호 1388<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/b9e8932a-6c77-4659-bc7d-344708fcab98/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new String[N][M];
        for (int i=0;i&lt;N;i++) {
            String sentence = br.readLine();
            for (int j=0;j&lt;M;j++) {
                arr[i][j] = String.valueOf(sentence.charAt(j));
            }
        }
        for (int i=0;i&lt;N;i++) {
            for (int j=0;j&lt;M;j++) {
                if (arr[i][j].equals(&quot;-&quot;) || arr[i][j].equals(&quot;|&quot;)) {
                    dfs(i,j);
                }
            }
        }
        System.out.println(count);
    }
    static String [][] arr;
    static int count = 0;
    static int N;
    static int M;
    static void dfs(int indy, int indx) {
        if (arr[indy][indx].equals(&quot;-&quot;)) {
            arr[indy][indx]=&quot;0&quot;;
            if (indx+1 &lt; M &amp;&amp; arr[indy][indx+1].equals(&quot;-&quot;)) {
                dfs(indy,indx+1);
            } else if (indx+1&lt;M) {
                count+=1;
                dfs(indy, indx+1);
            } else {
                count+=1;
            }
        } else if (arr[indy][indx].equals(&quot;|&quot;)) {
            arr[indy][indx]=&quot;0&quot;;
            if (indy+1&lt;N &amp;&amp; arr[indy+1][indx].equals(&quot;|&quot;)) {
                dfs(indy+1, indx);
            } else if (indy+1&lt;N) {
                count+=1;
            } else {
                count+=1;
            }
        }
    }
}</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li><p>공백이 없을 때는 StringTokenizer를 이용해 분리할 수 없습니다.</p>
<ul>
<li>문자열.charAt(인덱스값)으로 문자열의 특정 위치에 있는 문자를 반환합니다.</li>
<li>String.valueof(변환할 값)를 이용해 Character를 다시 String으로 형변환 합니다.</li>
</ul>
</li>
<li><p>문자열을 비교할 때는 ==이 아닌 A.equals(B)로 해야합니다.</p>
</li>
</ul>