from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from rembg import remove
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def Demo(request):
  return render(request, 'demo.html')

@csrf_exempt
def Service(request):
  if request.method == 'POST' or request.method == 'PUT':
    try:
      image = request.FILES['image'].read()
      output = remove(image)
      return HttpResponse(output, content_type="image/jpeg")
    except:
      return HttpResponseBadRequest("Something went wrong!!!")
      