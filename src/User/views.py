from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . forms import UserForm

def index(request):
    return render(request, 'User/home.html')


def about(request):
    return render(request, 'User/about.html')


def contact(request):
    forms = UserForm()

    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('contact')

    return render(request, 'User/contact.html', {'forms': forms})
