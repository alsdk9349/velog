<h2 id="1-문제-링크-httpswwwacmicpcnetproblem24479">1. 문제 링크 <a href="https://www.acmicpc.net/problem/24479">https://www.acmicpc.net/problem/24479</a></h2>
<h2 id="2-문제-번호-24479">2. 문제 번호 24479<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/9723759c-a770-448a-b107-66c807f28513/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        arr = new ArrayList[N];
        for (int i = 0; i &lt; N; i++) {
            arr[i] = new ArrayList&lt;&gt;();
        }
        result = new int[N];
        visited = new int[N];
        for (int i=0;i&lt;M;i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a-1].add(b-1);
            arr[b-1].add(a-1);
        }
        for (int i=0;i&lt;N;i++) {
            Collections.sort(arr[i]);
        }
        dfs(R-1);
        for (int i=0;i&lt;N;i++) {
            System.out.println(result[i]);
        }
    }
    static ArrayList&lt;Integer&gt;[] arr;
    static int [] result;
    static int count = 1;
    static int [] visited;
    static void dfs(int index) {
        result[index] = count;
        visited[index]=1;
        for (int i=0;i&lt;arr[index].size();i++) {
            if (visited[arr[index].get(i)]!=1) {
                count++;
                dfs(arr[index].get(i));
            }
        }
    }
}</code></pre>
<h2 id="4-공부한-내용">4. 공부한 내용</h2>
<ul>
<li><p>자바에서 dfs를 구현할 때는 기본적으로 psvm 밖에서 static void dfs를 구현하고, 안에서 호출합니다.</p>
</li>
<li><p>Array와 ArrayList는 다릅니다.</p>
<table>
<thead>
<tr>
<th></th>
<th>Array</th>
<th>ArrayList</th>
</tr>
</thead>
<tbody><tr>
<td>크기 조정 가능 여부</td>
<td>고정된 크기를 가지며, 한 번 생성하면 크기를 변경할 수 없음</td>
<td>동적 배열로, 요소를 추가하거나 제거하면서 크기가 자동으로 조정</td>
</tr>
<tr>
<td>타입</td>
<td>기본 타입(int, char 등)과 참조 타입(객체) 모두 저장</td>
<td>기본 타입 직접 저장 불가, 참조 타입만 저장. 기본 타입을 저장하려면 해당 타입의 래퍼 클래스를 사용(예: int 대신 Integer)</td>
</tr>
<tr>
<td>성능</td>
<td>메모리 할당이 단순하고 빠름. 따라서 대용량 데이터를 다룰 때 더 효율적일 수 있음</td>
<td>크기 조정이 가능하기 때문에 새로운 요소를 추가할 때 성능 저하 가능성 존재. 초기 용량을 설정하면 성능 문제 해결</td>
</tr>
<tr>
<td>기능</td>
<td>단순한 데이터 구조로, 요소의 추가/삭제 등의 기능이 없음</td>
<td>요소 추가, 삭제, 검색 등 다양한 메서드를 제공. Collections 클래스와 함께 사용할 수 있는 메서드 존재</td>
</tr>
</tbody></table>
<ul>
<li>ArrayList의 메서드 예시<ul>
<li>선언 : ArrayList&lt;타입&gt; 이름 = new ArrayList&lt;&gt;(초기크기);</li>
<li>초기 크기는 생략 가능. 이후에 알아서 변함.</li>
<li>정렬 : Collections.sort(배열 이름)</li>
<li>요소 추가 : 이름.add</li>
<li>요소 조회 : 이름.get(index)</li>
<li>요소 길이 : 이름.size()</li>
</ul>
</li>
</ul>
</li>
</ul>