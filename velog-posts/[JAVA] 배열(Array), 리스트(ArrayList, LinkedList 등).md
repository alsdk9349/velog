<h1 id="1-배열array">1. 배열(Array)</h1>
<ul>
<li><p>메모리의 연속 공간에 값이 채워져 있는 형태의 자료구조입니다.</p>
</li>
<li><p>고정된 크기를 가진 배열은 한 번 선언하면 크기를 늘리거나 줄일 수 없습니다.</p>
</li>
<li><p>선언한 자료형의 값만 저장할 수 있습니다.</p>
</li>
<li><p>배열의 값은 인덱스를 통해 바로 참조할 수 있습니다.</p>
</li>
<li><p>새로운 값의 삽입이나 특정 인덱스의 값을 삭제하기 어렵습니다. 값을 삽입하거나 삭제하려면 해당 인덱스 주변에 있는 값을 이동시키는 과정이 필요합니다.</p>
<pre><code class="language-java">// 정수형(int) 배열 선언과 초기화
int[] numbers = new int[5];  // 크기가 5인 배열을 선언

// 배열에 값 할당
numbers[0] = 10;
numbers[1] = 20;
numbers[2] = 30;
numbers[3] = 40;
numbers[4] = 50;

// 배열 선언과 동시에 초기화
int[] numbers2 = {10, 20, 30, 40, 50};</code></pre>
</li>
</ul>
<h1 id="2-리스트">2. 리스트</h1>
<ul>
<li>리스트는 노드를 포인터로 연결한 자료구조입니다.<ul>
<li>노드 : 값과 포인터를 쌍으로 갖는 기초 단위(둘 다 필수는 아님)<pre><code>  - 값(Value): 노드가 담고 있는 실제 데이터입니다.</code></pre><ul>
<li>포인터(Pointer): 다음 노드가 어디에 있는지 가리키는 주소입니다. 다른 노드의 위치(주소)를 알고 있는 일종의 &quot;화살표&quot;로 컴퓨터 메모리 상의 특정 위치를 가리키는 변수입니다. 이 주소를 통해서 컴퓨터는 해당 데이터를 접근할 수 있게 됩니다.</li>
<li>예를 들어 첫 번째 노드에는 값 10이 있고, 두 번째 노드를 가리키는 포인터가 있습니다. 두 번째 노드에는 값 20이 있고, 세 번째 노드를 가리키는 포인터가 있습니다. 마지막 세 번째 노드에는 값 30이 있고, 다음 노드를 가리키는 포인터는 없습니다(이것을 종종 &quot;null&quot; 포인터라고 합니다).</li>
</ul>
</li>
</ul>
</li>
<li>인덱스가 없으므로 값에 접근하려면 Head 포인터부터 순서대로 접근해야 합니다(값에 접근하는 속도 느림).</li>
<li>포인터로 연결되어 있으므로 데이터를 삽입하거나 삭제하는 연산 속도가 빠릅니다.</li>
<li>선언할 때 크기를 별도로 지정하지 않아도 되며 크기가 가변적입니다.</li>
<li>포인터를 저장할 공간이 필요하므로 배열보다 구조가 복잡합니다.</li>
</ul>
<h3 id="a-arraylist">A. ArrayList</h3>
<pre><code class="language-java">import java.util.ArrayList;
import java.util.List;

// 정수형(int) 리스트 선언
List&lt;Integer&gt; numbers = new ArrayList&lt;&gt;();

// 리스트에 값 추가
numbers.add(10);
numbers.add(20);
numbers.add(30);

// 리스트의 크기
int size = numbers.size();  // 리스트에 들어있는 요소의 개수를 반환

// 리스트에서 값 가져오기
int value = numbers.get(0);  // 인덱스 0의 값을 가져옴

// 리스트 선언과 동시에 초기화 (Java 9 이상에서 사용 가능)
List&lt;Integer&gt; numbers2 = List.of(10, 20, 30, 40, 50);
</code></pre>
<h3 id="b-linkedlist">B. LinkedList</h3>
<pre><code class="language-java">import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {
        // LinkedList 객체 생성
        LinkedList&lt;String&gt; list = new LinkedList&lt;&gt;();

        // 리스트에 요소 추가
        list.add(&quot;첫 번째&quot;);
        list.add(&quot;두 번째&quot;);
        list.add(&quot;세 번째&quot;);

        // 리스트의 요소 출력
        System.out.println(&quot;리스트 요소: &quot; + list); // 리스트 요소: [첫 번째, 두 번째, 세 번째]

        // 특정 위치에 요소 추가
        list.add(1, &quot;중간에 추가된 요소&quot;);

        // 리스트의 특정 위치의 요소 가져오기
        String element = list.get(2);
        System.out.println(&quot;인덱스 2의 요소: &quot; + element); // 인덱스 2의 요소: 두 번째

        // 리스트의 요소 삭제
        list.remove(&quot;두 번째&quot;);
        System.out.println(&quot;리스트 요소(삭제 후): &quot; + list); // 리스트 요소(삭제 후): [첫 번째, 중간에 추가된 요소, 세 번째]

        // 리스트의 크기 확인
        System.out.println(&quot;리스트 크기: &quot; + list.size()); // 리스트 크기: 3
    }
}</code></pre>
<h1 id="3-비교">3. 비교</h1>
<table>
<thead>
<tr>
<th></th>
<th>배열(Array)</th>
<th>리스트(ArrayList)</th>
<th>리스트(LinkedList)</th>
</tr>
</thead>
<tbody><tr>
<td>크기변경</td>
<td>X</td>
<td>O(자동 조절)</td>
<td>O(자동 조절)</td>
</tr>
<tr>
<td>요소 삽입/삭제</td>
<td>불가능 - O(n)</td>
<td>O(n)</td>
<td>O(1)</td>
</tr>
<tr>
<td>인덱스</td>
<td>O</td>
<td>O</td>
<td>X</td>
</tr>
<tr>
<td>접근 속도</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(n)-노드를 순차적으로 탐색</td>
</tr>
<tr>
<td>메모리 효율</td>
<td>연속된 메모리 블록에 저장되므로 효율적</td>
<td>내부 배열의 크기가 초과하면 새로운 배열을 할당하고 기존 배열의 요소를 복사해야 하므로 비용이 발생</td>
<td>각 노드가 다음 노드와 이전 노드를 가리키는 두 개의 포인터를 가지므로 메모리 사용이 비효율적</td>
</tr>
<tr>
<td>사용 예시</td>
<td>- 크기가 고정된 데이터가 필요한 경우<br />- 인덱스를 통해 빠르게 접근해야하는 경우</td>
<td>- 크기가 동적으로 변할 수 있는 데이터가 필요한 경우<br />- 빠른 읽기와 크기 조절이 중요한 경우</td>
<td>-빈번한 삽입과 삭제가 필요한 경우<br />- 요소의 추가와 삭제가 많고, 읽기 성능이 크게 중요하지 않은 경우</td>
</tr>
<tr>
<td>데이터 저장 방식</td>
<td></td>
<td>내부적으로 배열을 사용</td>
<td>내부적으로 이중 연결 리스트를 사용</td>
</tr>
<tr>
<td>알고리즘</td>
<td>정렬, 이진 탐색, 고정된 크기의 데이터를 처리하는 경우</td>
<td>동적 크기의 데이터를 처리해야 하고, 인덱스를 통한 접근이 중요한 경우</td>
<td>큐나 스택을 구현하거나, 데이터의 빈번한 삽입 및 삭제가 필요한 경우</td>
</tr>
</tbody></table>