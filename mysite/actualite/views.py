from django.shortcuts import render

# Create your views here.
def actualite(request):
    return render(request, 'actualite/actualite.html')
