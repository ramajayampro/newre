from django import forms
from todolist_app.models import Tasklist






class TaskForm(forms.ModelForm):
    class Meta:
       model = Tasklist
       fields = ['clientname', 'task', 'startdate', 'enddate',  'messagelogs', 'assignee','status', 'fstatus']




class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


