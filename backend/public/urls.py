
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from public import views

app_name = 'public'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('incidences/', views.IncidenceView.as_view(), name='incidences'),
    path('register/incidence/', views.RegisterIncidenceView.as_view(), name='register-incidence'),
    path('register/subject/incidence/', views.SubjectIncidenceView.as_view(), name='subject-incidence'),
    path('access-requests/', views.AccessRequests.as_view(), name='access-requests'),
    path('access-authorization/<int:pk>/', views.AccessAuthorization.as_view(), name='access-authorization'),
    path('configuration/', views.ConfigurationView.as_view(), name='configuration_user'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('delete-incidence/<int:pk>/', views.DeleteIncidence.as_view(), name='delete-incidence'),
    path('request-change-password/', views.ChangePasswordRequest.as_view(), name='change-password-request'),
    path('change-logo/', views.ChangeLogo.as_view(), name="change-logo"),
    path('users/', views.MyUsersView.as_view(), name='my-users')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)