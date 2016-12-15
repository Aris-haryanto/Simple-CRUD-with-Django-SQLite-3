from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'firstapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^savedata/$', views.crud.savedata, name='savedata'),
    url(r'^updatedata/$', views.crud.updatedata, name='updatedata'),
    url(r'^([0-9]+)/editdata/$', views.crud.editdata, name='editdata'),
    url(r'^([0-9]+)/deletedata/$', views.crud.deletedata, name='deletedata'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
