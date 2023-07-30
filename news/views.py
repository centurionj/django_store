from django.shortcuts import redirect
from django.contrib.auth.models import User

from aut.models import UserProfile


def update_spam_preference(request):
    email = request.POST.get('email')
    user = User.objects.get(email=email)
    profile = UserProfile.objects.get(user=user)
    profile.ready_to_spam = True
    profile.save()
    return redirect('index')
