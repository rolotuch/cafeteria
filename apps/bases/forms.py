# from django import forms
# from django.contrib.auth import authenticate

# class LoginForm(forms.Form):
#     email = forms.CharField(
#         label='E-mail',
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'input-group-field',
#                 'placeholder': 'Correo Electronico',
#             }
#         )
#     )
#     password = forms.CharField(
#         label='Contraseña',
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'input-group-field',
#                 'placeholder': 'contraseña'
#             }
#         )
#     )

#     def clean(self):
#         cleaned_data = super(LoginForm, self).clean()
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']

#         if not authenticate(email=email, password=password):
#             raise forms.ValidationError('Los datos de usuario no son correctos')
        
#         return self.cleaned_data
