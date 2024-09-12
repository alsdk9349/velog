<h1 id="1-mobaxterm">1. MobaXterm</h1>
<ul>
<li>MobaXterm은 원격 컴퓨팅을 위한 올인원 도구로, Windows 환경에서 다양한 네트워크 기능과 Unix 명령어를 제공하는 소프트웨어입니다.</li>
<li>특징<ul>
<li>SSH, X11, RDP, VNC, FTP, MOSH 등 다양한 원격 네트워크 프로토콜을 지원</li>
<li>bash, ls, cat, sed, grep, awk, rsync 등 Unix 명령어를 Windows 환경에서 사용</li>
<li>X11 그래픽 환경을 지원하여 원격 서버의 GUI 애플리케이션을 로컬 Windows 데스크톱에서 실행 가능</li>
<li>SH로 원격 서버에 연결할 때, 그래픽 SFTP 브라우저가 자동으로 열려 원격 파일을 직접 편집 가능</li>
<li>모든 기능이 하나의 포터블 실행 파일(.exe)로 제공되어 별도의 설치 없이 사용</li>
<li>무료로 사용 가능(일부 기능 유료)</li>
<li>SSH 연결을 사용하여 그래픽 애플리케이션과 파일 전송을 안전하게 암호화(원격 작업 중 데이터 보안을 보장)</li>
<li>PuTTY 기반으로, 안티앨리어스 폰트와 매크로 지원을 제공하는 탭 형식의 터미널을 제공<h1 id="2-설치">2. 설치</h1>
</li>
</ul>
</li>
<li>공식 페이지 : <a href="https://mobaxterm.mobatek.net/">https://mobaxterm.mobatek.net/</a>
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/145337d6-fe3d-40a1-9cb1-d6c6560fa0ab/image.png" /></li>
<li>Home Edition 다운로드
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/90f5ddea-69bb-4d3e-b96d-60e9620b0341/image.png" /></li>
<li>Installer edition 선택
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/a787b246-eee5-4bc2-b389-548ebc1d1381/image.png" /></li>
<li>다운받은 파일 압축풀기<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/d64fb40a-0c17-411c-a542-df19a1f92656/image.png" /></li>
<li>파일 실행<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/23b1f1b1-44b1-477d-8250-d955299487eb/image.png" /></li>
<li>설치<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/020bbe03-140b-42c6-921d-37135c13f4b9/image.png" />
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/6c37fa8d-c0a2-4731-9aa0-d20aeb922b4d/image.png" />
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/c4c919e0-cbbf-4a3c-aa2a-03f2736720d9/image.png" />
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/af6cfb38-4a4d-4d12-be4d-926d385c1eb6/image.png" />
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/61b91e15-bc2f-44ed-b700-9ae69aa3cabd/image.png" /></li>
</ul>
<h1 id="3-실행">3. 실행</h1>
<ul>
<li>생성된 바로가기 클릭
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/1025add2-34f1-4e1c-9794-627172012f85/image.png" /></li>
<li>한국어 설정
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/05b44a56-671c-4b4d-8c3e-f8f53a883b5d/image.png" />
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/c2042c20-caff-4350-af32-3945801122f8/image.png" />
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/d0e0b1a6-5a74-41dc-8ccf-b20cbb30db5b/image.png" />
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/2e13b0b0-93fa-4338-b250-0277d57a9826/image.png" /></li>
</ul>
<h1 id="4-ssh-연결하기">4. SSH 연결하기</h1>
<p><img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/c056937d-3da8-4bfe-bf00-e2e81f2dcc89/image.png" /></p>
<ul>
<li>Session</li>
<li>SSH</li>
<li>Remote host : 도메인 or IP 주소</li>
<li>Specify username : 사용할 이름 입력 </li>
<li>Advanced SSH settings</li>
<li>Use private key : 필요할 경우 보안 키 선택(ec2인스턴스 생성할 때만든 pem 파일 등)</li>
</ul>