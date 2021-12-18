from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "home.html"

def storepage(request):
    return render(request, "account/store.html")
