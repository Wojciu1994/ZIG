from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from myapp.forms import UserCreationForm
from django.template import RequestContext

