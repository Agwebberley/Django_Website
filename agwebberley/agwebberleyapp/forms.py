from django import fourms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'body', 'download1n', 'download1', 'download2n', 'download2')

		widgets = {
			'title': form.TextInput


		}