from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.hospital_home,name='home'),
    path('pform/',views.patient_signup, name='pform'),
    path('dform/',views.doctor_signup,name='dform'),
    path('plogin/',views.patient_login,name='plogin'),
    path('dlogin/',views.doctor_login,name='dlogin'),
    path('logout/',views.logout_view,name='logout'),
    path('pdash/',views.patient_dashboard,name='pdash'),
    path('ddash/',views.doctor_dashboard,name='ddash'),
    path('blog-home/',views.blog_home_page, name= 'blog-home'),
    path('blog-posts/',views.published_posts, name= 'blog-posts'),
    path('blog-form/',views.blog_post_form, name= 'blog-form'),
    path('published/<int:pk>/',views.publish_draft_post, name= 'published'),
    path('dp-posts/',views.patient_post_view,name='dp-posts'),
    path('<int:pk>/',views.delete_posts, name= 'delete')

]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

