<h2 id="1-문제-링크-httpswwwacmicpcnetproblem16953">1. 문제 링크 <a href="https://www.acmicpc.net/problem/16953">https://www.acmicpc.net/problem/16953</a></h2>
<h2 id="2-문제-번호-16953">2. 문제 번호 16953<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/8e1a6428-c3db-48a2-9da1-5f869916ce69/image.PNG" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        A = Long.parseLong(st.nextToken());
        B = Long.parseLong(st.nextToken());
        bfs(A,B);
        System.out.println(result);
    }
    static long A;
    static long B;
    static long result = -1;
    static long[] next;
    static String sr;
    static void bfs(long start, long end) {
        Queue&lt;long[]&gt; q = new LinkedList&lt;&gt;();
        long [] arr = new long[]{start,1L};
        q.offer(arr);
        while (!q.isEmpty()) {
            long [] lst = q.poll();
            long now = lst[0];
            long count = lst[1];
            if (now==end) {
                result = count;
                break;
            }
            if (now&lt;end) {
                next = new long [] {now*2L,count+1L};
                q.offer(next);
                next = new long [] {now*10L+1L, count+1L};
                q.offer(next);
            }
        }
    }
}</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li><p>Queue 안에 배열 이용하는 법 복습</p>
<ul>
<li>Queue&lt;자료형[]&gt; 큐의 이름 = new LinkedList&lt;&gt;();</li>
<li>자료형 [] 배열 이름 = new 자료형[]{배열 구성 요소 1, 2, 3, ...};</li>
<li>큐의 이름.offer(배열 이름);</li>
<li>자료형 [] 배열 이름 2 = q.poll();</li>
<li>자료형 변수명1 = 배열 이름 2[0];</li>
<li>자료형 변수명2 = 배열 이름 2[1];</li>
</ul>
</li>
<li><p>int로 해서 [틀렸습니다]가 떴는데 게시판을 참고해 long으로 바꿨더니 정답이 되었습니다. 이유는 아직 잘 모르겠는데 long으로 해야만 답이 나오는 테케가 있었을 것으로 예상됩니다.</p>
</li>
</ul>