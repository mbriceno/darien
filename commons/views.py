from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CommonsLoginView(LoginView):
    """
    View for handler login override Django auth view.
    """
    template_name = 'login.html' # template on /templates
    success_url = '/clients/' # redirect to this success URL if login is successfull


@method_decorator(login_required(login_url='/'), name='dispatch')
class ClientDetailView(DetailView):
    """
    View for displaying Client profile. 
    Override default DetailView with custom template, model and object name
    """
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'


@method_decorator(login_required(login_url='/'), name='dispatch')
class ClientListView(ListView):
    """
    View for displaying a list of Credits.
    Override default ListView with custom template, model and object name
    """
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'


@method_decorator(login_required(login_url='/'), name='dispatch')
class ClientCreateView(CreateView):
    """
    View for create a new Client.
    Override default CreateView with custom template, model and form
    """
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.save()
        return response


@method_decorator(login_required(login_url='/'), name='dispatch')
class ClientUpdateView(UpdateView):
    """
    View for update a Client.
    Override default UpdateView with custom template, model and form
    """
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.save()
        return response


@method_decorator(login_required(login_url='/'), name='dispatch')
class ClientDeleteView(DeleteView):
    """
    View for delete a Client.
    Override default DeleteView with custom confirm template and model
    """
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')
