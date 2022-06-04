from django.urls import path, include

from . import views


urlpatterns = [
	path('accounts/', include('allauth.urls')),
	path('', views.AnimesView.as_view(), name='home'),
	path("filter/", views.FilterAnimesView.as_view(), name='filter'),
	path("search/", views.Search.as_view(), name='search'),
	path('<slug:slug>/', views.AnimeDetailView.as_view(),name='anime_detail'),

]