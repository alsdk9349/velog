<h3 id="-여기부터는-앞에-설치했던-무료-ec2로-안될수도-있습니다">* 여기부터는 앞에 설치했던 무료 ec2로 안될수도 있습니다.</h3>
<h3 id="-다른-말이-없을-경우-기본적으로-앞에서-연결한-mobaxterm의-터미널에-명령어를-입력하면-됩니다">* 다른 말이 없을 경우 기본적으로 앞에서 연결한 mobaxterm의 터미널에 명령어를 입력하면 됩니다.</h3>
<h1 id="1-도커docker">1. 도커(Docker)</h1>
<ul>
<li>설치 <pre><code># Docker 설치를 위한 패키지 업데이트
sudo apt-get update
</code></pre></li>
</ul>
<h1 id="필요-패키지-설치">필요 패키지 설치</h1>
<p>sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common</p>
<h1 id="docker의-gpg-키-추가">Docker의 GPG 키 추가</h1>
<p>curl -fsSL <a href="https://download.docker.com/linux/ubuntu/gpg">https://download.docker.com/linux/ubuntu/gpg</a> | sudo apt-key add -</p>
<h1 id="docker-저장소-추가">Docker 저장소 추가</h1>
<p>sudo add-apt-repository &quot;deb [arch=amd64] <a href="https://download.docker.com/linux/ubuntu">https://download.docker.com/linux/ubuntu</a> $(lsb_release -cs) stable&quot;</p>
<h1 id="docker-패키지-목록-업데이트">Docker 패키지 목록 업데이트</h1>
<p>sudo apt-get update</p>
<h1 id="docker-설치">Docker 설치</h1>
<p>sudo apt-get install -y docker-ce</p>
<pre><code>- 설치 확인</code></pre><h1 id="docker-버전-확인">Docker 버전 확인</h1>
<p>docker --version</p>
<pre><code>- 서비스 시작 및 상태 확인</code></pre><h1 id="docker-서비스-시작">Docker 서비스 시작</h1>
<p>sudo systemctl start docker</p>
<h1 id="docker-서비스-상태-확인">Docker 서비스 상태 확인</h1>
<p>sudo systemctl status docker</p>
<pre><code>- 실행 중인 컨테이너 확인(아직 뭐 없음)</code></pre><p>sudo docker ps</p>
<pre><code>- EC2 인스턴스가 재부팅될 때 Docker와 Jenkins가 자동으로 시작되게 설정</code></pre><p>sudo systemctl enable docker</p>
<pre><code># 2. 엔진엑스(Nginx)
- 설치</code></pre><h1 id="시스템-패키지-업데이트">시스템 패키지 업데이트</h1>
<p>sudo apt update</p>
<h1 id="nginx-설치">NGINX 설치</h1>
<p>sudo apt install nginx</p>
<pre><code>- NGINX 버전 확인</code></pre><p>nginx -v</p>
<pre><code>- NGINX 서비스 시작</code></pre><p>sudo systemctl start nginx</p>
<pre><code>
- 서버가 재부팅될 때 NGINX가 자동으로 시작되도록 설정</code></pre><p>sudo systemctl enable nginx</p>
<pre><code>- NGINX 상태 확인</code></pre><p>sudo systemctl status nginx</p>
<pre><code>- 설정 테스트 및 재시작</code></pre><h1 id="설정-파일-테스트">설정 파일 테스트</h1>
<p>sudo nginx -t</p>
<h1 id="nginx-재시작">NGINX 재시작</h1>
<p>sudo systemctl restart nginx</p>
<pre><code>

# 3. MySQL
- 설치</code></pre><h1 id="패키지-목록-업데이트하기">패키지 목록 업데이트하기</h1>
<p>sudo apt update</p>
<h1 id="mysql-설치하기">MySQL 설치하기</h1>
<p>sudo apt install mysql-server -y</p>
<pre><code>- 버전 확인</code></pre><p>mysql --version</p>
<pre><code>- 서비스 시작하기</code></pre><p>sudo systemctl start mysql</p>
<pre><code>- 상태 확인하기</code></pre><p>sudo systemctl status mysql
```</p>