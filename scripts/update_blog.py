import os
from git import Repo
import feedparser

# 환경 변수에서 PAT를 가져옵니다
git_token = os.getenv('GH_PAT')

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@alsdk9349'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = Repo(repo_path)

# 사용자 정보 설정
repo.git.config('user.name', 'github-actions[bot]')
repo.git.config('user.email', 'github-actions[bot]@users.noreply.github.com')

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    file_name = entry.title
    file_name = file_name.replace('/', '-').replace('\\', '-') + '.md'
    file_path = os.path.join(posts_dir, file_name)

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)

        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}\nCo-authored-by: rimgosu <newnyup@gmail.com>')

# 변경 사항을 깃허브에 푸시
repo.git.push(f'https://{git_token}@github.com/alsdk9349/velog.git')
