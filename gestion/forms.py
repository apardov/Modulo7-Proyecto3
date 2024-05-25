from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import ModelForm
from .models import CustomEmailUser, Pedido, DetallePedido


# definicion de formularios para creacion de usuarios y modificacion de estos
# usando los predefinidos que Django provee
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomEmailUser
        fields = ('email', 'rut', 'nombre_completo')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomEmailUser
        fields = ('email', 'rut', 'nombre_completo')


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class DetallePedidoForm(ModelForm):
    class Meta:
        model = DetallePedido
        fields = '__all__'


class ChangeStatusForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado']
