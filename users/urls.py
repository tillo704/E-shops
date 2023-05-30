from .views import SignupView,ProfileView,UpdateProfileView,AddRemuveSavedView,SevedView,RecentlyViwedView
from django.urls import path

app_name= 'users'
urlpatterns = [
    path('signup/',SignupView.as_view(), name='signup'),
    path('profile/<str:username>/',ProfileView.as_view(), name='profile'),
    path('update/',UpdateProfileView.as_view(), name='update'),
    path('addremoveseved/<int:product_id>',AddRemuveSavedView.as_view(),name='addremovesaved'),
    path('savads/',SevedView.as_view(),name='saveds'),
    path('recently-viewed/',RecentlyViwedView.as_view(),name='recently_viewed')

    ]