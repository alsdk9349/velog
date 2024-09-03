<h2 id="1-문제-링크-httpssofteeraipractice6250">1. 문제 링크 <a href="https://softeer.ai/practice/6250">https://softeer.ai/practice/6250</a></h2>
<h2 id="2-문제-번호-6250">2. 문제 번호 6250<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/c383c109-8a3b-4944-830f-138484ae943b/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int [][] arr = new int[4][N];
        for (int i = 0; i&lt;3;i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0;j&lt;N;j++) {
                int k = Integer.parseInt(st.nextToken());
                arr[i][j]=k;
                arr[3][j]+=k;
            }
        }
        int [][] result = new int[4][N];
        PriorityQueue&lt;int[]&gt; pq;
        for (int i=0;i&lt;4;i++) {
            pq = new PriorityQueue&lt;&gt;((o1,o2) -&gt; Integer.compare(o2[0],o1[0]));
            for (int j=0;j&lt;N;j++) {
                pq.add(new int[]{arr[i][j],j});
            }
            int[] now = pq.poll();
            int score = now[0];
            int ind = now[1];
            int rank = 1;
            result[i][ind] = rank;
            for (int k=1;k&lt;N;k++) {
                int []next = pq.poll();
                int nscore = next[0];
                int nind = next[1];
                if(nscore==score) {
                    result[i][nind]=rank;
                } else {
                    result[i][nind] = k+1;
                    rank = k+1;
                }
                score = nscore;
            }
            for (int l=0;l&lt;N;l++) {
                System.out.print(result[i][l] + &quot; &quot;);
            }
            System.out.println();
        }
    }
}</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li>우선순위 큐 안에 배열 넣기<ul>
<li>pq = new PriorityQueue&lt;&gt;((o1,o2) -&gt; Integer.compare(o2[0],o1[0]));</li>
<li>첫 번째 원소 기준으로 내림차순 정렬</li>
</ul>
</li>
</ul>