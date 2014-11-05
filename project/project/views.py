from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
from django.utils.decorators import method_decorator

from PIL import Image, ImageEnhance

from form import UserRegistrationForm
from form import UserProfile
from form import UploadFileForm 

import helper
import logging
import os
import re
import subprocess

PATH = '/var/www/slowergram/project/project'
logging.warn("WSGI sends to the Apache2 error_log.")  #Used to log to apache's error.log


def edit(request):
	if request.method == 'POST':
		brightness = float(request.POST.get('brightness', -9)) #set default to -9
		image = request.POST.get('src', None)
		if brightness is -9 or image is None:
			return HttpResponse(status = 400)
		m = re.match(r'^/slowergram/(.*)\?.*$', image)  #Grab the name of the image plus extension
		if not m:
			return HttpResponse(status = 404)
		path_to_file = PATH + '/' + m.group(1)
		img = Image.open(path_to_file)
		enhancer = ImageEnhance.Brightness(img)
		brightness = helper.convert_brightness(brightness)
		enhanced_image = enhancer.enhance(brightness)
		enhanced_image.save(path_to_file)
	return HttpResponseRedirect('/slowergram')


def delete_image(request):
	if request.user.is_authenticated():
		image = request.POST.get('src', None)
		if image is None:
			return HttpResponse(status = 400)
		m = re.match(r'^/slowergram/(.*)\?.*$', image)  #Grabs file name
		if not m:
			return HttpResponse(status = 404)
		path_to_file = PATH + '/' + m.group(1)
		os.remove(path_to_file)
		return HttpResponseRedirect('/slowergram')
	return HttpResponse(status = 404)


def handle_uploaded_file(f, user, title):
	m = re.match(r'.*\.(.*)', f.name)
	with open(PATH + '/users/' + user.username + '/' + title + '.' + m.group(1), 'wb+') as destination:
		for chunk in f.chunks():	#looping over chunks ensures large files don't overwhelm system memory
			destination.write(chunk)

def home(request):
	user = request.user
	if user.is_authenticated():
		profile = user.get_profile()
		profile_name = user.username
		if profile.picture:
			profile_image = '/slowergram/media/' + str(profile.picture)
		else:
			profile_image = '/slowergram/media/default.jpg'
		content = {
			'name' : profile_name,
			'image' : profile_image
		}
	    	return render(request, 'index.html', content)
	return render(request, 'index.html')

def main(request):
	if request.user.is_authenticated():
		request.session.set_expiry(600) #Sets session expire to 10 minutes
		user = request.user
 	  	image_list = helper.find_images(PATH + '/users/' + user.username)
		images = []
		for image in image_list:
			m = re.match(r'(.*)\.', image)  #grabs file name without extension
			images.append({
				'path' : '/slowergram/users/' + user.username + '/' + image,
				'name' : m.group(1) if m else image,
			})
		content = {
			'gallery' : images, #image_list_path,
			'form' : UploadFileForm()
		}
		return render(request, 'main.html', content)
	else:
		return HttpResponseRedirect('/slowergram/login')


def register(request):
	#TODO(mike): Redirect failed registration into correct window instead of new one
	registered = False
	if request.method == 'POST':
		user_form = UserRegistrationForm(data=request.POST)  #Fills form with POST data
		profile_form = UserProfile(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.save()			#saves new user
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()			# saves new user profile
			registered = True
			os.mkdir(PATH + '/users/' + user.username, 0775)   #Creates user directory
		else:
			print user_form.errors, profile_form.errors  #Will output to apache's error.log

	else:
		user_form = UserRegistrationForm() #creates forms to pass to the front end for filling out
		profile_form = UserProfile()

	return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def remove_account(request):
	if request.method == 'POST':
		remove = request.POST.get('remove')
#		if remove:
			# DO STUFF
	else:
	#TODO(mike): Remember to remove folder
		return render(request, 'remove.html')



def settings(request):
	if request.user.is_authenticated():
		user = request.user
		profile = user.get_profile()
		profile_form = UserProfile()
		if request.method == 'POST':
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			return HttpResponseRedirect('/slowergram')
		else:
			profile_form = UserProfile();
			return render(request, 'settings.html', {'profile_form': profile_form})
	return HttpResponse(status = 404)



def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			title = request.POST.get('name')
			handle_uploaded_file(request.FILES['file'], request.user, title)
			return HttpResponseRedirect('/slowergram')
		else:
			return HttpResponse('invalid form')
	else:
		form = UploadFileForm()
	return HttpResponseRedirect('/slowergram')
