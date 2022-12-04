from django.shortcuts import render, HttpResponse
from rembg import remove

# Create your views here.
def index(request):
  if request.method == 'POST':
    image = request.FILES['image'].read()
    output = remove(image)
    return HttpResponse(output, content_type="image/jpeg")
  return render(request, 'index.html')