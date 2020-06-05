from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User,UserActivity
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
# from .serializers import SnippetSerializer


from .serializers import UserActivitySerializer,UserSerializer
# Create your views here.
def home(request,id):
    try:
        userdata = User.objects.get(ids=id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(userdata)
        # print(serializer.data)
        return JsonResponse(serializer.data)
