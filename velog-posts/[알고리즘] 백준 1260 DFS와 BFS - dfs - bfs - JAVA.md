<h2 id="1-문제-링크-httpswwwacmicpcnetproblem1260">1. 문제 링크 <a href="https://www.acmicpc.net/problem/1260">https://www.acmicpc.net/problem/1260</a></h2>
<h2 id="2-문제-번호-1260">2. 문제 번호 1260!<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/b02b9239-ecd7-437b-9f8a-cbaac72d2a2a/image.PNG" /></h2>
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
        V = Integer.parseInt(st.nextToken());
        visited = new boolean[N+1];
        arr = new ArrayList[N+1];
        result = new ArrayList[2];
        for (int i =0 ; i &lt; N+1; i++) {
            arr[i] = new ArrayList&lt;&gt;();
        }
        for (int i =0 ; i &lt;2; i++) {
            result[i] = new ArrayList&lt;&gt;();
        }
        for (int i = 0; i &lt; M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b);
            arr[b].add(a);
        }
        for (int i =0 ; i &lt; N+1; i++) {
            Collections.sort(arr[i]);
        }
        dfs(V);
        visited = new boolean[N+1];
        bfs(V);
        for (int i =0 ; i &lt; result[0].size(); i++) {
            System.out.print(result[0].get(i) + &quot; &quot;);
        }
        System.out.println();
        for (int i =0 ; i &lt; result[1].size(); i++) {
            System.out.print(result[1].get(i) + &quot; &quot;);
        }
    }
    static int N,M,V;
    static ArrayList&lt;Integer&gt; [] arr;
    static ArrayList&lt;Integer&gt; [] result;
    static boolean [] visited;
    static void dfs(int now) {
        visited[now] = true;
        result[0].add(now);
        for (int i=0 ; i &lt; arr[now].size(); i++) {
            int next = arr[now].get(i);
            if (!visited[next]) {
                dfs(next);
            }
        }
    }

    static void bfs(int start) {
        Queue&lt;Integer&gt; q = new LinkedList&lt;&gt;();
        visited[start] = true;
        q.offer(start);
        while (!q.isEmpty()) {
            int now = q.poll();
            result[1].add(now);
            for (int i=0 ; i &lt; arr[now].size(); i++) {
                int next = arr[now].get(i);
                if (!visited[next]) {
                    visited[next] = true;
                    q.offer(next);
                }
            }
        }
    }
}</code></pre>