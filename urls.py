from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),  # ✅ shows contact form at '/'
]
