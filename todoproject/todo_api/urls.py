# from django.conf.urls import url
from django.urls import path
from knox import views as knox_views
from .views import *

urlpatterns = [
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', LoginApiView.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('all_tasks', TodoListApiView.as_view()),
    path('all_categories', CategoryListApiView.as_view()),
    path('category_tasks/<str:pk>', CategoryTasksApiView.as_view()),
    path('category_create', CreateCategoryApiView.as_view()),
    path('category_edit/<str:pk>', EditCategoryApiView.as_view()),
    path('category_delete/<str:pk>', DeleteCategoryApiView.as_view()),
    path('task_details/<str:pk>', TodoTaskDetailsApiView.as_view()),
    path('task_create', CreateTodoTaskApiView.as_view()),
    path('task_edit/<str:pk>', EditTodoTaskApiView.as_view()),
    path('task_delete/<str:pk>', DeleteTaskApiView.as_view()),
]
