from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'polls/login.html'}),
]