from django.conf.urls import url
from entries import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
	url(r'^faq/$', views.faq, name='faq'),
	url(r'^entry/(?P<entry_name_slug>[\w\-]+)/$', views.viewentry, name='viewentry'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
	url(r'^invalidlogin/$', views.invalidlogin, name='invalidlogin'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^suggestion/$', views.suggestion, name='suggestion'),
    url(r'^contact/$', views.contact, name='contact'),
	url(r'^trending/$', views.trending, name='trending'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/(?P<cat_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^addentry/$', views.addentry, name='addentry'),
	url(r'^profile/(?P<username>[\w\-]+)/$', views.userprofile, name='userprofile'),
#new down here
    #editprofile
    url(r'^profile/(?P<username>[\w\-]+)/edit/$', views.edit_profile, name='edit_profile'),
    #change password
    url(r'^profile/(?P<username>[\w\-]+)/password/$', views.change_password, name='change_password'),
]
