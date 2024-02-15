from django.contrib.auth import login
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView, ListView, TemplateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from apps.forms import UserForm, UserForm
from apps.models import UserListModel
from apps.tasks import task_send_email


# Create your views here.



class IndexView(ListView):
    paginate_by = 3
    template_name = 'index.html'
    queryset = UserListModel.objects.all()
    context_object_name = 'users'






class DeleteProductView(View):
    def get(self, request, pk, force_insert=False, force_update=False, using=None, update_fields=None):
        UserListModel.objects.filter(id=pk).delete()
        emails: list = UserListModel.objects.filter(id=pk).values('email')

        task_send_email.delay("Yangi blog qoshildi", UserListModel.objects.filter(id=pk).first_name, list(emails))

        return redirect('index')



class AddUser(FormView):
    template_name = 'addproduct.html'
    form_class = UserForm  # Use your form class
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()  # Save the form data directly
        return super().form_valid(form)
class ProductUpdateView(UpdateView):

    model = UserListModel
    fields = ['rasm', 'username', 'first_name', 'last_name', 'description', 'email', 'website']  # Fields to be displayed in the form
    template_name = 'update_product.html'
    success_url = reverse_lazy('index')  # Redirect URL after successful update
    context_object_name = 'product'