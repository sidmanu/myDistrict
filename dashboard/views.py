from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.utils.html import format_html
import sys, traceback

from dashboard.models import *

def get_sidebar_context():
    context = {}
    return context

def my_render(request, template, context):
	template = 'dashboard/' + template
	return render(request, template, context)


def index(request):
	context = get_sidebar_context()
	return my_render(request, 'index.html', context)
	
def login(request):
	context = get_sidebar_context()
	return my_render(request, 'login.html', context)
	
