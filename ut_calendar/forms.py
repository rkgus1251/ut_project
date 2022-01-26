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
        }
        labels = {
            'date' : '날짜',
            'subject' : '진료명',
            'content' : '내용',
        }