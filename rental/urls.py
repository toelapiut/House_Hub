from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^landlord/profile/$',views.landlord_prof,name="landlord_profile"),
    url(r'^ajax/landlord/tenant/',views.ajax_choice,name="ajax-resp"),
    url(r'^house/image/(\d+)/$',views.add_house,name="image"),
    url( r'^like/(\d+)', views.like, name="liker"),
    url(r'^edit/profile/$',views.update_landlord_profile,name="edit"),
    url(r'^images/$',views.timeline,name="timeline"),
        ]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
