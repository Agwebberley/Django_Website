from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'body', 'download1n', 'download1', 'download2n', 'download2')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'download1n': forms.TextInput(attrs={'class': 'form-control'}),
			'download1': forms.TextInput(attrs={'class': 'form-control'}),
			'download2n': forms.TextInput(attrs={'class': 'form-control'}),
			'download2': forms.TextInput(attrs={'class': 'form-control'}),



		}