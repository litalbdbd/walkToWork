from django.urls import path, include

from . import views

app_name = "core"

urlpatterns = [
    path('', views.display_regions, name="home_page"),
    # path('regions-new/', views.DisplayRegions.as_view(), name="home_page_new"),
    path('cities/<str:name>/', views.display_cities, name="cities_page"),
    path('employees/<str:name>/', views.display_emloyees, name="employees_page"),
    # path('user_form/', views.display_user_form, name="user_form"),
    path('user_form/', views.EmployeeUpdateView.as_view(), name="user_form"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('logout/', views.logout)

]
