from django.shortcuts import render
from django.http import HttpResponse
import uuid
from .models import Urls

def index(request):
    return render(request, "shortner/index.html")

def create(request):
    if request.method == 'POST':
        url = request.POST['url']
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(url=url,urlid=uid)
        new_url.save()
        #return HttpResponse(uid) 
    return render(request, "shortner/link.html", {'res':uid})
        
# Create your views here.
