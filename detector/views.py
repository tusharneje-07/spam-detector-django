from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .detector import Gemini
import json
# Create your views here.
def detector(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        obj = Gemini(settings.API_KEY)
        data,msg = obj.checkspam(data['msg'])
        return JsonResponse({
            'data':data,
            'msg':msg
        })
    else:
        return render(request, 'index.html')
        
