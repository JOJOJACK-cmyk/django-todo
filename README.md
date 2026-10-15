# Django Todo List

Django 5.2 / Python 3.10 이상 / MySQL 8.0.11 이상. 개인 로컬 실습용 앱입니다.

## 구현 기능
- Todo 등록·목록·수정·삭제
- 목록의 체크박스로 완료/미완료 전환, 완료 항목 취소선 및 배경색
- 제목 필수 및 200자 제한, 등록·수정 오류 메시지
- 내용 선택 입력, 생성 일시 자동 저장
- Admin 모델 등록, CSRF 적용, 삭제·완료 변경은 POST만 허용

## Windows PowerShell 실행 순서
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```
`.env`에서 DB_PASSWORD를 실제 MySQL 비밀번호로 변경하고 DJANGO_SECRET_KEY에 임의의 긴 문자열을 넣습니다. DB_USER와 DB_PORT도 본인 환경에 맞춥니다.
MySQL Workbench에서 아래 구문만 먼저 실행합니다.
```sql
CREATE DATABASE IF NOT EXISTS todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
이어서 터미널에서 실행합니다.
```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- 목록: http://127.0.0.1:8000/
- 관리자: http://127.0.0.1:8000/admin/

`schema.sql`은 제출용 Todo 테이블 DDL입니다. 실제 설치는 마이그레이션으로 Todo 및 관리자용 테이블을 함께 생성합니다. schema.sql의 CREATE TABLE과 migrate를 중복 실행하지 마세요. Boolean 기본값과 생성 일시 자동 입력은 Django 모델에서 처리하므로 DDL에 DEFAULT가 없습니다.

## 검증
MySQL에 연결한 상태에서:
```powershell
python manage.py check
python manage.py test
python manage.py sqlmigrate todos 0001
```
MySQL 없이 CRUD 로직만 확인할 때는 `python manage.py test --settings=config.test_settings`를 사용합니다. 이 검사는 MySQL 연동 검증을 대체하지 않습니다.

## GitHub 제출
GitHub에서 빈 저장소 `django-todo`를 만든 뒤, 압축을 푼 프로젝트 폴더에서 실행합니다.
```powershell
git init
git add .
git commit -m "Implement Django Todo CRUD with MySQL"
git branch -M main
git remote add origin https://github.com/JOJOJACK-cmyk/django-todo.git
git push -u origin main
```
계정이 다르면 remote URL의 사용자명을 변경합니다. `.env`는 업로드하지 않습니다. 업로드 완료 후 실제 저장소 주소와 schema.sql 내용을 제출합니다.
