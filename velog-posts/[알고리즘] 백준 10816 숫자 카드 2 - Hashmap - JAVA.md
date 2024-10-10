<h2 id="1-문제-링크-httpswwwacmicpcnetproblem10816">1. 문제 링크 <a href="https://www.acmicpc.net/problem/10816">https://www.acmicpc.net/problem/10816</a></h2>
<h2 id="2-문제-번호-10816">2. 문제 번호 10816<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/aed88095-a510-460e-879a-220a0a3f9a14/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        HashMap&lt;String,Integer&gt; hashMap = new HashMap&lt;&gt;();
        for (int i=0; i&lt;N;i++) {
            String s = st.nextToken();
            hashMap.put(s, hashMap.getOrDefault(s,0) +1);
        }

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i=0;i&lt;M;i++) {
            String t = st.nextToken();
            System.out.println(hashMap.getOrDefault(t,0));

        }
    }
}
</code></pre>
<h2 id="4-풀이-과정">4. 풀이 과정</h2>
<ul>
<li>총 네 번의 시간초과를 거쳐 성공했습니다.<ul>
<li>투포인터로 풀었는데 시작하자마자 시간 초과</li>
<li>해시맵을 적용하긴 했는데 키가 있는지를 확인하는 로직을 한 번 거쳤어서 시작하자마자 시간 초과</li>
<li>키로 바로 조회해도 14%에서 시간 초과</li>
<li>해시맵 안에 넣는 키를 Integer형식으로 변환하는 과정을 뺐더니 4%에서 시간 초과</li>
<li>print + 공백으로 출력하지 않고 println으로 바꿨더니 성공</li>
</ul>
</li>
<li>새로 알게된 getOrDefault : hashmap에서 조회되지 않을 경우 직접 지정한 기본값으로 반환합니다.<ul>
<li>hashMap.put(s, hashMap.getOrDefault(s,0) +1); 해석</li>
<li>hashMap에 s를 키로 hashMap.getOrDefault(s,0) +1를 넣습니다.</li>
<li>hashMap.getOrDefault(s,0)는 hashMap에서 s를 키로 하는 값을 반환하되, 없을 경우 기본 값인 1을 넣습니다.</li>
</ul>
</li>
</ul>