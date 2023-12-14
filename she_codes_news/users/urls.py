from django.urls import path
from .views import CreateAccountView,UserView
app_name ='users'
urlpatterns = [    
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/account_view/', UserView.as_view(), name='accountView'),
    ]
    