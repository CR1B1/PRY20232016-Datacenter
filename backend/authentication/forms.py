from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type":"text", 
                "class":"form-control is-valid",
                "id":"validationServer01",
                "placeholder": "Correo",
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombres",
                "class": "form-control"
            }
        ), label='Nombres')
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Apellidos",
                "class": "form-control"
            }
        ), label='Apellidos')
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ), label='Nombre de usuario')
    
    dni = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "DNI",
                "class": "form-control"
            }
        ), label='DNI')
    
    
    role = forms.ChoiceField(
        choices=[(512,'Administrador'),(255, 'Ejecutivo'), (1, 'Empleado')],
        widget = forms.Select(attrs={
                "placeholder": "Role",
                "class": "form-select form-select-sm mb-3 input-box",
            }, choices=[(512,'Administrador'),(255, 'Ejecutivo'), (1, 'Empleado')]),
        label="Rol"
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control",
                "name": "Contrasena-1"
            }
        ), label="Contraseña")
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmación de la contraseña",
                "class": "form-control"
            }
        ), label="Confirmacion de contraseña")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0', placeholder="Primer nombre"),
                Column('last_name', css_class='form-group col-md-4 mb-0', placeholder="Segundo nombre"),
                Column('dni', css_class='form-group col-md-2 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('password1', css_class='form-group col-md-4 mb-0'),
                Column('password2', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('role', css_class='form-group col-md-4 mb-0'),
                Column('user_area', css_class='form-group col-md-4 mb-0'),
                Column('username', css_class='form-group col-md-4 mb-0', placeholder="Nombre de usuario"),
                
                css_class='form-row'
            ),
            Submit('save', 'Crear usuario', css_class='form-group col mb-0'),
        )
        
        
        
    class Meta:
        model = User
        fields = ( 'email', 'first_name','last_name','username', 'role', 'dni', 'password1', 'password2', 'user_area')
        
        
class UpdateForm(forms.ModelForm):  
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-control"
            }
        ), required=False, label="Primer Nombre")
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "form-control"
            }
        ), required=False, label="Segundo nombre")
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ), required=False, label="Nombre de usuario")
    
    dni = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "DNI",
                "class": "form-control"
            }
        ), required=False, label='DNI')

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'dni')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('username', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                Column('dni', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )
        self.helper.form_tag = False
        
        
class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type":"text", 
                "class":"form-control is-valid",
                "id":"validationServer01",
                "placeholder": "Correo",
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        ))

class ChangePasswordForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control",
                "name": "Contrasena-1"
            }
        ), label="Contrasena")
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirma tu constraseña",
                "class": "form-control"
            }
        ), label="Confirmacion de contrasena")
    
    class Meta:
        model = User
        fields = ( 'password1', 'password2' )