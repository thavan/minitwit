from django.urls import include, path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('dashboard/<int:page>/', views.dashboard, name='dashboard'),
	path('dashboard/users/<str:user>/', views.user_dashboard, name='user_dashboard'),
	path('follow/<str:user_id>/', views.follow, name='follow'),
	path('profile/<str:pk>/', views.ProfileUpdate.as_view(), name='profile')
]