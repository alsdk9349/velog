<h1 id="1-정의">1. 정의</h1>
<p>RowMapper는 Java에서 주로 JDBC(Java Database Connectivity)와 함께 사용되는 인터페이스입니다. 이 인터페이스는 SQL 쿼리의 결과 집합(ResultSet)을 Java 객체로 매핑(mapping)하는 역할을 합니다. RowMapper를 사용하면 데이터베이스 쿼리 결과를 객체로 변환하여, 객체 지향 프로그래밍의 장점을 살릴 수 있습니다. 일반적으로 RowMapper는 다음과 같은 메소드를 정의한 인터페이스입니다.</p>
<pre><code class="language-java">public interface RowMapper&lt;T&gt; {
    T mapRow(ResultSet rs, int rowNum) throws SQLException;
}</code></pre>
<p>여기서 T는 매핑하려는 자바 객체의 타입입니다. mapRow 메소드는 JDBC ResultSet에서 데이터를 추출하여 원하는 객체 타입(T)으로 변환하는 역할을 합니다. 매개변수 rs는 JDBC ResultSet 객체로부터 데이터를 추출하고, rowNum은 현재 행의 인덱스를 나타냅니다.</p>
<h1 id="2-구현">2. 구현</h1>
<pre><code class="language-java">import org.springframework.jdbc.core.RowMapper;
import java.sql.ResultSet;
import java.sql.SQLException;

public class UserRowMapper implements RowMapper&lt;User&gt; {
    @Override
    public User mapRow(ResultSet rs, int rowNum) throws SQLException {
        User user = new User();
        user.setId(rs.getInt(&quot;id&quot;));
        user.setName(rs.getString(&quot;name&quot;));
        user.setEmail(rs.getString(&quot;email&quot;));
        return user;
    }
}</code></pre>
<h1 id="3-설명">3. 설명</h1>
<ul>
<li>UserRowMapper는 User 객체에 데이터베이스에서 가져온 id, name, email 등의 정보를 매핑하는 역할을 합니다. JDBC Template을 사용할 때, 이러한 RowMapper를 활용하여 데이터베이스 결과를 자바 객체로 변환하는 과정을 간단하게 처리할 수 있습니다.</li>
<li>이 코드에서는 <code>UserRowMapper</code> 클래스가 <code>RowMapper&lt;User&gt;</code> 인터페이스를 구현하고 있으며, <code>mapRow</code> 메서드에서 <code>ResultSet</code>의 각 행을 <code>User</code> 객체로 변환하고 있습니다.</li>
<li><code>int rowNum</code>은 <code>RowMapper</code> 인터페이스의 <code>mapRow</code> 메서드에서 각 행의 순서를 나타내는 인덱스입니다. 이 인덱스는 현재 처리 중인 행이 ResultSet의 몇 번째 행인지를 나타냅니다. 이는 0부터 시작하는 인덱스가 아니라 1부터 시작하는 인덱스입니다.</li>
<li>RowMapper의 주요 메서드는 <code>mapRow(ResultSet rs, int rowNum)</code>입니다. 이 메서드는 ResultSet 객체에서 한 행(row)의 데이터를 읽어 Java 객체로 변환하고, 변환된 객체를 반환합니다.</li>
</ul>