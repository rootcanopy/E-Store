from django.shortcuts import render


# DISPLAY USERS PROFILE
def profile(request):
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
