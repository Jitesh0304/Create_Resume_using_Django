from django.shortcuts import render


def servicepage(request):
    context = {'service':'active'}
    return render(request, 'service/serv.html', context)