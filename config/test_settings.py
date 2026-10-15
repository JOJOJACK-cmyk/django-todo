from .settings import *
# CRUD 로직 테스트 전용. 실제 실행은 settings.py의 MySQL을 사용합니다.
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}
