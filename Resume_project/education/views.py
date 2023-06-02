from django.shortcuts import render

def skillpage(request):
    context = {'skill':'active'}
    return render(request, 'education/skill.html', context)