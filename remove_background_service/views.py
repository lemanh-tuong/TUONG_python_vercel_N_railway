from django.shortcuts import render
from rembg import remove
import cv2
from django.conf import settings


# Create your views here.
def index(request):
  return render(request, 'index.html')