from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import *
urlpatterns =[
     path('',index, name='home'),
     path('news', news, name='news'),
     path('category/<int:category_id>/', get_category),
     path('news/<int:news_id>/', view_news, name='view_news'),
     path('news/add_news/', add_news, name='add_news'),
     path('login/', login_user, name='login'),
     path('logout/', logout_user, name='logout'),
     path('register/', register_user, name='register'),
    path('reg',registr, name='registr'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
     urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
