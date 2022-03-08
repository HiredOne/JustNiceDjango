from django import forms # Import forms
from .models import Article # Import model

#2) Make form
class ArticleModelForm(forms.ModelForm): # Use this to collect the data
    class Meta: # Meta data
        model = Article # State the model
        fields = [ # State the fields to be collected 
            'title',
            'content',
            'active'
        ]