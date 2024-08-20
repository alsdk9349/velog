<h2 id="1-문제-링크-httpswwwacmicpcnetproblem2178">1. 문제 링크 <a href="https://www.acmicpc.net/problem/2178">https://www.acmicpc.net/problem/2178</a></h2>
<h2 id="2-문제-번호-2178">2. 문제 번호 2178!<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/45a3721b-4e29-4f6e-ad3d-fb59131d6ff4/image.PNG" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        visited = new boolean[N][M];
        String s;
        Character c;
        for (int i = 0; i &lt; N; i++) {
            s = br.readLine();
            for (int j = 0; j&lt; M; j++) {
                map[i][j] = s.charAt(j)-'0';
            }
        }
        bfs(0,0,1);
    }
    static int N, M;
    static int[][] map;
    static boolean [][] visited;
    static int [] directy = new int []{0,0,1,-1};
    static int [] directx = new int []{-1,1,0,0};
    static void bfs(int y, int x, int count) {
        Queue&lt;int[]&gt; q = new LinkedList&lt;&gt;();
        visited[y][x] = true;
        q.offer(new int[] {y,x,count});
        while (!q.isEmpty()) {
            int [] now = q.poll();
            int nowy = now[0];
            int nowx = now[1];
            int nowcount = now[2];
            if (nowy == N-1 &amp;&amp; nowx == M-1) {
                System.out.println(nowcount);
                break;
            }
            for (int i = 0; i &lt; 4; i++) {
                int ny = nowy + directx[i];
                int nx = nowx + directy[i];
                if (ny &gt;=0 &amp;&amp; nx&gt;=0 &amp;&amp; ny&lt;N &amp;&amp; nx&lt;M &amp;&amp; !visited[ny][nx] &amp;&amp; map[ny][nx]==1) {
                    visited[ny][nx] = true;
                    q.offer(new int[] {ny,nx,nowcount+1});
                }
            }
        }
    }
}
</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li><p>공백이 없이 입력된 숫자들을 분리하고 싶을 때</p>
<ul>
<li>BufferedReader br을 사용할 경우 String s = br.readLine();로 입력을 받습니다.</li>
<li>int 이름 = s.charAt(인덱스)-'0'으로 형변환 합니다.</li>
</ul>
</li>
<li><p>q에 배열을 넣을 때</p>
<ul>
<li>Queue&lt;자료형[]&gt; q = new LinkedList&lt;&gt;();</li>
<li>q.offer(new 자료형[] {넣을 값1, 2, 3, ...});</li>
</ul>
</li>
</ul>