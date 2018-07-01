"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from polls import views
# import form_user.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  url(r'^form_user_save/$', views.form_user_save),
    url(r'^form_top/$', views.form_top, name='top'),
    url(r'^form_user_login/$', views.FormUserLogin.as_view(), name='user_login'),
  # views_form_user_loginというモジュールはありません
    url(r'^form_time_login/$', views.form_time_login_function, name='time_login'),
    url(r'^form_user/$', views.FormUser.as_view(), name='form_user'),
    url(r'^form_secret/$', views.FormSecret.as_view(), name='form_secret'),
    url(r'^del-user/$', views.del_user, name='del_user'),
    url(r'^del-demo-user/$', views.del_demo_user, name='del_demo_user'),
    url(r'^form_time/$', views.form_time, name='form_time'),
  url(r'^add_syain/$', views.form_save),
  url(r'^search/$', views.search),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
