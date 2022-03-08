from django import forms
from .models import TestApp

class TestForm(forms.ModelForm):
    title = forms.CharField(
        label = '', 
        widget = forms.TextInput(attrs = {
                "placeholder": "Enter Title"
                }
            )
    )
    email = forms.EmailField()
    description = forms.CharField(
        required = False, 
        widget = forms.Textarea(attrs = {
                "placeholder": "Enter Description",
                'class': 'New_Class_Name2',
                'id' : 'MyIdForTextarea',
                'rows' : 20,
                'cols' : 50
            }       
        )
    )
    price = forms.FloatField(initial = 199.99)

    class Meta:
        model = TestApp
        fields = [
            'title',
            'description',
            'price'
        ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     if not "news" in title:
    #         raise forms.ValidationError("This is not a valid news")
    #     else:
    #         return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email")
    #     else:
    #         return email

class RawTestForm(forms.Form):
    title = forms.CharField(
        label = '', 
        widget = forms.TextInput(attrs = {
                "placeholder": "Enter Title"
                }
            )
    )
    description = forms.CharField(
        required = False, 
        widget = forms.Textarea(attrs = {
                "placeholder": "Enter Description",
                'class': 'New_Class_Name2',
                'id' : 'MyIdForTextarea',
                'rows' : 20,
                'cols' : 50
            }       
        )
    )
    price = forms.FloatField(initial = 199.99)
