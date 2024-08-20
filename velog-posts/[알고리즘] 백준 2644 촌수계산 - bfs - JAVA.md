<h2 id="1-문제-링크--httpswwwacmicpcnetproblem2644">1. 문제 링크  <a href="https://www.acmicpc.net/problem/2644">https://www.acmicpc.net/problem/2644</a></h2>
<h2 id="2-문제-번호-2644">2. 문제 번호 2644<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/510ebe4e-3f12-407b-9634-fbb217ac7088/image.PNG" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(br.readLine());
        arr = new ArrayList[n+1];
        visited = new boolean[n+1];
        for (int i=0;i&lt;n+1;i++) {
            arr[i] = new ArrayList&lt;&gt;();
        }
        for (int i=0;i&lt;m;i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[x].add(y);
            arr[y].add(x);
        }
        for (int i=1;i&lt;n+1;i++) {
            Collections.sort(arr[i]);
        }
        bfs(a, b);
        if (!flag) {
            System.out.println(-1);
        }

    }
    static int n,m,a,b;
    static ArrayList&lt;Integer&gt; [] arr;
    static boolean []visited;
    static boolean flag = false;
    static void bfs(int start, int end) {
        Queue&lt;Integer[]&gt; q = new LinkedList&lt;&gt;();
        Integer[] pair = new Integer[]{start,0};
        visited[start] = true;
        q.offer(pair);
        while(!q.isEmpty()) {
            Integer[] result = q.poll();
            int now = result[0];
            int count = result[1];
            if (now == end) {
                flag = true;
                System.out.println(count);
                break;
            }
            for (int i=0;i&lt;arr[now].size();i++) {
                int next = arr[now].get(i);
                if (!visited[next]) {
                    visited[next] = true;
                    Integer [] go = new Integer[]{next,count+1};
                    q.offer(go);
                }
            }
        }
    }
}</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li><p>Queue 안에 배열 넣기</p>
<ul>
<li>Queue&lt;자료형[]&gt; q = new LinkedList&lt;&gt;();</li>
<li>자료형[] 이름 = new 자료형[]{start,0};</li>
<li>q.offer(이름);</li>
</ul>
</li>
<li><p>배열 빼서 활용</p>
<ul>
<li>자료형[] 이름1 = q.poll();</li>
<li>자료형 이름2 = 이름1[인덱스];</li>
<li>자료형 이름3 = 이름1[인덱스]; 반복</li>
</ul>
</li>
</ul>