from django import fourms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'body', 'download1n', 'download1', 'download2n', 'download2')

		widgets = {
			'title': form.TextInput(attrs={'class': 'form-control'}),
			'author': form.TextInput(attrs={'class': 'form-control'}),
			'body': form.TextInput(attrs={'class': 'form-control'}),
			'download1n': form.TextInput(attrs={'class': 'form-control'}),
			'download1': form.TextInput(attrs={'class': 'form-control'}),
			'download2n': form.TextInput(attrs={'class': 'form-control'}),
			'download2': form.TextInput(attrs={'class': 'form-control'}),



		}