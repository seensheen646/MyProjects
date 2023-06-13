
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('booking',views.booking,name="booking"),
    path('feature',views.feature,name="feature"),
    path('menu',views.menu,name="menu"),
    path('team',views.team,name="team"),
    path('single',views.single,name="single"),
    path('contactus',views.contact_us,name="contact_us"),

]
