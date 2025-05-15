from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Demoapp.urls')),  # add this
    path('api-auth/', include('rest_framework.urls')),  # for login on browsable API
]
