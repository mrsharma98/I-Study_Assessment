from django.urls import path, include
from . import views

urlpatterns = [
        path('<int:pizza_id>', views.detail, name='detail'),

]
