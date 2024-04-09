
from django.urls import path
from news.views import Posts_list


urlpatterns = [
   path('', Posts_list.as_view()),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('products/', include('simpleapp.urls')),
]