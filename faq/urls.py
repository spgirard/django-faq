### faq app urls


from django.urls import path
from . import views

app_name="faq"

urlpatterns=[
    path('', views.list, name="faq"),
]