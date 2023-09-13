### project urls


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #   faq app
    path('faq/', include('faq.urls', namespace='faq')),
    #   index of site - no page so we send to faq home
    path('', include('faq.urls', namespace='project_home')),
]
