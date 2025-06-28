
from django.urls import path
from .views import hello, welcome  # ✅ Make sure welcome is imported

urlpatterns = [
    path('', hello),
    path('welcome/', welcome),
]
from django.urls import path
from .views import hello, echo

urlpatterns = [
    path('welcome/', hello),
    path('echo/', echo),  # new POST endpoint
]
from django.urls import path
from .views import hello, echo, register, login

urlpatterns = [
    path('welcome/', hello),
    path('echo/', echo),
    path('register/', register),
    path('login/', login),
]
from django.http import HttpResponse

def notify(request):
    return HttpResponse("This is the notify endpoint.")
from django.urls import path
from .views import hello, notify  # 👈 Make sure notify is imported

urlpatterns = [
    path('hello/', hello),
    path('notify/', notify),
]





