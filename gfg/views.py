from django.shortcuts import render
from .models import GeeksforGeeks
from .forms import geeks

def gfgForm(request):
  if request.method == "POST":
    form = geeks(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = geeks()
  return render(request, 'contact.html', {'form': form})