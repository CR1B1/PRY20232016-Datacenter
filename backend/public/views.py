import datetime
from public.models import AccessRequest, Incidence, Subject
import public.forms as forms 
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views import View
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db import connection
from authentication.forms import UpdateForm
from authentication.models import User
from authentication.filters import UserFilter
from public.queries import sql_graph_priority, sql_graph_solved, sql_incidences_per_user
from public.filters import DashboardFilter, IncidenceFilter

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['template_name'] = self.check_role()
        else:
            context['template_name'] = self.template_name
        return context
    
    def check_role(self):
        if self.request.user.role == 512:
            return 'accounts/administrator.html'
        if self.request.user.role == 255:
            return 'accounts/manager.html'
        if self.request.user.role == 1:
            return 'accounts/employee.html'
        return self.template_name
    
    def get(self,request,*args, **kwargs): 
        if self.request.user.role == 512 and self.request.user.is_superuser == False:
            notification_password = User.objects.filter(administrator=self.request.user, showed_password_change_request=True).count()
            template = self.get_context_data().get('template_name', self.template_name)
            return render(request, template, context={"notifications": notification_password})
        template = self.get_context_data().get('template_name', self.template_name)
        return render(request, template)
    
class SubjectIncidenceView(View, LoginRequiredMixin):
    queryset = Subject.objects.all()
    form_class = forms.SubjectForm
    template_name = 'forms/subject.html'
    message = ''
    errors = ''
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        incidences = None
        return render(request, self.template_name, {'form': form, 'message': self.message, 'errors': self.errors, 'incidences': incidences})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            self.message = 'Subject Incidence Create'
            return HttpResponseRedirect(reverse_lazy('public:register-incidence'))
        else:
            self.message = 'Error to create subject incidence'
            self.errors = form.errors
            return HttpResponseRedirect(reverse_lazy('public:subject-incidence'))
    
class RegisterIncidenceView(View, LoginRequiredMixin):
    queryset = Incidence.objects.all()
    form_class = forms.IncidenceForm
    template_name = 'forms/incidence.html'
    message = ''
    errors = ''
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        incidences = None
        return render(request, self.template_name, {'form': form, 'message': self.message, 'errors': self.errors, 'incidences': incidences})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form = form.save()
            form.user = self.request.user
            form.save()
            self.message = 'Incidencia creada'
        else:
            self.message = 'Error al crear la incidencia'
            self.errors = form.errors
        return HttpResponseRedirect(reverse_lazy('public:incidences'))
    
class IncidenceView(ListView, View, LoginRequiredMixin):
    queryset = Incidence.objects.all()
    template_name = 'lists/incidences.html'
    paginate_by = 5
    
    def get(self, request, *args, **kwargs):
        queryset = Incidence.objects.all()
        user = self.request.user
        if self.request.user.user_area:
            area = self.request.user.user_area.area_name
        else:
            area = None
        queryset = queryset if user.role == 512 else queryset.filter(user__user_area__area_name=area) if user.role == 255 else queryset.filter(user=self.request.user)
        f = IncidenceFilter(request.GET, queryset=queryset.order_by('-id'))
        paginator = Paginator(f.qs, self.paginate_by)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj, 'filter':f})  
    
class ConfigurationView(View):
    template_name = 'accounts/configuration.html'
    
    def get(self, request, *args, **kwargs):
        user = self.request.user
        message = self.request.GET.get("message", None)
        error = self.request.GET.get("error", None)
        form = UpdateForm(instance=user)
        if user.role == 512:
            image_form = forms.LogoForm(instance=user)
        else:
            image_form = None
        return render(request, self.template_name, {"form": form, "image_form": image_form, "message": message, "error": error})
    
class DashboardView(View):
    template_name = 'dashboard/charts.html'
    queryset = Incidence.objects.all()
    
    def get(self, request, *args, **kwargs):
        if self.request.user.role > 1 or self.request.user.authorization == 2:
            _filter = DashboardFilter()
            if self.request.user.role == 512 or self.request.user.is_superuser:
                _id = self.request.GET.get("user_area", None)
            else:
                if self.request.user.user_area:
                    _id = self.request.user.user_area.pk
                else:
                    _id = 0
            priority_data = self.__get_priority_data(_id)
            solved_data = self.__get_solved_data(_id)
            incidences_per_user = self.__get_total_incidences(_id)
            return render(request=request,template_name=self.template_name, context={"priority_data":priority_data, "solved_data": solved_data, "incidences_per_user": incidences_per_user, "filter": _filter})
        else:
            template_name = 'authorization_denied.html'
            return render(request=request,template_name=template_name)
        
        
    def __get_priority_data(self, _id:int):
        with connection.cursor() as cursor:
            cursor.execute(sql_graph_priority(_id))
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        
    def __get_solved_data(self, _id:int):
        with connection.cursor() as cursor:
            cursor.execute(sql_graph_solved(_id))
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        
    def __get_total_incidences(self, _id:int):
        with connection.cursor() as cursor:
            cursor.execute(sql_incidences_per_user(_id))
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        
class MyUsersView(View):
    queryset = User.objects.all()
    pagination = 5
    
    def get(self, request, *args, **kwargs):
        user = self.request.user
        page_number = request.GET.get("page")
        if user.role == 512 or user.is_superuser:
            queryset = self.queryset
            template_name = 'lists/users.html'
        elif user.role == 255 or user.authorization == 2:
            queryset = self.queryset.filter(user_area=user.user_area)
            template_name = 'lists/users.html'
        else:
            template_name = 'authorization_denied.html'
            return render(request=request,template_name=template_name)
        update = self.queryset.filter(showed_password_change_request=True).update(showed_password_change_request=False)
        f = UserFilter(request.GET, queryset=queryset.filter(is_superuser=False))
        paginator = Paginator(f.qs, self.pagination)   
        page_obj = paginator.get_page(page_number)
        return render(request=request,template_name=template_name, context={'page_obj': page_obj, 'filter':f})
    

class AccessRequests(View):
    template_view = 'requests/requests_list.html'
    queryset = AccessRequest.objects.all()
    pagination = 25
    
    def get(self, request, *args, **kwargs):
        user = self.request.user
        page_number = request.GET.get("page")
        if user.role == 512 or user.is_superuser:
            update = self.queryset.filter(showed=False).update(showed=True)
            queryset = self.queryset.filter(approver_user=self.request.user)
            template_name = 'lists/users.html'
        else:
            template_name = 'authorization_denied.html'
            return render(request=request,template_name=template_name)
        paginator = Paginator(queryset, self.pagination)   
        page_obj = paginator.get_page(page_number)
        return render(request=request,template_name=self.template_view, context={'page_obj': page_obj})
    
    def post(self, request, *args, **kwargs):
        try:
            objects = AccessRequest.objects.get(request_user=self.request.user)
            if self.request.user.authorization < 2:
                user = User.objects.filter(pk=self.request.user.pk).update(
                    authorization = 1
                )
            else:
                pass
        except AccessRequest.DoesNotExist:
            _object = AccessRequest.objects.create(
                request_user = self.request.user,
                approver_user = self.request.user.administrator
                )
            _object.save()
            user = User.objects.filter(pk=self.request.user.pk).update(
                authorization = 1
            )
        return HttpResponseRedirect(reverse_lazy("public:access-requests"))
    
class AccessAuthorization(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=int(pk)).update(
                authorization = 2
        )
        _object = AccessRequest.objects.get(request_user__pk=pk)
        _object.approval_date = datetime.datetime.now()
        _object.approval = True
        _object.save()
        return HttpResponseRedirect(reverse_lazy("public:access-requests"))
    
class DeleteIncidence(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        incidence = get_object_or_404(Incidence, pk=pk)
        incidence.delete()
        return HttpResponseRedirect(reverse_lazy("public:incidences"))
    
    
class ChangePasswordRequest(View):
    template_name = 'authorization_required.html'
    
    def get(self, request, *args, **kwargs):
        form = forms.UserChangePasswordForm()
        return render(request=request, template_name=self.template_name, context={"form": form})
    
    def post(self, request, *args, **kwargs):
        form = forms.UserChangePasswordForm()
        try:
            email = request.POST.get('email').lower()
            user = get_object_or_404(User, email=email)
            user.change_password = True
            user.showed_password_change_request = True
            user.save()
            message = "Se envio la solicitud al administrador"
            success = True
        except Exception as e:
            message = "El usuario no existe"
            success = False
        return render(request=request, template_name=self.template_name, context={"form": form, "message":message, "success":success})
    
    
class ChangeLogo(View):
    def post(self, request, *args, **kwargs):
        image_form = forms.LogoForm(data=request.POST, instance=request.user, files=request.FILES)
        if image_form.is_valid():
            image_form.save()
        return HttpResponseRedirect(reverse_lazy("public:configuration_user"))