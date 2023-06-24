from django.urls import path
from . import views
from django.contrib.auth import views as authviews


app_name = 'about'
urlpatterns = [
    path('', views.index, name='index'),
    path('kinds/', views.kinds, name='kinds'),
    path('new_cat/', views.new_cat, name='new_cat'),
    path('edit_cat/<int:cat_id>/', views.edit_cat, name='edit_cat'),
    path('registration/', views.registration, name='reg'),
    path('profile/', views.profile, name='profile'),
    path('auth_user/', views.CustomLoginView.as_view(), name='userauth'),
    path('log_out/', authviews.LogoutView.as_view(), name='log_out'),
    path('cat_detail/<int:cat_id>/', views.card_of_cat,name='cat_detail')
]