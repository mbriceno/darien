from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from credits.models import Credit
from credits.forms import CreditForm



@method_decorator(login_required(login_url='/'), name='dispatch')
class CreditDetailView(DetailView):
    """
    View for displaying the details of a Credit.
    Override default DetailView with custom template and model.
    """
    model = Credit
    template_name = "credit_detail.html"


@method_decorator(login_required(login_url='/'), name='dispatch')
class CreditListView(ListView):
    """
    View for displaying a list of Credits.
    Override default ListView with custom template and model.
    """
    model = Credit
    template_name = "credit_list.html"


@method_decorator(login_required(login_url='/'), name='dispatch')
class CreditCreateView(SuccessMessageMixin, CreateView):
    """
    View for creating a new Credit.
    Override default CreateView with custom template, model and form.
    """
    model = Credit
    form_class = CreditForm
    template_name = "credit_form.html"
    success_url = reverse_lazy('credit_list')
    success_message = "Credit created successfully!"


@method_decorator(login_required(login_url='/'), name='dispatch')
class CreditUpdateView(SuccessMessageMixin, UpdateView):
    """
    View for updating an existing Credit.
    Override default UpdateView with custom template, model and form.
    """
    model = Credit
    form_class = CreditForm
    template_name = "credit_form.html"
    success_url = reverse_lazy('credit_list')
    success_message = "Credit updated successfully!"


@method_decorator(login_required(login_url='/'), name='dispatch')
class CreditDeleteView(DeleteView):
    """
    View for delete a Credit.
    Override default DeleteView with custom confirm template and model
    """
    model = Credit
    template_name = 'credit_confirm_delete.html'
    success_url = reverse_lazy('credit_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Credit deleted successfully!")
        return super().delete(request, *args, **kwargs)
