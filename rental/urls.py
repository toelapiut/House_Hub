from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$',views.choice,name='choice'),
    url(r'^home/$',views.index,name='home'),
    url(r'^landlord/profile/$',views.landlord_prof,name="landlord_profile"),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
