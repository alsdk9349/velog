<h1 id="1-정의">1. 정의</h1>
<p>Docker는 컨테이너화된 소프트웨어와 마이크로서비스를 구축, 공유 및 실행할 수 있도록 도와주는 오픈소스 플랫폼입니다. 가상화된 컨테이너는 애플리케이션과 그 애플리케이션이 동작하는 데 필요한 모든 것을 포함하는 가볍고 독립적인 패키지입니다. 이를 통해 개발자들은 애플리케이션을 다양한 환경(예: 개발 환경, 테스트 환경, 프로덕션 환경)에서 일관되게 실행할 수 있습니다.</p>
<h1 id="2-장점">2. 장점</h1>
<ul>
<li><p>복잡한 설정에 소요되는 시간을 줄여 코드 작성에 집중할 수 있도록 도와줍니다</p>
</li>
<li><p>포트 매핑, 파일 시스템 문제 및 기타 기본 설정을 자동으로 처리하며, 정기적으로 버그 수정 및 보안 업데이트를 제공합니다.</p>
</li>
<li><p>개발 도구와 언어를 자유롭게 선택하여 사용할 수 있으며, Docker Hub에서 인증된 이미지와 템플릿의 방대한 라이브러리에 접근할 수 있습니다. 이를 통해 개발 팀은 안전한 저장소를 사용하여 환경을 확장하고, 자동 빌드 및 지속적 통합을 신속하게 수행하며 협업할 수 있습니다.</p>
<h1 id="3-구성-요소">3. 구성 요소</h1>
</li>
<li><p>도커 엔진(Docker Engine): 도커의 핵심 컴포넌트로, 컨테이너를 생성하고 실행하는 역할을 합니다. 도커 엔진은 클라이언트-서버 아키텍처로 구성되어 있습니다. 도커 데몬(Docker Daemon)이 서버 역할을 하며, 도커 클라이언트(Docker Client)를 통해 사용자가 명령을 내릴 수 있습니다.</p>
</li>
<li><p>도커 이미지(Docker Image): 컨테이너를 생성하는 데 사용되는 불변의 템플릿입니다. 이미지에는 애플리케이션 코드와 함께 해당 애플리케이션을 실행하는 데 필요한 모든 라이브러리와 종속성이 포함됩니다.</p>
</li>
<li><p>도커 컨테이너(Docker Container): 이미지에서 생성된 실행 가능한 인스턴스입니다. 컨테이너는 독립적으로 실행되며, 필요에 따라 생성되고 삭제될 수 있습니다.</p>
</li>
<li><p>도커 허브(Docker Hub): 도커 이미지를 저장하고 공유할 수 있는 클라우드 기반의 저장소입니다. 개발자들은 이곳에서 공식 이미지나 커뮤니티에서 제공하는 다양한 이미지를 사용할 수 있습니다.</p>
</li>
<li><p>도커 컴포즈(Docker Compose): 다중 컨테이너 애플리케이션을 정의하고 실행할 수 있도록 돕는 도구입니다. docker-compose.yml 파일을 사용하여 여러 컨테이너의 설정을 정의하고 한꺼번에 관리할 수 있습니다.</p>
</li>
<li><p>도커 네트워크(Docker Network): 컨테이너 간의 네트워크 연결을 관리합니다. 서로 다른 컨테이너들이 네트워크를 통해 통신할 수 있도록 도와줍니다.</p>
</li>
<li><p>도커 볼륨(Docker Volume): 컨테이너가 종료되어도 데이터를 유지할 수 있도록 데이터를 저장하는 방법을 제공합니다.</p>
</li>
</ul>
<h1 id="4-사용-방법">4. 사용 방법</h1>
<ol>
<li><p>도커 설치: 도커 데스크탑(Docker Desktop)을 설치하여 로컬 개발 환경에 도커 엔진과 관련 도구들을 설치합니다.</p>
</li>
<li><p>도커 이미지 생성: Dockerfile이라는 텍스트 파일을 작성하여 도커 이미지를 정의합니다. Dockerfile에는 애플리케이션을 어떻게 설치하고 설정할지에 대한 명령들이 포함됩니다.</p>
</li>
<li><p>도커 이미지 빌드: 작성한 Dockerfile을 사용해 도커 이미지를 빌드합니다. 이 이미지는 특정 애플리케이션의 모든 종속성과 함께 패키징된 형태입니다.</p>
</li>
<li><p>도커 컨테이너 실행: 빌드된 이미지를 기반으로 컨테이너를 생성하고 실행합니다. 이때 명령어를 통해 필요한 설정(포트 매핑, 환경 변수 등)을 지정할 수 있습니다.</p>
</li>
<li><p>도커 컴포즈 사용: 여러 컨테이너로 구성된 애플리케이션을 실행할 때는 docker-compose.yml 파일을 작성하여 docker-compose up 명령어로 모든 컨테이너를 한 번에 실행할 수 있습니다.</p>
</li>
<li><p>컨테이너 관리: 컨테이너를 시작, 중지, 삭제하거나 로그를 확인하고 네트워크 연결 상태를 관리하는 등의 작업을 수행할 수 있습니다.</p>
</li>
</ol>
<h1 id="5-공식-페이지">5. 공식 페이지</h1>
<p><a href="https://www.docker.com/">https://www.docker.com/</a></p>