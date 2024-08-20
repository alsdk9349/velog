<h2 id="1-문제-링크-httpswwwacmicpcnetproblem7576">1. 문제 링크 <a href="https://www.acmicpc.net/problem/7576">https://www.acmicpc.net/problem/7576</a></h2>
<h2 id="2-문제-번호-7576">2. 문제 번호 7576<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/d3d249dd-15d0-457e-93a7-8c8f04f94182/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        // 배열 입력 받기
        arr = new int[N][M];
        for (int i=0;i&lt;N;i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0;j&lt;M;j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        bfs();
        System.out.println(result);

    }
    static int M, N;
    static int [][] arr;
    static int [] directy = new int [] {0,0,1,-1};
    static int [] directx = new int [] {1,-1,0,0};
    static int result;

    //처음부터 모든 토마토가 익어있는지 확인할 변수
    static boolean flag = false;

    static void bfs() {
        int [] now;
        int nexty,nextx,nextc;
        Queue&lt;int[]&gt; q = new LinkedList&lt;&gt;();

        // q안에 처음부터 익어있는 토마토 다 넣기
        for (int i=0;i&lt;N;i++) {
            for (int j=0;j&lt;M;j++) {
                if (arr[i][j] ==1) {
                    q.offer(new int[]{i,j,0});
                    flag = true;
                }
            }
        }

        // q에 하나도 안들어갔을경우 바로 return
        if (!flag) {
            result = 0;
        }

        while (!q.isEmpty()) {
            now = q.poll();
            for (int i=0;i&lt;4;i++) {
                nexty = now[0] + directy[i];
                nextx = now[1] + directx[i];
                if ( 0&lt;=nexty &amp;&amp; nexty&lt;N &amp;&amp; 0&lt;=nextx &amp;&amp; nextx&lt;M &amp;&amp; arr[nexty][nextx]==0) {
                    arr[nexty][nextx] = 1;
                    q.offer(new int[]{nexty,nextx,now[2]+1});
                    result = now[2]+1;
                }
            }
        }

        // 토마토가 모두 익었는지 확인
        for (int i=0;i&lt;N;i++) {
            for (int j=0;j&lt;M;j++) {
                if (arr[i][j]==0) {
                    result = -1;
                }
            }
        }
    }
}
</code></pre>
<h2 id="4-오답-노트">4. 오답 노트</h2>
<ul>
<li>90퍼센트 좀 넘었을 때 틀렸습니다.<ul>
<li>게시판을 찾아보다가 입력된 배열이 전부 0이었을경우 (익지 않은 토마토들만 들어왔을 경우)를 고려하지 않아서 틀렸었던 걸로 예상하고 고쳐서 해결했습니다. </li>
<li>게시판을 보지 않고 다양한 테스트케이스를 생각하는 연습을 해야겠다고 생각했습니다.</li>
</ul>
</li>
</ul>