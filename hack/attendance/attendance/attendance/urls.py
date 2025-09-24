"""
URL configuration for attendance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from student import views as student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_views.signup_view, name='root_signup'),
    path("", include("student.urls")),
    # path("student/", include("student.urls")),  # Add student prefix
    path("faculty/", include("faculty.urls")),
    path("analytics/", include("faculty.urls")),  # Alias for analytics
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
