from django.contrib import admin
from django.urls import path
from api.views import *
from webapi.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView.as_view(),name="home"),
    path('logout', LogoutView.as_view(next_page='home'), name='logout'),
    path('user-account/task-add', AddTaskViewList.as_view(),name="add-task"),
    path('user-account', TasksViewMyAccount.as_view(),name="user-account"),
    path('user-account/user-info', TasksViewInfoUser.as_view(),name="user-info"),
    path('user-account/my-tasks', TasksViewList.as_view(),name="my-tasks"),
    path('user-login', TasksViewLoginUser.as_view(),name="user-login"),
    path('user-create', TasksViewCreateUser.as_view(),name="user-create"),
    path('modify-task/<int:task_id>', modifyTaskView.as_view(),name="modify-task"),
    path('delete-task/<int:task_id>', deleteTaskView.as_view(),name="delete-task"),
    path('api/', TasksApiView.as_view()),
    path('api/<int:task_id>', TasksApiViewId.as_view()),
    path('api/changeStatus/', TaskApiChangeStatus.as_view())
]
