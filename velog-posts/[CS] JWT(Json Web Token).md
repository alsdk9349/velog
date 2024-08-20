<h1 id="1-정의">1. 정의</h1>
<ul>
<li>JWT(Json Web Token)는 RFC 7519 웹 표준으로 지정이 되어있고, JSON 객체를 사용해서 토큰 자체에 정보들을 저장하고 있는 Web Token 입니다.</li>
</ul>
<h1 id="2-공식-페이지">2. 공식 페이지</h1>
<p><a href="https://jwt.io/">https://jwt.io/</a></p>
<h1 id="3-구조">3. 구조</h1>
<ul>
<li><p>Header, Payload, Signature 세 개의 Base64-URL 문자열로 구성되며, 점(.)으로 구분됩니다.</p>
</li>
<li><p>Header : 보통 JWT 유형, 사용되는 signature 알고리즘(HMAC SHA256 또는 RSA 등) 두 가지 정보를 담고 있습니다.</p>
<pre><code class="language-json">{
  &quot;alg&quot;: &quot;HS256&quot;,
  &quot;typ&quot;: &quot;JWT&quot;
}
</code></pre>
<ul>
<li>이 JSON은 Base64Url로 인코딩되어 JWT의 첫 번째 부분을 형성합니다.</li>
</ul>
</li>
<li><p>Payload : 서버와 클라이언트가 주고받는, 실제로 시스템에서 사용될 정보에 대한 내용들이 담겨있습니다. 페이로드는 클레임(Claims)을 포함하고 있는데, 클레임은 특정 엔터티(일반적으로 사용자) 및 추가 데이터에 대한 정보를 담고 있습니다. </p>
<ul>
<li>클레임의 세 가지 유형<ul>
<li>등록된 클레임(Registered claims): 이 클레임들은 필수는 아니지만 권장되는 사전 정의된 클레임 세트로, 유용하고 상호 운용 가능한 클레임을 제공합니다. 예를 들어, iss (발급자), exp (만료 시간), sub (주제), aud (청중) 등이 있습니다. JWT는 컴팩트한 형식을 유지하기 위해 클레임 이름이 세 글자라는 점에 유의하세요.<ul>
<li>공개 클레임(Public claims): 이는 JWT 사용자들이 자유롭게 정의할 수 있는 클레임입니다. 그러나 충돌을 피하기 위해 IANA JSON Web Token Registry에 등록하거나 충돌 방지 네임스페이스를 포함하는 URI로 정의되어야 합니다.</li>
<li>비공개 클레임(Private claims): 이는 등록된 클레임이나 공개 클레임이 아닌, 정보를 공유하는 당사자들 간에 합의된 맞춤형 클레임입니다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="language-json">{
  &quot;sub&quot;: &quot;1234567890&quot;,
  &quot;name&quot;: &quot;John Doe&quot;,
  &quot;admin&quot;: true
}</code></pre>
<ul>
<li>페이로드 역시 Base64Url로 인코딩되어 JSON Web Token의 두 번째 부분을 형성합니다.</li>
<li>조작은 불가능하지만 누구나 읽을 수 있으므로, 페이로드나 헤더에 비밀 정보를 포함하지 않아야 합니다.</li>
</ul>
</li>
<li><p>Signature : 토큰의 유효성 검증을 위한 문자열. 이 문자열을 통해 서버에서는 이 토큰이 유효한 토큰인지를 검증합니다.</p>
<ul>
<li>인코딩된 헤더, 인코딩된 페이로드, 비밀 키, 헤더에 명시된 알고리즘을 사용하여 Signature를 생성합니다.</li>
<li>예를 들어 HMAC SHA256 알고리즘을 사용하려면 서명은 다음과 같이 생성됩니다<pre><code class="language-text">HMACSHA256(
base64UrlEncode(header) + &quot;.&quot; +
base64UrlEncode(payload),
secret)</code></pre>
</li>
<li>이 Signature는 메시지가 전송 중 변경되지 않았음을 확인하는 데 사용되며, 개인 키로 서명된 토큰의 경우 JWT 발신자가 맞는지 확인할 수 있습니다.</li>
</ul>
</li>
</ul>
<ul>
<li>예시<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/b5f007b8-7f2f-44ac-9de0-68d221d3754c/image.png" /></li>
</ul>
<h1 id="4-작동-원리">4. 작동 원리</h1>
<p><img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/a809d6e8-a4d9-4c37-b115-d5ddc59878cf/image.png" /></p>
<ul>
<li>인증 과정에서 사용자가 자격 증명을 사용해 로그인에 성공하면 JSON Web Token이 반환됩니다. 이 토큰은 필요한 시간만큼 유지하는 것이 좋습니다. 또한, 브라우저 저장소에는 민감한 세션 데이터를 저장하지 않는 것이 좋습니다.</li>
<li>사용자가 보호된 경로 또는 리소스에 접근하고자 할 때, JWT를 보내야 합니다. 이때 일반적으로 Authorization 헤더에 Bearer 스키마를 사용하여 JWT를 전달합니다. 헤더의 내용은 Authorization: Bearer &lt;토큰&gt; 과 같이 표시됩니다. 경우에 따라 무상태 인증 메커니즘으로 작동할 수 있습니다. </li>
<li>서버의 보호된 경로는 Authorization 헤더에 유효한 JWT가 있는지 확인하고, 존재하면 사용자가 보호된 리소스에 접근할 수 있도록 허용합니다.</li>
<li>JWT에 필요한 데이터가 포함되어 있다면, 특정 작업을 수행할 때 데이터베이스 조회의 필요성을 줄일 수 있습니다.</li>
<li>토큰이 Authorization 헤더에 포함되어 전달되는 경우, 쿠키를 사용하지 않으므로 Cross-Origin Resource Sharing (CORS) 문제를 피할 수 있습니다.</li>
<li>애플리케이션 또는 클라이언트가 인증 서버에 인증을 요청합니다. 이는 다양한 인증 흐름 중 하나를 통해 수행됩니다. 예를 들어, OpenID Connect를 준수하는 웹 애플리케이션은 authorization code flow를 사용하여 /oauth/authorize 엔드포인트를 통해 인증을 진행할 수 있습니다.
인증이 승인되면, 인증 서버는 애플리케이션에 액세스 토큰을 반환합니다.
애플리케이션은 이 액세스 토큰을 사용하여 보호된 리소스(예: API)에 접근합니다. 서명된 토큰의 경우, 토큰에 포함된 모든 정보는 사용자나 다른 당사자에게 노출되며, 이들은 해당 정보를 변경할 수 없더라도 볼 수 있습니다. 따라서 토큰 안에 비밀 정보를 포함해서는 안 됩니다.<h1 id="5-주의할-점">5. 주의할 점</h1>
</li>
<li>JWT 토큰을 HTTP 헤더를 통해 보낼 때는 크기가 너무 커지지 않도록 주의해야 합니다. 일부 서버는 헤더 크기가 8KB를 넘지 않도록 제한하고 있습니다. 만약 JWT 토큰에 사용자 권한 전체를 포함하는 등 너무 많은 정보를 담으려 한다면, Auth0의 세분화된 권한 관리(Fine-Grained Authorization)와 같은 대안을 고려해야 할 수 있습니다.</li>
</ul>
<h1 id="5-장점">5. 장점</h1>
<ul>
<li>중앙의 인증 서버, 데이터 스토어에 대한 의존성 없음, 시스템 수평 확장 유리<ul>
<li>JWT는 클라이언트 측에 토큰이 저장되고, 서버는 토큰을 검증하여 사용자의 신원을 확인합니다. 이 과정에서 JWT는 자체적으로 서명된 토큰이기 때문에 중앙의 인증 서버나 데이터 스토어를 통해 매번 검증할 필요가 없습니다. 즉, JWT는 자체적으로 인증 정보를 담고 있어, 별도의 상태 저장소가 필요 없습니다.</li>
<li>이로 인해 서버 간 상태를 공유할 필요가 없어 시스템의 수평 확장(Scale-Out)이 용이합니다. 여러 서버로 트래픽을 분산시키더라도 각 서버가 동일한 방식으로 JWT를 검증할 수 있기 때문에, 특정 서버에 의존하지 않고 부하를 분산시킬 수 있습니다.</li>
</ul>
</li>
<li>Base64 URL Safe Encoding &gt; URL, Cookie, Header 모두 사용 가능<ul>
<li>JWT는 Base64 URL Safe Encoding으로 인코딩되어 URL, 쿠키(Cookie), HTTP 헤더(Header) 등 다양한 방식으로 안전하게 전달될 수 있습니다. 이로 인해 웹 애플리케이션에서 유연하게 사용할 수 있으며, 다양한 환경에서 호환성이 좋습니다.</li>
<li>URL에 포함시킬 때도 문제가 없고, 쿠키나 헤더로 전달할 때도 별도의 인코딩이 필요하지 않아 사용이 편리합니다.</li>
</ul>
</li>
</ul>
<h1 id="6-단점">6. 단점</h1>
<ul>
<li>Payload의 정보가 많아지면 네트워크 사용량 증가, 데이터 설계 고려 필요<ul>
<li>JWT의 페이로드(Payload)에는 사용자의 정보, 권한, 만료 시간 등의 데이터가 포함됩니다. 만약 이 데이터가 많아지면 JWT의 크기도 커지게 되고, 이를 클라이언트와 서버 간에 주고받을 때 네트워크 사용량이 증가하게 됩니다.</li>
<li>네트워크 사용량이 증가하면 성능 저하로 이어질 수 있으므로, JWT 설계 시 페이로드에 포함되는 정보를 신중하게 결정해야 합니다. 불필요하게 많은 정보를 담지 않고 최소한의 정보만 포함시키는 것이 중요합니다.</li>
</ul>
</li>
</ul>
<ul>
<li>토큰이 클라이언트에 저장, 서버에서 클라이언트의 토큰을 조작할 수 없음<ul>
<li>JWT는 클라이언트에 저장되며, 이 토큰은 클라이언트가 직접 관리하게 됩니다. 서버는 JWT를 발급한 이후에는 클라이언트의 토큰을 임의로 변경하거나 폐기할 수 없습니다.</li>
<li>이는 보안 측면에서 문제가 될 수 있습니다. 예를 들어, 사용자의 권한이 변경되거나 계정이 탈취된 경우, 기존의 JWT를 무효화할 수 없으므로 토큰의 유효기간이 끝날 때까지 해당 토큰을 사용할 수 있게 됩니다. 이를 방지하기 위해서는 토큰의 만료 시간을 짧게 설정하거나, 블랙리스트를 사용하는 등의 추가적인 보안 조치가 필요합니다.</li>
</ul>
</li>
</ul>