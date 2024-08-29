<h2 id="1-문제-링크-httpssofteeraipractice6246">1. 문제 링크 <a href="https://softeer.ai/practice/6246">https://softeer.ai/practice/6246</a></h2>
<h2 id="2-문제-번호-6246">2. 문제 번호 6246<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/373d5906-66b5-4076-88c5-631c6e3fca93/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st =new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][n];
        visited = new boolean[n][n];
        for (int i=0;i&lt;n;i++) {
            st =new StringTokenizer(br.readLine());
            for (int j=0;j&lt;n;j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st =new StringTokenizer(br.readLine());
        int sty = Integer.parseInt(st.nextToken())-1;
        int stx = Integer.parseInt(st.nextToken())-1;
        goal = new int [m-1][2];
        for (int i=0;i&lt;m-1;i++) {
            st =new StringTokenizer(br.readLine());
            goal[i][0]=Integer.parseInt(st.nextToken())-1;
            goal[i][1]=Integer.parseInt(st.nextToken())-1;
        }
        visited[sty][stx] = true;
        dfs(sty,stx,0,goal[0][0],goal[0][1]);
        System.out.println(result);
    }
    static int n,m;
    static int result = 0;
    static int [][] arr;
    static int [][] goal;
    static boolean [][] visited;
    static int [] directy = {0,0,1,-1};
    static int [] directx = {1,-1,0,0};
    static void dfs (int y,int x, int goalind, int edy, int edx) {
        if (y==edy &amp;&amp; x==edx) {
            if (goalind == m-2) {
                result++;
                return;
            } else {
                dfs(y,x,goalind+1,goal[goalind+1][0],goal[goalind+1][1]);
            }
        } else {
            for (int i=0;i&lt;4;i++) {
                int ny = y+directy[i];
                int nx = x+directx[i];
                if (0&lt;=ny &amp;&amp; ny&lt;n &amp;&amp; 0&lt;=nx &amp;&amp; nx&lt;n &amp;&amp; arr[ny][nx]!=1 &amp;&amp; visited[ny][nx]==false) {
                    visited[ny][nx] = true;
                    dfs(ny,nx,goalind,edy,edx);
                    visited[ny][nx]=false;
                }
            }
        }
    }
}
</code></pre>