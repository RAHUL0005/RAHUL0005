from django import forms
from .models import Task,register
from django.contrib.admin.widgets import AdminDateWidget

class XYZ_DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"
    def __init__(self, **kwargs):
        # kwargs["format"] = "%Y-%m-%d %H:%M"
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        # kwargs["format"] = '%d/%m/%Y %H:%M'
        super().__init__(**kwargs)

class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = '%d/%m/%Y'
        super().__init__(**kwargs)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'due_date': XYZ_DateInput(format=["%Y-%m-%d"], ),

        }
class RegForm(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'
        # widgets = {'password': forms.PasswordField}

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
