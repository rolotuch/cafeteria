# from django.shortcuts import render

# from .forms import LoginForm
# # Create your views here.
# class LoginUser(FormView):
#     template_name = 'users/login.html'
#     form_class = LoginForm
#     success_url = reverse_lazy('home_app:index')

#     def form_valid(self, form):
#         user = authenticate(
#             email=form.cleaned_data['email'],
#             password=form.cleaned_data['password']
#         )
#         login(self.request, user)
#         return super(LoginUser, self).form_valid(form)