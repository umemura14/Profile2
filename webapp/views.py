from re import template
from django import views
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = ""
        return ctxt


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["time"] = "2021.10/01"
        ctxt["skills"] = [" Java",
                          "HTML",
                          "CSS",
                          "Python",
                          "Git",
                          "Linux"
                          ]
        return ctxt
