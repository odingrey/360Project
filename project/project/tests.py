from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.test.client import Client
from django.utils import unittest


from form import UserRegistrationForm
from form import UserProfile
from selenium import webdriver
from pyvirtualdisplay import Display
from views import main
from views import home
from views import edit
from views import register
from views import delete_image
from views import upload_file
from views import settings
from views import remove_account

from project import helper

class FormTests(TestCase):
	def setUp(self):  #writes new user and profile to a test database
		form_data = {'username' : 'test@test.com', 'password1' : 'test', 'password2' : 'test'}
                self.user = User.objects.create_user('test@test.com', 'test@test.com', 'test')
		profile_form = UserProfile(data=form_data)
		self.failUnlessEqual(profile_form.is_valid(), True)
		profile = profile_form.save(commit=False)
		profile.user = self.user
		profile.save()
		self.userprofile = profile

	def test_registration_forms(self):  # checks for valid registration
                form_in = {'username' : 'test1@test.com', 'password1' : 'test', 'password2': 'test'}
		form = UserRegistrationForm(data=form_in)
		self.assertEqual(form.is_valid(), True) 

	def test_failed_registration_form(self):	#incorrect password
		form_in = {'username' : 'test1@test.com', 'password1' : 'test', 'password2' : 'tset'}
		form = UserRegistrationForm(data=form_in)
		self.assertEqual(form.is_valid(), False)

	def test_email_format_registration_form(self):	#username does not match email formatting
		form_in = {'username' : 'test', 'password' : 'test', 'password2' : 'test'}
		form = UserRegistrationForm(data=form_in)
		self.assertEqual(form.is_valid(), False)

	def test_user_write_to_db(self): #Ensures user was correctly written to test database
		database_found = User.objects.get(username = 'test@test.com')
		self.assertEqual(database_found == self.user, True)

	def test_user_profile(self): #Ensures profile was correctly written to the test database
		database_found = User.objects.get(username = 'test@test.com')
		self.assertEqual(database_found.userprofile == self.userprofile, True)
		


class ResolveTests(TestCase):
	#These test that the server spits out proper information when a user is logged out.
	def test_home_resolve(self):
		response = resolve('/')
		self.assertEqual(response.func, home)

	def test_main_resolve(self):
		response = resolve('/main')
		self.assertEqual(response.func, main)

        def test_main_resolve(self):
                response = resolve('/main')
                self.assertEqual(response.func, main)

        def test_edit_resolve(self):
                response = resolve('/edit/')
                self.assertEqual(response.func, edit)

        def test_register_resolve(self):
                response = resolve('/register/')
                self.assertEqual(response.func, register)

        def test_delete_image_resolve(self):
                response = resolve('/delete/')
                self.assertEqual(response.func, delete_image)

        def test_upload_resolve(self):
                response = resolve('/upload')
                self.assertEqual(response.func, upload_file)

        def test_settings_resolve(self):
                response = resolve('/settings')
                self.assertEqual(response.func, settings)

        def test_remove_account_resolve(self):
                response = resolve('/remove_account/')
                self.assertEqual(response.func, remove_account)



class StatusTests(TestCase):
	#These check that the server spits out the correct status codes when a user is logged out.
	def test_home(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)

        def test_main(self):
                response = self.client.get("/main")
                self.assertEqual(response.status_code, 302)

        def test_edit(self):
                response = self.client.get("/edit/")
                self.assertEqual(response.status_code, 302)

        def test_delete_image(self):
                response = self.client.get("/delete/")
                self.assertEqual(response.status_code, 404)

        def test_register(self):
                response = self.client.get("/register/")
                self.assertEqual(response.status_code, 200)

        def test_remove_account(self):
                response = self.client.get("/remove_account/")
                self.assertEqual(response.status_code, 200)

        def test_settings(self):
                response = self.client.get("/settings")
                self.assertEqual(response.status_code, 404)

        def test_upload_file(self):
                response = self.client.get("/upload")
                self.assertEqual(response.status_code, 302)
	
	#tests broken link when logged out
	def test_failed_request(self):
		response = self.client.get("/not_real_link")
		self.assertEqual(response.status_code, 404)

class LoginTests(TestCase):
	
	def setUp(self):	#creates user object used for the test
		self.user = User.objects.create_user('test@test.com', 'test@test.com', 'test')
	#Tests the login system
	def test_successful_login(self):
		login = self.client.login(username='test@test.com', password='test')
		self.assertEqual(login, True)

	#These test the server status codes when a user is logged in.
        def test_logged_main(self):
                self.client.login(username='test@test.com', password='test')
                response = self.client.get("/main/")
                self.assertEqual(response.status_code, 200)

        def test_logged_edit(self):
                self.client.login(username='test@test.com', password='test')
                response = self.client.get("/edit/")
                self.assertEqual(response.status_code, 302)

        def test_logged_delete_image(self):
                self.client.login(username='test@test.com', password='test')
                response = self.client.get("/delete/")
                self.assertEqual(response.status_code, 400)

        def test_logged_register(self):
                self.client.login(username='test@test.com', password='test')
                response = self.client.get("/register/")
                self.assertEqual(response.status_code, 200)

        def test_logged_remove_account(self):
                self.client.login(username='test@test.com', password='test')
                response = self.client.get("/remove_account/")
                self.assertEqual(response.status_code, 200)

        def test_logged_upload_file(self):
                self.client.login(username='test@test.com', password='test')
                response = self.client.get("/upload")
                self.assertEqual(response.status_code, 302)

	#Tests broken link when logged in
        def test_logged_failed_request(self):
                self.client.login(username='test@test.com', password='test')
                response = self.client.get("/not_real_link")
                self.assertEqual(response.status_code, 404)


	#  Tests server returns while logged in
        def test_logged_home_resolve(self):
        	login = self.client.login(username='test@test.com', password='test')
                response = resolve('/')
                self.assertEqual(response.func, home)

        def test_logged_main_resolve(self):
        	login = self.client.login(username='test@test.com', password='test')
                response = resolve('/main')
                self.assertEqual(response.func, main)

        def test_logged_main_resolve(self):
        	login = self.client.login(username='test@test.com', password='test')
                response = resolve('/main')
                self.assertEqual(response.func, main)

        def test_logged_edit_resolve(self):
        	login = self.client.login(username='test@test.com', password='test')
                response = resolve('/edit/')
                self.assertEqual(response.func, edit)

        def test_logged_register_resolve(self):
        	login = self.client.login(username='test@test.com', password='test')
                response = resolve('/register/')
                self.assertEqual(response.func, register)

        def test_logged_delete_image_resolve(self):
        	login = self.client.login(username='test@test.com', password='test')
                response = resolve('/delete/')
                self.assertEqual(response.func, delete_image)

        def test_logged_upload_resolve(self):
        	login = self.client.login(username='test@test.com', password='test')
                response = resolve('/upload')
                self.assertEqual(response.func, upload_file)

        def test_logged_settings_resolve(self):
        	login = self.client.login(username='test@test.com', password='test')
                response = resolve('/settings')
                self.assertEqual(response.func, settings)

        def test_logged_remove_account_resolve(self):
        	login = self.client.login(username='test@test.com', password='test')
                response = resolve('/remove_account/')
                self.assertEqual(response.func, remove_account)

class ExtraTests(TestCase):
	#Tests the brightness conversion between front and backend
	def test_brightness_converter(self):
		converted = helper.convert_brightness(50)
		self.assertEqual(converted, 1)

	def test_many_requests(self):
		for i in xrange(0,100000):
			response = resolve('/')
			self.assertEqual(response.func, home)
