from django import forms

class ContactForm(forms.Form):
    Your_Name = forms.CharField(max_length=150,required=True)
    Email = forms.EmailField(required=True)
    Subject = forms.CharField(max_length=256, required=True)
    Body = forms.CharField(max_length=256,widget = forms.Textarea ,required=True)