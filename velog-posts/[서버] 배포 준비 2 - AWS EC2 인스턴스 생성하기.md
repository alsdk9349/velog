<h1 id="1-aws-ec2">1. AWS EC2</h1>
<ul>
<li><p>EC2(Amazon Elastic Compute Cloud)는 아마존 웹 서비스(AWS)에서 제공하는 클라우드 컴퓨팅 서비스 중 하나로, 사용자가 가상 서버를 생성하고 관리할 수 있는 기능을 제공합니다. EC2는 사용자가 필요한 만큼의 컴퓨팅 파워를 쉽게 확보하고, 필요에 따라 확장하거나 축소할 수 있는 유연한 환경을 제공합니다.</p>
</li>
<li><p>특징</p>
<ul>
<li>가상 서버 제공: EC2는 사용자가 원하는 운영 체제(예: Linux, Windows)와 설정을 가진 가상 서버(인스턴스라고 함)를 생성할 수 있게 해줍니다.</li>
<li>유연한 확장성: 사용자는 필요에 따라 인스턴스의 수와 크기를 자유롭게 조정할 수 있습니다. 예를 들어, 트래픽이 많은 기간에는 더 많은 인스턴스를 추가하고, 트래픽이 적을 때는 줄일 수 있습니다.</li>
<li>다양한 인스턴스 타입: EC2는 다양한 종류의 인스턴스 타입을 제공합니다. 인스턴스 타입은 CPU, 메모리, 스토리지 및 네트워크 성능 등 특정한 용도를 위해 최적화되어 있습니다. 예를 들어, 일반적인 용도의 인스턴스, 고성능 컴퓨팅에 적합한 인스턴스, 메모리 집약적인 애플리케이션을 위한 인스턴스 등이 있습니다.</li>
<li>비용 효율성: EC2는 사용한 만큼만 비용을 지불하는 방식(종량제)입니다. 따라서 초기 하드웨어 투자 없이 필요에 따라 리소스를 사용할 수 있고, 필요하지 않을 때는 인스턴스를 종료하여 비용을 절감할 수 있습니다.</li>
<li>안정성과 보안성: EC2는 AWS의 인프라를 기반으로 높은 안정성과 보안성을 제공합니다. 데이터 센터의 물리적 보안, 네트워크 보안, 사용자 인증 및 권한 관리 등 다양한 보안 기능을 포함합니다.</li>
<li>다양한 스토리지 옵션: EC2 인스턴스는 여러 가지 스토리지 옵션을 지원합니다. 예를 들어, 인스턴스 스토어(일시적 저장소), Amazon EBS(Elastic Block Store)라는 영구 스토리지, 그리고 Amazon S3(Simple Storage Service)를 사용할 수 있습니다.</li>
</ul>
</li>
<li><p>활용 방안</p>
<ul>
<li>웹 애플리케이션 호스팅</li>
<li>데이터 분석 및 처리</li>
<li>게임 서버 운영</li>
<li>백엔드 서버</li>
<li>소프트웨어 개발 및 테스트 환경 구축</li>
<li>고성능 컴퓨팅(예: 머신러닝, 빅데이터 분석)</li>
</ul>
</li>
</ul>
<h1 id="2-aws-가입하기">2. AWS 가입하기</h1>
<ul>
<li>링크 : <a href="https://aws.amazon.com/ko/?nc2=h_lg">https://aws.amazon.com/ko/?nc2=h_lg</a></li>
<li>홈페이지 -&gt; AWS 계정 생성
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/1c70a9f3-cc26-4f6f-bd77-2ac742c22ad1/image.png" /></li>
<li>회원가입 , 로그인</li>
</ul>
<h1 id="3-ec2-인스턴스-생성">3. EC2 인스턴스 생성</h1>
<ul>
<li><p>홈 화면<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/8017683d-e6a8-49c5-8812-9b8fa83175b0/image.png" /></p>
<ul>
<li>지역 : 서울</li>
<li>검색 : ec2</li>
<li>서비스 : ec2선택</li>
</ul>
</li>
<li><p>인스턴스 시작 <img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/61f9266e-5bd4-4273-a846-1964e1815890/image.png" /></p>
</li>
<li><p>설정</p>
<ul>
<li><p>이름 : 원하는 이름 입력</p>
</li>
<li><p>소프트웨어 선택
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/87a52e4b-94a6-440e-b221-6769ef3e2f6e/image.png" /></p>
</li>
<li><p>AMI / 인스턴스 유형 선택
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/5a35244c-cf16-41d6-830c-8b87d40e4425/image.png" /></p>
</li>
<li><p>키 생성</p>
<ul>
<li>키 페어 이름 : 원하는 키 이름 입력</li>
<li>RSA / pem 선택 후 키 페어 생성</li>
<li>만들어진 pem파일 저장, 보관(나중에 필요)
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/f24944b5-63a9-409f-8c59-f043e3ccdb29/image.png" />
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/1a1ccc87-06fd-472c-a98d-1e3b49e391b1/image.png" /></li>
</ul>
</li>
<li><p>네트워크 : 기본 설정(수정 가능)
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/ca411858-b81f-4edd-b5db-7205fd7dfdef/image.png" /></p>
</li>
<li><p>스토리지 : 최대 30까지 무료 사용 가능
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/0b43f707-7f7d-427e-934c-f57d0fe1b404/image.png" /></p>
</li>
<li><p>인스턴스 시작!
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/aa7599a0-e12d-454b-9b9f-d3e8f21f5ce9/image.png" /></p>
</li>
<li><p>인스턴스 창에서 확인 가능
<img alt="" src="https://velog.velcdn.com/images/alsdk9349/post/f9796aca-0859-4857-b18a-a669fdeefb96/image.png" /></p>
</li>
</ul>
</li>
</ul>