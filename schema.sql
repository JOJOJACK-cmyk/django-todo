-- 제출용 Todo 테이블 DDL (MySQL 8 이상)
-- 실제 프로젝트 최초 설치는 CREATE DATABASE 실행 후 manage.py migrate 사용.
-- migrate와 아래 CREATE TABLE을 같은 DB에 중복 실행하지 마세요.
CREATE DATABASE IF NOT EXISTS todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE todo_db;
CREATE TABLE todos_todo (
    id BIGINT NOT NULL AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    content LONGTEXT NOT NULL,
    is_completed BOOL NOT NULL,
    created_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
-- is_completed=False와 created_at 자동 입력은 Django ORM이 적용합니다.
-- content 미입력 시 ORM은 빈 문자열을 저장합니다.
