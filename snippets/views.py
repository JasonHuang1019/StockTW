from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,StockSerializer
import requests
from snippets.stock_scrapy import total

#%%
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from snippets.serializers import UserSerializer, GroupSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    查看、编辑用户的界面
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    查看、编辑组的界面
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def Line_Notify(token, message):
    headers = {"Authorization": "Bearer " + token}
    param = {'message': message}
    # image = {'imageFile' : open(str(img), 'rb')}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = param)
    return r.status_code

def Line_Notify_img(token, message, img):
    headers = {"Authorization": "Bearer " + token}
    param = {'message': message}
    image = {'imageFile' : open(str(img), 'rb')}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = param, files = image)
    return r.status_code


#%%
@csrf_exempt
def stock_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        token = 'Sy9rJxszlzspDGHBZsarWuA1NuDqSLo6dWkZ09dwxat'
        title, table = total()
        status = Line_Notify_img(token, title, 'table.png')
        status ={'status':status}
        # serializer = StockSerializer(status, many=True)
        
        return JsonResponse(status, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
#%%
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        print(snippets)
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)