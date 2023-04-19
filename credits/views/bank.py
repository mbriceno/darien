from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from credits.models import Bank
from credits.forms import BankForm


@method_decorator(login_required(login_url='/'), name='dispatch')
class BankDetailView(DetailView):
    """
    View for displaying Bank profile. 
    Override default DetailView with custom template, model and object name
    """
    model = Bank
    template_name = 'bank_detail.html'
    context_object_name = 'bank'


@method_decorator(login_required(login_url='/'), name='dispatch')
class BankListView(ListView):
    """
    View for displaying a list of Banks.
    Override default ListView with custom template, model and object name
    """
    model = Bank
    template_name = 'bank_list.html'
    context_object_name = 'banks'


@method_decorator(login_required(login_url='/'), name='dispatch')
class BankCreateView(SuccessMessageMixin, CreateView):
    """
    View for create a new Bank.
    Override default CreateView with custom template, model and form.
    Implement SuccessMessageMixin to pass a message to the view.
    """
    model = Bank
    template_name = 'bank_form.html'
    form_class = BankForm
    success_url = reverse_lazy('bank_list')
    success_message = "Bank created successfully!"


@method_decorator(login_required(login_url='/'), name='dispatch')
class BankUpdateView(SuccessMessageMixin, UpdateView):
    """
    View for update a Bank.
    Override default UpdateView with custom template, model and form.
    Implement SuccessMessageMixin to pass a message to the view.
    """
    model = Bank
    template_name = 'bank_form.html'
    form_class = BankForm
    success_url = reverse_lazy('bank_list')
    success_message = "Bank updated successfully!"


@method_decorator(login_required(login_url='/'), name='dispatch')
class BankDeleteView(DeleteView):
    """
    View for delete a Bank.
    Override default DeleteView with custom confirm template and model
    """
    model = Bank
    template_name = 'bank_confirm_delete.html'
    success_url = reverse_lazy('bank_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Bank deleted successfully!")
        return super().delete(request, *args, **kwargs)
