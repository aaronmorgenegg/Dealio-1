from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from dealioApp import views as core_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^restaurants$', views.restaurants, name='restaurants'),
    url(r'^promotions/(?P<restaurant_id>\d+)/$', views.promotions, name='promotions'),#this uses a named group for regex
    url(r'^addPromo/(?P<restaurant_id>\d+)/$', views.add_promo, name='addPromo'),
    url(r'^promotion_confirm_delete/(?P<pk>\d+)/$', views.delete_promo.as_view(), name='promotion-delete'),
    url(r'^restaurant/add/$', views.RestaurantCreate.as_view(), name='restaurant-add'),
    url(r'^restaurant/(?P<pk>\d+)/$', views.RestaurantUpdate.as_view(), name='restaurant-update'),
    url(r'^ownerSignUp$', views.ownerSignUp, name ='ownerSignUp'),
    url(r'^ownerLogin$', auth_views.login, {'template_name': 'dealioApp\ownerLogin.html'}, name ='ownerLogin'),
    url(r'^ownerLogout/$', auth_views.logout, {'template_name': 'dealioApp\ownerLogout.html', 'next_page': '/'}, name='logout'),
    url(r'^placefinder$', views.placefinder, name='placefinder'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]
