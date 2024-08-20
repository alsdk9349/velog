<h1 id="1-정의">1. 정의</h1>
<p>Builder 패턴은 객체 생성의 복잡성을 줄이고, 객체의 상태를 설정하는 방법을 유연하게 만들어주는 디자인 패턴입니다. 특히, 객체 생성 시 많은 매개변수나 다양한 설정을 필요로 하는 경우에 유용합니다. Java에서 Builder 패턴은 자주 사용되며, 특히 복잡한 객체를 생성할 때 유용합니다.</p>
<ul>
<li><p>구조</p>
<ul>
<li><p>Product : 빌더가 생성하는 객체입니다.</p>
</li>
<li><p>Builder : 객체를 생성하는 데 필요한 설정을 제공하는 클래스입니다. 보통 <code>Product</code> 객체를 생성하는 여러 메서드를 포함합니다.</p>
</li>
<li><p>ConcreteBuilder : <code>Builder</code> 인터페이스를 구현하는 클래스입니다. 실제 <code>Product</code> 객체를 생성하고, 속성을 설정합니다.</p>
</li>
<li><p>Director : <code>Builder</code>를 사용하여 객체를 생성하는 클래스입니다. <code>Builder</code> 객체에 필요한 설정을 제공하고, 최종 객체를 반환합니다.</p>
<h1 id="2-구현">2. 구현</h1>
<pre><code class="language-java">public class User {
private final String name;
private final int age;
private final String email;

private User(Builder builder) {
  this.name = builder.name;
  this.age = builder.age;
  this.email = builder.email;
}

public static class Builder {
  private String name;
  private int age;
  private String email;

  public Builder setName(String name) {
      this.name = name;
      return this;
  }

  public Builder setAge(int age) {
      this.age = age;
      return this;
  }

  public Builder setEmail(String email) {
      this.email = email;
      return this;
  }

  public User build() {
      return new User(this);
  }
}

@Override
public String toString() {
  return &quot;User{name='&quot; + name + &quot;', age=&quot; + age + &quot;, email='&quot; + email + &quot;'}&quot;;
}

public static void main(String[] args) {
  User user = new User.Builder()
          .setName(&quot;Alice&quot;)
          .setAge(30)
          .setEmail(&quot;alice@example.com&quot;)
          .build();

  System.out.println(user);
}
}</code></pre>
<h1 id="3-설명">3. 설명</h1>
</li>
</ul>
</li>
<li><p>User: <code>Builder</code> 패턴을 사용하는 객체입니다. <code>User</code> 객체는 <code>name</code>, <code>age</code>, <code>email</code> 필드를 가지고 있습니다.</p>
</li>
<li><p>Builder: <code>User</code> 객체를 생성하기 위한 내부 클래스로, 각 필드를 설정할 수 있는 메서드 (<code>setName</code>, <code>setAge</code>, <code>setEmail</code>)를 제공합니다. <code>build()</code> 메서드는 설정된 값을 사용하여 <code>User</code> 객체를 생성합니다.</p>
</li>
<li><p>사용 방법: <code>User.Builder</code>를 사용하여 객체를 설정하고, <code>build()</code> 메서드를 호출하여 최종 <code>User</code> 객체를 생성합니다.</p>
</li>
</ul>
<h1 id="4-장점">4. 장점</h1>
<ul>
<li>가독성 향상 : 여러 개의 매개변수를 가진 생성자를 사용할 때, 각 매개변수의 의미가 명확하지 않을 수 있습니다. <code>Builder</code> 패턴을 사용하면 각 속성을 설정하는 메서드가 명확하게 구분되므로 가독성이 높아집니다.</li>
<li>불변성 유지 : <code>Builder</code> 패턴을 사용하면 객체를 생성할 때 불변 객체를 쉽게 생성할 수 있습니다. 객체의 상태를 변경할 수 없으므로, 데이터의 무결성을 유지할 수 있습니다.</li>
<li>유연성 : 생성할 객체의 설정을 유연하게 조정할 수 있습니다. 선택적인 매개변수나 필수 매개변수를 쉽게 처리할 수 있습니다.</li>
</ul>