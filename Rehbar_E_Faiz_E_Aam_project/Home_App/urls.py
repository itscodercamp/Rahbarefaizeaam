
from django.urls import path
from . import views

urlpatterns = [

    # Main Stream Urls Routings 
    path('', views.Home_Page, name='home'),
    path('About_Us/', views.About_Page, name='about'),
    path('Gallery/', views.Gallery_Page, name='gallery'),

    path('Home/', views.Home_Page, name='home'),
    path('Services/', views.Services, name='Services'),

    path('Donate/', views.Donate_Page, name='donate'),
    path('Blog/', views.Blog_Page, name='blog'),
    path('blog/<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),

    path('Contact_Us/', views.Contact_Page, name='contact'),

    path('Demo/', views.Demo, name='demo'),

    # ajax call to forms url routing here
    path('Become_volunteer/', views.Become_volunteer, name='Become_volunteer'),
    path('Contact us Form/', views.ContactUsForm, name='ContactUsForm'),
    path('donate_form_details/', views.donate_form_details, name='donate_form_details'),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
