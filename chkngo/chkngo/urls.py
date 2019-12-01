"""chkngo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', views.RestoList, name = "RestoList"),
    path('restaurants/<RestoID>/', views.RestoView, name = "RestoView"),
    path('restaurants/<RestoID>/manage',views.RestaurantManagement, name = 'RestoManage'),
    path('restaurants/<RestoID>/ReviewUpload/', views.ReviewUpload, name = 'ReviewUpload'),
    path('restaurants/<RestoID>/SeeWaitList/', views.SeeWaitlist, name = 'SeeWaitList'),
    path('restaurants/<RestoID>/DeleteEntry/<first_name>/<last_name>/<id>/', views.DeleteEntry, name ="DeleteEntry"),
    path('restaurants/<RestoID>/SeatEntry/<id>', views.SeatEntry, name = "SeatEntry"),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'),name = 'Logout'),
    path('register/', views.Register, name = 'Register'),
    path('register/make_category', views.MakeCategory, name = "MakeCategory"),
    
    # path('', views.home, name = 'Home'),
]