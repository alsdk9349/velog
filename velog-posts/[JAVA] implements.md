<h1 id="1-정의">1. 정의</h1>
<p>implements는 자바에서 인터페이스를 구현할 때 사용하는 키워드입니다. 인터페이스는 클래스가 가져야 할 메서드의 집합을 정의하며, 클래스는 이 인터페이스를 implements 키워드를 사용하여 구현할 수 있습니다.</p>
<h1 id="2-구현">2. 구현</h1>
<ul>
<li><p>인터페이스 정의</p>
<pre><code class="language-java">public interface Animal {
  void makeSound();
  void move();
}</code></pre>
</li>
<li><p>클래스에서 인터페이스 구현</p>
<pre><code class="language-java">public class Dog implements Animal{
  @Override
  public void makeSound() {
      System.out.println(&quot;woof&quot;);
  }

  @Override
  public void move() {
      System.out.println(&quot;The dog runs&quot;);
  }
}</code></pre>
</li>
<li><p>예시 코드 실행</p>
<pre><code class="language-java">public class Main {
  public static void main(String[] args) {
      Animal myDog = new Dog();
      myDog.makeSound(); //woof 출력됨
      myDog.move(); // The dog runs 출력됨
  }
}</code></pre>
<h1 id="3-설명">3. 설명</h1>
<p>여기서 Animal은 인터페이스이고, Dog 클래스는 Animal 인터페이스를 implements 키워드를 사용하여 구현합니다. Dog 클래스는 Animal 인터페이스에 정의된 모든 메서드(makeSound와 move)를 반드시 구현해야 합니다. 예시 코드를 실행하면 myDog 객체는 Animal 타입으로 선언되었지만, 실제로는 Dog 클래스의 인스턴스이므로 Dog 클래스에서 구현한 메서드들이 호출됩니다.</p>
</li>
</ul>