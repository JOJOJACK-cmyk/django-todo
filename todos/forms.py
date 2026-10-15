from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content', 'is_completed']
        widgets = {'content': forms.Textarea(attrs={'rows': 5})}
        error_messages = {'title': {
            'required': '할 일 제목을 입력해 주세요.',
            'max_length': '제목은 200자 이하로 입력해 주세요.',
        }}
