# -*- coding: utf-8 -*-
from django.conf import settings
from . import tasks
import os
import json
import threading
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import OverwriteStorage
import numpy as np
from PIL import Image
# Create your views here.

@csrf_exempt
def server(request):
	file_name = request.FILES['image']
	fs= OverwriteStorage()
	fs.save(file_name.name, file_name)
	return JsonResponse({'status' : True})
def client(request):
	
	return render(request, "client.html")