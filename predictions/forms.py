from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full px-3 py-2 border rounded-md shadow-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )
