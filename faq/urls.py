### faq app urls


from django.urls import path
from . import views

app_name="faq"

urlpatterns=[
    #   pass a category in
    path('<slug:category_slug>/', views.list, name="questions_by_category"),
    #   pass nothing
    path('', views.list, name="faq"),
]