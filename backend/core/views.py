from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

def handler400(request, *args, **argv):
    return render(request, '400.html', status=400)

def admin_logout(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("admin:login"))