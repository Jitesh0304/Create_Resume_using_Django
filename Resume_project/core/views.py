from django.shortcuts import render


def homepage(request):
    context = {'home':'active'}
    return render(request, 'core/home.html', context)


def contactpage(request):
    context = {'contact':'active'}
    return render(request, 'core/contact.html', context)