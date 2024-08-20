<h1 id="1-정의">1. 정의</h1>
<p>Java에서 Map은 키-값 쌍을 저장하는 자료구조를 말합니다. Map은 컬렉션 프레임워크의 일부로, 각 키가 하나의 값에 매핑되는 구조를 제공합니다. 이를 통해 특정 키에 해당하는 값을 빠르게 조회하거나 수정할 수 있습니다. Map은 데이터베이스의 테이블이나 레코드를 다룰 때 유용하게 사용될 수 있습니다.</p>
<h1 id="2-구현">2. 구현</h1>
<pre><code class="language-java">import java.util.HashMap;
import java.util.Map;

public class MapExample {
    public static void main(String[] args) {
        // Map 생성
        Map&lt;String, Integer&gt; map = new HashMap&lt;&gt;();

        // 값 추가
        map.put(&quot;apple&quot;, 1);
        map.put(&quot;banana&quot;, 2);
        map.put(&quot;cherry&quot;, 3);

        // 값 조회
        System.out.println(&quot;Value for 'apple': &quot; + map.get(&quot;apple&quot;));

        // 키 존재 여부 확인
        if (map.containsKey(&quot;banana&quot;)) {
            System.out.println(&quot;Map contains 'banana'&quot;);
        }

        // 값 삭제
        map.remove(&quot;cherry&quot;);
        System.out.println(&quot;After removing 'cherry': &quot; + map);

        // 전체 조회
        System.out.println(&quot;All keys: &quot; + map.keySet());
        System.out.println(&quot;All values: &quot; + map.values());
        System.out.println(&quot;All entries: &quot; + map.entrySet());
    }
}</code></pre>
<h1 id="3-기본-제공-메서드">3. 기본 제공 메서드</h1>
<ul>
<li>put(K key, V value): 지정된 키와 값을 맵에 추가합니다.</li>
<li>get(Object key): 주어진 키에 대한 값을 반환합니다.</li>
<li>remove(Object key): 지정된 키와 관련된 값을 삭제합니다.</li>
<li>containsKey(Object key): 지정된 키가 맵에 존재하는지 확인합니다.</li>
<li>containsValue(Object value): 지정된 값이 맵에 존재하는지 확인합니다.</li>
<li>size(): 맵에 있는 키-값 쌍의 수를 반환합니다.</li>
<li>isEmpty(): 맵이 비어 있는지 확인합니다.</li>
<li>clear(): 모든 키-값 쌍을 맵에서 제거합니다.</li>
<li>keySet(): 맵에 포함된 모든 키를 반환합니다.</li>
<li>values(): 맵에 포함된 모든 값을 반환합니다.</li>
<li>entrySet(): 맵에 포함된 모든 키-값 쌍을 반환합니다.</li>
</ul>
<h1 id="4-주요-구현체">4. 주요 구현체</h1>
<ul>
<li>HashMap :해시 테이블을 기반으로 하며, 키와 값의 쌍을 빠르게 저장하고 조회할 수 있습니다. 순서를 보장하지 않으며, 기본적으로 동기화되지 않습니다.</li>
<li>LinkedHashMap : HashMap을 확장한 클래스입니다. 입력 순서(또는 액세스 순서)를 유지합니다. 요소의 순서를 보장할 수 있어서, 순서가 중요한 경우 유용합니다.</li>
<li>TreeMap : 이진 탐색 트리 기반으로, 키를 자연 순서 또는 생성 시 제공된 비교기로 정렬하여 저장합니다. 정렬된 키 순서로 요소를 반환하며, 키를 정렬된 상태로 유지합니다.</li>
<li>ConcurrentHashMap : 멀티스레드 환경에서 사용하기 적합한 동기화된 HashMap 구현체입니다. 높은 동시성 성능을 제공하며, 여러 스레드가 동시에 접근할 수 있도록 설계되었습니다.</li>
</ul>
<h1 id="5-작동-원리">5. 작동 원리</h1>
<ul>
<li>해시 테이블 : HashMap은 내부적으로 해시 테이블을 사용하여 데이터를 저장합니다. 해시 함수를 통해 키를 해시 값으로 변환하고, 이 값을 통해 테이블의 인덱스를 결정합니다.</li>
<li>트리 구조 : TreeMap은 내부적으로 트리 구조를 사용하여 키를 정렬된 상태로 유지합니다. 이를 통해 키의 순서를 보장하며, 정렬된 순서로 데이터를 조회할 수 있습니다.</li>
<li>동기화 : ConcurrentHashMap은 동기화된 맵으로, 멀티스레드 환경에서 안전하게 사용될 수 있도록 설계되었습니다. 락을 사용하여 동시성을 제공하며, 성능을 최적화합니다.</li>
</ul>