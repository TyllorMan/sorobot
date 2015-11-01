from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from models import Robot, Usuario
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
#from django.contrib.auth.models import User

# Create your views here.

class InsereRoboView(DetailView):
	model = Robot
	template_name = 'index.html'

class IndexView(TemplateView):
    template_name = 'home.html'

class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['nome','email','password']
    template_name = 'usuario_form.html'

def login_user(request):
	if not request.user.is_authenticated():
	    state = "Please log in below..."
	    username = password = ''
	    if request.POST :
	        username = request.POST.get('username')
	        password = request.POST.get('password')

	        user = authenticate(username=username, password=password)
	        if user is not None:
	            if user.is_active:
	                login(request, user)
	                return render_to_response('logado.html',{'usuario':request.user})
	            else:
	                state = "Your account is not active, please contact the site admin."
	        else:
	            state = "Your username and/or password were incorrect."

	    return render_to_response('auth.html',{'state':state, 'username': username})
	else:
	    return render_to_response('home.html',{'usuario':request.user})

def logout_user(request):
	texto = 'Deslogou com gosto!'
	logout(request)
	return render_to_response('logout.html',{'texto':texto})