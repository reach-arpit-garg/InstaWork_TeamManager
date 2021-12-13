from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member/<uuid:pk>', views.edit_member, name='member_edit'),
    path('addMember/', views.add_member, name='member_add'),
]
