from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns=[
  url('signup/', views.signup, name='signup'),
  url('account/', include('django.contrib.auth.urls')),
  url('', views.index, name='index'),
  url('profile/<username>', views.profile, name='profile'),
  url('profile_update/<username>/', views.user_profile, name='user_profile'),
]
