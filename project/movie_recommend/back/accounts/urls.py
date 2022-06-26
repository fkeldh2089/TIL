from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile, name='profile'),
    path('why/<int:user_pk>/follow/', views.follow, name='follow'),
    path('update/', views.update, name='update'),

]
