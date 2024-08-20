<h2 id="1-문제-링크-httpswwwacmicpcnetproblem24444">1. 문제 링크 <a href="https://www.acmicpc.net/problem/24444">https://www.acmicpc.net/problem/24444</a></h2>
<h2 id="2-문제-번호-24444">2. 문제 번호 24444<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/377f5003-4e5e-4123-8d87-a1932adafa01/image.PNG" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st= new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        arr = new ArrayList[N+1];
        visited = new boolean[N+1];
        result = new int [N+1];
        for (int i=0;i&lt;N+1;i++) {
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
            Collections.sort(arr[i]);
        }
        bfs(R);
        for (int i=1;i&lt;N+1;i++) {
            System.out.println(result[i]);
        }
    }
    static int N;
    static int M;
    static int R;
    static List&lt;Integer&gt;[]arr ;
    static boolean [] visited;
    static int [] result;
    static int count =1;
    static void bfs(int index) {
        Queue&lt;Integer&gt; q = new LinkedList&lt;Integer&gt;();
        q.offer(index);
        visited[index]=true;
        while (!q.isEmpty()) {
            int nowind = q.poll();
            result[nowind] = count++;
            for(int i=0;i&lt;arr[nowind].size();i++) {
                int check = arr[nowind].get(i);
                if(!visited[check]) {
                    visited[check] = true;
                    q.offer(check);
                }
            }
        }
    }
}</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li>bfs 구현 기본<ul>
<li>Q 선언 : Queue&lt;자료형&gt; 이름 = new LinkedList&lt;자료형&gt;();</li>
<li>요소 추가 : 이름.offer(추가할 요소);</li>
<li>Q가 비어있는지 확인 : 이름.isEmpty()</li>
<li>요소 추출 : 이름.poll();</li>
</ul>
</li>
</ul>
<ul>
<li>배열 안의 요소들을 ArrayList로 만들기<ul>
<li>import java.util.ArrayList;</li>
<li>선언 : public List&lt;자료형&gt;[]arr</li>
<li>생성 : arr = new ArrayList[초기 길이(나중에 자동으로 변함)];</li>
<li>동시에 선언 생성 : ArrayList&lt;자료형&gt; 이름 = new ArrayList&lt;&gt;(초기길이);</li>
<li>ArrayList 관련 함수 복습<ul>
<li>요소 추가 : 이름.add(추가할 요소);</li>
<li>정렬 : Collections.sort(이름);</li>
<li>요소 탐색 : 이름.get(인덱스 번호);</li>
<li>길이 구하기 : 이름.size();</li>
</ul>
</li>
</ul>
</li>
</ul>