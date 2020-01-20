from django.urls import path,include
from . import views

urlpatterns =[
  path('employee/', views.dashboard, name = 'dashboard'),
  path('display_employee',views.display_employee,name='display_employee'),
  path('add_employee',views.add_employee,name='add_employee'),
  path('edit_employee',views.edit_employee,name='edit_employee'),
  path('delete_employee',views.delete_employee,name='delete_employee'),
]