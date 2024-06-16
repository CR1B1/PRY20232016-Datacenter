# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include,re_path  # add this
from django.conf import settings
from django.conf.urls.static import static
from core.views import admin_logout


urlpatterns = [
   path("admin/logout/", admin_logout, name='logout'), # Overwrite Logout admin view
   re_path(r'^admin/', (admin.site.urls)),
   path("auth/", include("authentication.urls", 'authentication')), # Auth routes - login / register
   path("", include("public.urls", 'public')),            # Public View
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)