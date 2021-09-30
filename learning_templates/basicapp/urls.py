from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from basicapp import views

# TEMPLATE TAGGING
app_name = 'basicapp'

urlpatterns = [
	path('relative/', views.relative, name='relative'),
	path('other/', views.other, name='other'),
	# if it base/basicapp/relative or base/basicapp/other display the template views
]