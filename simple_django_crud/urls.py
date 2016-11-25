from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from applications.crud.views import index, car_detail, add_car, delete_car

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^car/(?P<pk>\d+)/$', car_detail, name='car_detail'),
    url(r'^add_car/$', add_car, name='add_car'),
    url(r'^delete_car/(?P<pk>\d+)/$', delete_car, name='delete_car'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
