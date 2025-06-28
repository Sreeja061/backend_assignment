
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello from Django!"})
# views.py
@api_view(['GET'])
def welcome(request):
    return Response({"msg": "Welcome user!"})
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def echo(request):
    user_input = request.data.get('input', 'No input provided')
    return Response({'echo': user_input})
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status

@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": f"User '{user.username}' registered successfully"})

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        return Response({"message": f"Welcome back, {user.username}!"})
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def echo(request):
    data = request.data
    message = data.get("message")
    if not message:
        return Response({"error": "No input provided"}, status=400)
    return Response({"msg": message})
from .tasks import send_telegram_message

@api_view(['POST'])
def notify(request):
    msg = request.data.get("msg", "Hello from Django + Celery!")
    send_telegram_message.delay(msg)  # Background task
    return Response({"status": "Message is being sent..."})
from django.http import JsonResponse
from .tasks import send_telegram_message

def notify(request):
    message = "Hello from Django!"
    send_telegram_message.delay(message)  # 🧠 runs in background
    return JsonResponse({"status": "Task sent to Celery"})







