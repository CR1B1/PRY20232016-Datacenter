from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render
from django.http import HttpResponseServerError


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        user = request.user
        if user.is_authenticated:
            pass
        else:
            if request.path.startswith(reverse('admin:index')):
                return None
            if request.path == "/request-change-password/":
                return None
            if request.path != '/auth/login/':
                return HttpResponseRedirect(reverse('authentication:login'))
            
class AdminCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path == '/auth/login/':
            if request.user.is_superuser:
                request.session.flush()
                return HttpResponseRedirect(reverse('authentication:login'))


class Custom400Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 400:
            return render(request, '400.html', {'path': request.path})
        return response
    
class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            return render(request, '404.html', {'path': request.path})
        return response
    
class Custom500Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            return render(request, '500.html', {'path': request.path})
        return response

class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            response = HttpResponseServerError("Oops! Something went wrong.")
        return response