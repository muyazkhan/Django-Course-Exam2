from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import registaionForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# singup forms
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = registaionForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account successfully Created')
                form.save()
                print(form.cleaned_data)
        else:
            form = registaionForm()
        return render(request, 'singup.html', {'form': form})
    else:
        return redirect('home')

  # login forms
class userlogin(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


def user_logout(request):
    logout(request)
    return redirect('login')