from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def user(request):
	if not 'user_id' in request.session:
		return redirect('/')

	users = User.objects.all()
	context = {
		'users': users
	}
	return render(request, 'login/user.html', context)

def register(request):
	errors = []
	for key, val in request.POST.items():
		if len(val) < 3:
			errors.append("{} must be at least two characters".format(key))

	if request.POST['password'] != request.POST['password_confirmation']:
		errors.append("Error: Password and password confirmation do not match.")

	if errors:
		for err in errors:
			messages.error(request, err)

	else:

		hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(first_name = request.POST['first_name'],\
							last_name = request.POST['last_name'],\
							password = hashpw,\
							email = request.POST['email'])
		request.session['user_id'] = user.id

		return redirect('/user')

def login(request):
	try:
		user = User.objects.get(email = request.POST['email'])
		# bcrypt.checkpw(given_password, stored_password)
		if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
			request.session['user_id'] = user.id
			return redirect('/user')
		else:
			messages.error(request, "Email/Password combination incorrect.")
			return redirect('/')
	except User.DoesNotExist:
		messages.error(request, "Email does not exist. Please try again.")
		return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')

