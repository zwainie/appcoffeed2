from django.shortcuts import render

	

# Create your views here.
from django.views.generic.base import TemplateView

class LandingView(TemplateView):
    template_name = "base/index.html"