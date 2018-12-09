from django import forms

#Tupla de Regiones
regiones=(('1','Arica y Parinacota'),('2','Tarapacá'),('3','Antofagasta'),
    ('4','Atacama',),
    ('5','Coquimbo'),
    ('6','Valparaiso'),
    ('7','Metropolitana de Santiago'),
    ('8',"Libertador General Bernardo O'Higgins"),
    ('9','Maule'),
    ('10','Biobío'),
    ('11','La Araucanía'),
    ('12','Los Ríos'),
    ('13','Los Lagos'),
    ('14','Aisén del General Carlos Ibáñez del Campo'),
    ('15','Magallanes y de la Antártica Chilena'),
    ('16','Ñuble'),)

class RegistrarPersonaForm(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellidoPersona=forms.CharField(widget=forms.TextInput(),label="Apellido")
    mailPersona=forms.EmailField(label="Email: ")
    fechaNacimiento=forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2001)),label="Fecha de Nacimiento")
    numeroFono=forms.CharField(widget=forms.TextInput(),label="Telefono")
    regionPersona=forms.ChoiceField(choices=(regiones),label="Región")
    ciudadPersona=forms.ChoiceField(choices=(('1', 'Unknown',),),label="Ciudad")
    viviendaPersona=forms.ChoiceField(choices=(('1', 'Casa con Patio Grande'),('2', 'Casa con Patio Pequeño'),('3', 'Casa sin Patio'),('4', 'Departamento')),label="Tipo Vivienda")

# Formulario para Registro de una Persona DESDE EL ADMIN
class RegistrarAdminForm(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellidoPersona=forms.CharField(widget=forms.TextInput(),label="Apellido")
    mailPersona=forms.EmailField(label="Email: ")
    fechaNacimiento=forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2001)),label="Fecha de Nacimiento")
    numeroFono=forms.CharField(widget=forms.TextInput(),label="Telefono")
    #----------- CAMBIAR CAMPOS
    regionPersona=forms.ChoiceField(choices=(regiones),label="Región")
    ciudadPersona=forms.ChoiceField(choices=(('1', 'First and only',),),label="Ciudad")
    #-----------------
    viviendaPersona=forms.ChoiceField(choices=(('1', 'Casa con Patio Grande'),('2', 'Casa con Patio Pequeño'),('3', 'Casa sin Patio'),('4', 'Departamento')),label="Tipo Vivienda")
    tipoPersona=forms.ChoiceField(choices=(('1', 'Usuario'),('2','Administrador'),),label="Tipo de Usuario")

# Formulario para el Login
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

# Formulario para Email Restablece Contraseña
class RecuperacionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut")

# Formulario para Restablecer Contraseña
class RestablecerForm(forms.Form):
    password_A=forms.CharField(widget=forms.PasswordInput(),label="Nueva Contraseña")
    password_B=forms.CharField(widget=forms.PasswordInput(),label="Repita Contraseña")

