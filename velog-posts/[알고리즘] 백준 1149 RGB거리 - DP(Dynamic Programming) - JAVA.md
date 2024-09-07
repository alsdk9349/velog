<h2 id="1-문제-링크-httpswwwacmicpcnetproblem1149">1. 문제 링크 <a href="https://www.acmicpc.net/problem/1149">https://www.acmicpc.net/problem/1149</a></h2>
<h2 id="2-문제-번호-1149">2. 문제 번호 1149<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/84fa3d31-3c1a-4a00-8a98-2bed6f6ba6ba/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int result=(int)21e8;
        int N = Integer.parseInt(br.readLine());
        int [][] arr = new int[N][3];
        int [][] dp = new int[N][3];

        for (int i=0;i&lt;N;i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0;j&lt;3;j++) {
                arr[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        for (int j=0;j&lt;3;j++) {
            dp[0][j] = arr[0][j];
        }

        for (int i=1;i&lt;N;i++) {
            for (int j=0;j&lt;3;j++) {
                int a;
                int b;
                if (j==0) {
                    a = 1;
                    b = 2;
                } else if (j==1) {
                    a = 0;
                    b = 2;
                } else {
                    a = 0;
                    b = 1;
                }
                dp[i][j]=Math.min(dp[i-1][a],dp[i-1][b]) + arr[i][j];
            }
        }

        for (int i=0;i&lt;3;i++) {
            if (dp[N-1][i]&lt;result) {
                result = dp[N-1][i];
            }
        }
        System.out.println(result);
    }
}</code></pre>
<h2 id="4-로직">4. 로직</h2>
<ul>
<li><p>df로 풀면 시간초과가 떠서 dp로 풀었습니다. </p>
</li>
<li><p>첫 번째 집부터 각 집까지 칠하는 최소값을 찾아서 점점 채워나갑니다.</p>
<ul>
<li>우선 N행 3열의 arr 배열에 각 비용을 입력 받습니다.</li>
<li>또 다른 N행 3열의 dp 배열을 만들고 첫 번째 행을 arr의 첫 번째 행으로 채웁니다.</li>
<li>다음 행을 채울 때는 바로 직전 행의 세 개의 열 중 현재 열이 아닌 두 값을 비교해 더 작은 값에 현재 비용을 더합니다.</li>
<li>마지막 행의 세 개 열 중 최소값을 출력합니다.</li>
</ul>
</li>
<li><p>Math.min(A,B)를 하면 둘 중 작은 수를 반환합니다.</p>
</li>
</ul>