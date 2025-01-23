from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

from accounts.views import signup, signin, user_profile, signout
from core.views import status

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/status/')),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('profile/', user_profile, name='profile'),
    path('status/', status, name='status'),
]
