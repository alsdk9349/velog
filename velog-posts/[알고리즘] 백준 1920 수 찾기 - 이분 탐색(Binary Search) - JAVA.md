<h2 id="1-문제-링크-httpswwwacmicpcnetproblem1920">1. 문제 링크 <a href="https://www.acmicpc.net/problem/1920">https://www.acmicpc.net/problem/1920</a></h2>
<h2 id="2-문제-번호-1920">2. 문제 번호 1920<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/35455c5d-b70f-4791-94ac-00e9b3e84bd2/image.png" /></h2>
<h2 id="3-내-코드">3. 내 코드</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
         int n = Integer.parseInt(br.readLine());
         int[]na = new int[n];
         st = new StringTokenizer(br.readLine());
         for (int i=0;i&lt;n;i++) {
             na[i]=Integer.parseInt(st.nextToken());
         }
         Arrays.sort(na);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i=0;i&lt;m;i++) {
            int answer = 0;
            int k =Integer.parseInt(st.nextToken());
            int start = 0;
            int end = n-1;
            while (start&lt;=end) {
                int mid = (start+end)/2;
                if (k==na[mid]) {
                    answer=1;
                    break;
                } else if (k&lt;na[mid]) {
                    end = mid-1;
                } else {
                    start = mid +1;
                }
            }
            System.out.println(answer);
        }
    }
}</code></pre>
<h2 id="4-로직">4. 로직</h2>
<ul>
<li>이분 탐색(이진 탐색) : <strong>정렬된 배열</strong>에서 특정 값을 효율적으로 찾기 위한 알고리즘입니다. 배열을 반으로 나누면서 목표 값을 찾습니다. 배열의 중간 값을 기준으로 찾고자 하는 값이 중간 값보다 크거나 작음을 판단한 뒤, 탐색 범위를 절반으로 줄여 나가며 반복합니다.</li>
<li>과정<pre><code>1. 배열의 중간 값을 확인합니다.
2. 중간 값이 찾고자 하는 값과 같으면 탐색을 종료합니다.
3. 찾고자 하는 값이 중간 값보다 크다면 배열의 오른쪽 절반을 탐색합니다.
4. 찾고자 하는 값이 중간 값보다 작다면 배열의 왼쪽 절반을 탐색합니다.
5. 이 과정을 찾을 때까지 반복하거나 탐색 범위가 없어질 때까지 반복합니다.</code></pre></li>
<li>이분탐색은 탐색 범위를 절반씩 줄이기 때문에 시간 복잡도가 <strong>O(log n)</strong>으로 매우 효율적입니다.</li>
<li>예시<pre><code class="language-java">import java.util.Arrays;
</code></pre>
</li>
</ul>
<p>public class BinarySearch {</p>
<pre><code>// 이분탐색 함수
public static int binarySearch(int[] arr, int target) {
    int left = 0; // 탐색 범위의 왼쪽 끝
    int right = arr.length - 1; // 탐색 범위의 오른쪽 끝

    // 탐색 범위가 유효한 동안 반복
    while (left &lt;= right) {
        int mid = (left + right) / 2; // 중간 인덱스 계산

        // 목표 값을 찾은 경우
        if (arr[mid] == target) {
            return mid; // 인덱스 반환
        }

        // 중간 값이 목표 값보다 작은 경우, 오른쪽 절반 탐색
        if (arr[mid] &lt; target) {
            left = mid + 1;
        }
        // 중간 값이 목표 값보다 큰 경우, 왼쪽 절반 탐색
        else {
            right = mid - 1;
        }
    }

    // 값을 찾지 못한 경우 -1 반환
    return -1;
}

public static void main(String[] args) {
    // 예시 배열 (정렬된 상태여야 함)
    int[] arr = {1, 3, 5, 7, 9, 11, 13, 15};
    int target = 7;

    // 이분탐색 호출
    int result = binarySearch(arr, target);

    // 결과 출력
    if (result != -1) {
        System.out.println(&quot;값 &quot; + target + &quot;는 배열의 인덱스 &quot; + result + &quot;에 있습니다.&quot;);
    } else {
        System.out.println(&quot;값 &quot; + target + &quot;를 배열에서 찾을 수 없습니다.&quot;);
    }
}</code></pre><p>}</p>
<p>```</p>