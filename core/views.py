from django.shortcuts import render

from .forms import AuthorForm
from .models import Author
import datetime


# Create your views here.
def home(request):
    products = Author.objects.all()

    return render(request, 'home.html', {'products': products})

def index(request):
    error={}
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            error=form.errors
            data= Author.objects.create(form['cleaned_data'])
            # data.created_on=datetime.datetime.now()
            # data.last_logged_in=datetime.datetime.now(),
            data.save()

    else:
        form=AuthorForm()

    return render(request, 'index.html', {'form': form, 'error': error})

