from django.contrib import admin
from django.urls import path
from api.views import home  # 👈 import kiya

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', home),  # 👈 ye line add ki
]
