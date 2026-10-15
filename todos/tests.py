from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo

class TodoTests(TestCase):
    def test_crud_and_completion(self):
        self.assertContains(self.client.get('/'), '등록된 할 일이 없습니다')
        self.client.post(reverse('todos:create'), {'title': '장보기', 'content': ''})
        todo = Todo.objects.get()
        self.assertFalse(todo.is_completed)
        self.assertIsNotNone(todo.created_at)
        self.client.post(reverse('todos:update', args=[todo.pk]), {'title': '공부', 'content': 'Django'})
        todo.refresh_from_db()
        self.assertEqual(todo.title, '공부')
        self.client.post(reverse('todos:toggle', args=[todo.pk]))
        todo.refresh_from_db()
        self.assertTrue(todo.is_completed)
        self.assertContains(self.client.get('/'), 'card completed')
        self.client.post(reverse('todos:toggle', args=[todo.pk]))
        todo.refresh_from_db()
        self.assertFalse(todo.is_completed)
        self.client.post(reverse('todos:delete', args=[todo.pk]))
        self.assertFalse(Todo.objects.exists())

    def test_validation_create_and_update(self):
        for title in ['', '   ', 'x' * 201]:
            response = self.client.post(reverse('todos:create'), {'title': title})
            self.assertTrue(response.context['form'].errors)
        self.assertFalse(Todo.objects.exists())
        todo = Todo.objects.create(title='원래 제목')
        response = self.client.post(reverse('todos:update', args=[todo.pk]), {'title': ''})
        self.assertContains(response, '할 일 제목을 입력해 주세요.')
        todo.refresh_from_db()
        self.assertEqual(todo.title, '원래 제목')

    def test_post_only_and_csrf(self):
        todo = Todo.objects.create(title='유지')
        for action in ['delete', 'toggle']:
            url = reverse('todos:' + action, args=[todo.pk])
            self.assertEqual(self.client.get(url).status_code, 405)
            self.assertEqual(Client(enforce_csrf_checks=True).post(url).status_code, 403)
        self.assertTrue(Todo.objects.filter(pk=todo.pk).exists())

    def test_missing_item_and_escaping(self):
        self.assertEqual(self.client.get('/999/edit/').status_code, 404)
        Todo.objects.create(title='<script>alert(1)</script>')
        self.assertContains(self.client.get('/'), '&lt;script&gt;')
