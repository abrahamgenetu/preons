"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path

from main.views import TutorCreateView, CategoryCreateView, SeriesCreateView
from . import views

app_name = "main"
urlpatterns = [

    path("", views.homepage, name="homepage"),
    path('tutor_create/', TutorCreateView.as_view(), name='Tutor-create'),
    path('series_create/', SeriesCreateView.as_view(), name='Series-create'),
    path('category_create/', CategoryCreateView.as_view(), name='Category-create'),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("register/<single_slug>", views.single_slug, name="courses"),
    path("logout/", views.logout_request, name="logout"),
    path("course/<single_slug>", views.single_slug, name="course"),
    path("courses/", views.courses_request, name="courses"),
    path("courses/<single_slug>", views.single_slug, name="courses"),
    path("about/", views.about_request, name="about"),
    path("about/<single_slug>", views.single_slug, name="courses"),
    path("login/", views.login_request, name="login"),
    path("login/<single_slug>", views.single_slug, name="login"),
    path("contact/", views.contact_request, name="login"),
    path("about/<single_slug>", views.single_slug, name="contact"),
    path("blog/", views.blog_request, name="blog"),
    path("blog/<single_slug>", views.single_slug, name="news"),
    path("<single_slug>", views.single_slug, name="single_slug")
]
