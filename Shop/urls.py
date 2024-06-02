from django.urls import path
from . import views
 
urlpatterns=[
  path('',views.Home,name='home'),
  path('register',views.Register,name='register'),
  path('login',views.LoginPage,name="login"),
  path('logout',views.LogoutPage,name="logout"),
  path('collections',views.Collections,name='collections'),
  path('collections/<str:name>',views.collectionsView,name='collections'),
  path('collections/<str:cname>/<str:pname>',views.productDetails,name="productDetails"),
  path('addtocart',views.add_to_cart,name='addtocart'),
 ]