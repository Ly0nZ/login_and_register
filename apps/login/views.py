from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def register(request):
	print(request.POST)
	return redirect('/')