from django.contrib import admin
from django.urls import path, include
from core import views as cv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cv.homepage, name="home"),
    path('contact/', cv.contactpage, name="contact"),
    path('service/', include('service.urls')),
    path('education/', include('education.urls'))
]
