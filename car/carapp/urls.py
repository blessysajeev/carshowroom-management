from django.urls import path, include
from carapp import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('packages/',views.packages,name='packages'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    # path('home/',views.home,name='home'),
    path('testdrive/',views.testdrive,name='testdrive'),
    path('cars/',views.cars,name='cars'),
    path('testview/' , views.testview,name='testview'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('staffhome',views.staffhome,name='staffhome'),
    path('stafflogin',views.stafflogin,name="stafflogin"),
    path('staffregister',views.staffregister,name="staffregister"),
    path('visit',views.visit,name="visit"),
    path('job',views.job,name="job"),
    # path('book/<int:id>',views.book,name='book'),


    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change_password/', views.change_password, name='change_password'),

]