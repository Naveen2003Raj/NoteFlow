
from django.contrib import admin
from django.urls import path
from taskapp import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home'),
    path('register/',views.register,name="Register"),
    path('login/',auth.LoginView.as_view(template_name='login.html'),name="Login"),
    path('page/',views.page,name="Page"),
    path('notes/', views.notes, name='notes'),
    path('edit-note/<int:id>/', views.edit_note, name='edit_note'),
    path('delete-note/<int:id>/', views.delete_note, name='delete_note'),
    path('todo/', views.todo, name='todo'),
path('edit-todo/<int:id>/', views.edit_todo, name='edit_todo'),
path('delete-todo/<int:id>/', views.delete_todo, name='delete_todo'),
path('logout/', views.user_logout, name='logout'),
]

