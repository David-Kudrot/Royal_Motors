from django import forms
from cars.models import CommentModel




class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'email', 'body']