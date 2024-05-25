from django.urls import path
from .views import register, EmailLoginView, EmailLogoutView, authenticated, home, order_details, order_status

app_name = 'gestion'

urlpatterns = [
    path('', home, name='home'),
    path('login/', EmailLoginView.as_view(), name='login'),
    path('logout/', EmailLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('authenticated/', authenticated, name='authenticated'),
    path('detail/<int:pedido_id>', order_details, name='detail'),
    path('status/<int:pedido_id>', order_status, name='status')
]
