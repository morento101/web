from django.conf.urls import url
from . import views
from .views import question, popular, new_ques


urlpatterns = [
	url(r'^$', new_ques),
	url(r'^question/(?P<id>[0-9]+)/', question),
	url(r'popular/', popular),
]
