from django import forms
from .models import Date


class DateInput(forms.DateInput) :
    input_type = 'date'


class ScheduleForm(forms.ModelForm) :
    class Meta :
        model = Date
        fields = ['date', 'subject', 'content']
        widgets = {
            'date' : DateInput(),
            # 'subject' : forms.TextInput(attrs={'class':'form-control'}),
            # 'content' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 10}),
        }
        labels = {
            'date' : '날짜',
            'subject' : '제목',
            'content' : '내용',
        }