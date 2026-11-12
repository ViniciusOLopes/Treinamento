from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.TextInput(attrs={
                'style': 'font-size: 18px'
                })}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {
            'text': forms.Textarea(attrs={
                'cols':48,
                'style': 'font-size: 18px'
                })}