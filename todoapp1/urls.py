from django.urls import path
from . import views
urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('completed/<int:pk>',views.completed,name='completed'),
    path('uncompleted/<int:pk>',views.uncompleted,name='uncompleted'),
    path('editTask/<int:pk>',views.editTask,name='editTask'),
    path('deleteTask/<int:pk>',views.deleteTask,name='deleteTask'),

]