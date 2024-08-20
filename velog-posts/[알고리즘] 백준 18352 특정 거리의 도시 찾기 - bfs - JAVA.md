<h2 id="1-문제-링크-httpswwwacmicpcnetproblem18352">1. 문제 링크 <a href="https://www.acmicpc.net/problem/18352">https://www.acmicpc.net/problem/18352</a></h2>
<h2 id="2-문제-번호-18352">2. 문제 번호 18352<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/b0123c30-f42c-44e7-bbed-6b33f619c8ef/image.PNG" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        arr = new ArrayList[N+1];
        for (int i=0;i&lt;N+1;i++) {
            arr[i] = new ArrayList&lt;&gt;();
        }
        visited = new boolean[N+1];
        result = new ArrayList&lt;&gt;();
        for (int i=0;i&lt;M;i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b);
        }
        bfs(X,K);
        Collections.sort(result);
        if (result.isEmpty()) {
            System.out.println(-1);
        } else {
            for (int i=0;i&lt;result.size();i++){
                System.out.println(result.get(i));
            }
        }
    }

    static int N,M,K,X;
    static ArrayList&lt;Integer&gt; [] arr;
    static boolean [] visited;
    static ArrayList&lt;Integer&gt; result;
    static void bfs(int start, int distance) {
        Queue&lt;int[]&gt; q = new LinkedList&lt;&gt;();
        int [] ins = new int[] {start,0};
        visited[start] = true;
        q.offer(ins);
        while (!q.isEmpty()) {
            int [] out = q.poll();
            int now = out[0];
            int dis = out[1];
            if (dis&gt;distance) {
                break;
            }
            if (dis==distance) {
                result.add(now);
            }
            for (int i=0;i&lt;arr[now].size();i++) {
                int num = arr[now].get(i);
                if (!visited[num]) {
                    visited[num] = true;
                    int [] next = new int[]{num,dis+1};
                    q.offer(next);
                }
            }
        }
    }
}</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li>배열 안에 ArrayList 넣는 법 복습<ul>
<li>static ArrayList&lt;자료형&gt; [] 이름;</li>
<li>이름 = new ArrayList[크기];</li>
<li>for (int i=0;i&lt;N+1;i++) {<pre><code>  이름[i] = new ArrayList&lt;&gt;();</code></pre>  }</li>
</ul>
</li>
</ul>
<h2 id="5-오답-노트">5. 오답 노트</h2>
<ul>
<li>최단거리가 아니라 지나가는 모든 숫자를 출력해서 테케 안나옴 오답 1</li>
<li>2차원 배열 ArrayList가 아닌 [][]로 해서 메모리 초과 오답 2</li>
<li>시작점 visited 체크 안해서 오답 3</li>
</ul>