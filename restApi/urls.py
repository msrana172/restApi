from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hrm.api import UserList, UserDetail
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/users_list/$', UserList.as_view(), name='user_list'),
    url(r'^api/users_list/(?P<employee_id>\d+)/$', UserDetail.as_view(), name='user_list'),
]
