from django import forms
from .models import Activity


class ToDoForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"
