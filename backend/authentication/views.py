from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth import authenticate, login
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .forms import LoginForm, SignUpForm, UpdateForm, ChangePasswordForm
from authentication.models import User

class LoginView(View):
    template_name = 'auth/login.html'
    
    def get(self,request,*args, **kwargs):
        form = LoginForm()
        msg = request.GET.get('success', '')
        return render(request, self.template_name, {"form": form, "msg": msg})
    
    def post(self,request,*args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if request.session.test_cookie_worked():
                    request.session.delete_test_cookie()
                request.session.set_test_cookie()
                return HttpResponseRedirect(reverse_lazy('public:index'))
            else:
                message = 'Se ha ingresado un usuario o contraseña incorrectos'
        else:
            message = 'Error de la plataforma'
        return render(request, self.template_name, {"form": form, "message": message})
        
class RegisterView(View):
    message = ''
    success = False
    template_name = 'auth/register.html'
    
    def get(self,request,*args,**kwargs):
        form = SignUpForm()
        if self.request.user.role == 255:
            form.fields.pop("user_area")
        return render(request, self.template_name, {"form": form, "msg": self.message, "success": self.success})
    
    def post(self,request,*args,**kwargs):
        form = SignUpForm(request.POST)
        if self.request.user.role == 255:
            form.fields.pop("user_area")
        try:
            if form.is_valid():
                instance = form.save()
                instance.administrator = self.request.user
                if self.request.user.role == 255:
                    instance.user_area = self.request.user.user_area
                    instance.administrator = self.request.user.administrator
                instance.save()
                self.message = f'Usuario creado {instance.username}'
                self.success = True
                return render(request, self.template_name, {"form": form, "message": self.message, "success": self.success})
            else:
                self.message = 'Error en el formulario'
        except Exception as e:
            self.message = 'Error en el formulario'
        return render(request, self.template_name, {"form": form, "message": self.message, "success": self.success})

class UpdateView(View):
    message = ''
    error = None
    success = None
    
    def post(self,request,*args,**kwargs):
        form = UpdateForm(request.POST, instance=self.request.user)
        try:
            if form.is_valid():
                form.save()
                self.message = 'Se actualizo tus datos de usuario'
                return HttpResponseRedirect(reverse('public:configuration_user') + f'?message={self.message}')
            else:
                self.message = 'El formato ingresado no es el correcto'
        except Exception as e:
            self.message = 'Error en la actualización de tus datos'
        return HttpResponseRedirect(reverse('public:configuration_user') + f'?error={self.message}')
    
class ChangePassword(View):
    template_name = "auth/change_password.html"
    
    def get(self, request, *args, **kwargs):
        form = ChangePasswordForm()
        user = get_object_or_404(User, pk=kwargs['pk'])
        return render(request=request, template_name=self.template_name, context={"form":form, "kwargs": kwargs, "user": user})
        
    def post(self, request, *args, **kwargs):
        new_password = request.POST.get("password1")
        user = get_object_or_404(User, pk=kwargs['pk'])
        user.set_password(new_password)
        user.change_password = False
        user.save()
        return HttpResponseRedirect(reverse_lazy("public:my-users"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("authentication:login"))