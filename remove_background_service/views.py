from django.shortcuts import render
from rembg import remove
import cv2
from django.conf import settings

input_path = settings.MEDIA_ROOT + '/1.jpg'
output_path = 'output.png'
input = cv2.imread(input_path)
output = remove(input)
cv2.imwrite(output_path, output)

# Create your views here.
def index(request):
  return render(request, 'index.html')