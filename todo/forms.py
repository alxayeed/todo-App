from django import forms

class TodoForm(forms.Form):
	text = forms.CharField(max_length = 60,
		widget=forms.TextInput({'class':'form-control', 'placeholder': 'Enter todo e.g. Delete junk files', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))