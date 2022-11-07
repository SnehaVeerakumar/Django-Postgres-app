from django import forms
from .models import GeeksforGeeks

class geeks(forms.ModelForm):
  class Meta:
    model = GeeksforGeeks
    fields = ["fullname", "mobile_number",]
    labels = {'fullname': "Name", "mobile_number": "Mobile Number",}