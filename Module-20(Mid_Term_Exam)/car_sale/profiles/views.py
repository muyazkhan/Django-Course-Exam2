from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .import forms
from . import models
from django.contrib import messages
from .models import Car,Purchase
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView,DetailView
# Create your views here.
# def profile(request):
#   return render(request,'profile.html')

method_decorator(login_required, name="dispatch")
class product_details(CreateView):
    model = models.Car
    form_class = forms.car
    template_name = 'home.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

method_decorator(login_required, name="dispatch")
class DetailPostView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'product_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
method_decorator(login_required, name="dispatch")        
class profile(CreateView):
    template_name = "profile.html"
    def get(self, request, *args, **kwargs):
        data = Purchase.objects.filter(user=request.user)
        return render(request, 'profile.html', {'data': data})  

method_decorator(login_required, name="dispatch")
def buy(request, id):
    data = Car.objects.get(pk = id)
    quant = data.quantity
    if quant > 0:
        quant -= 1
        data.quantity = quant
        data.save()
        Purchase.objects.create(user=request.user, car = data)
        return redirect('profile')
    return render(request, 'product_details.html', {'car': data})