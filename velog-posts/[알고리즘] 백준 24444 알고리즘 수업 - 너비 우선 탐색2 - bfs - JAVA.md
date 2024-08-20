<h2 id="1-문제-링크-httpswwwacmicpcnetproblem24445">1. 문제 링크 <a href="https://www.acmicpc.net/problem/24445">https://www.acmicpc.net/problem/24445</a></h2>
<h2 id="2-문제-번호-24445">2. 문제 번호 24445<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/b383870d-39de-49e8-9adf-d58703f00e88/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        result = new int[N+1];
        arr = new ArrayList[N+1];
        visited = new boolean[N+1];
        for (int i=1;i&lt;N+1;i++) {
            arr[i] = new ArrayList&lt;&gt;();
        }
        for (int i=0;i&lt;M;i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b);
            arr[b].add(a);
        }
        for (int i=1;i&lt;N+1;i++) {
            Collections.sort(arr[i],Collections.reverseOrder());
        }
        bfs(R);
        for (int i=1;i&lt;N+1;i++) {
            System.out.println(result[i]);
        }
    }
    static int N;
    static int M;
    static int R;
    static List&lt;Integer&gt;[] arr;
    static int [] result;
    static int count = 1;
    static boolean [] visited;
    static void bfs(int ind) {
        Queue&lt;Integer&gt; q = new LinkedList&lt;Integer&gt;();
        q.offer(ind);
        result[ind] = count++;
        visited[ind] = true;
        while (!q.isEmpty()) {
            int now = q.poll();
            for (int i=0;i&lt;arr[now].size();i++) {
                int next = arr[now].get(i);
                if (!visited[next]) {
                    q.offer(next);
                    result[next] = count++;
                    visited[next] = true;
                }
            }
        }
    }
}</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li><p>자료형 명시</p>
<ul>
<li>static List&lt;자료형&gt;[] 이름; 자료형을 필수로 넣어줘야합니다.</li>
<li>Queue&lt;자료형&gt; q = new LinkedList&lt;자료형&gt;(); 자료형을 필수로 넣어줘야합니다.</li>
</ul>
</li>
<li><p>ArrayList를 내림차순으로 정렬하는법은 Collections.sort(이름,Collections.reverseOrder());입니다.</p>
</li>
</ul>