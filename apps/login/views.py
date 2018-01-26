from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def register(request):
	errors = []
	for key, val in request.POST.items():
		if len(val) < 3:
			errors.append("{} must be at least two characters".format(key))

	if request.POST['password'] != request.POST['password_confirmation']:
		errors.append["Error: Password and password confirmation do not match."]

	if errors:
		for err in errors:
			messages.error(request, err)

	else:

		hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		print(hashpw)
	return redirect('/')