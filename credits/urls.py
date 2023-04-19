from django.urls import path
from .views import BankCreateView, BankUpdateView, BankDeleteView, BankListView, BankDetailView
from .views import CreditListView, CreditCreateView, CreditUpdateView, CreditDetailView, CreditDeleteView


urlpatterns = [
    path('banks/', BankListView.as_view(), name='bank_list'),
    path('banks/new/', BankCreateView.as_view(), name='bank_create'),
    path('banks/<int:pk>/edit/', BankUpdateView.as_view(), name='bank_update'),
    path('banks/<int:pk>/delete/', BankDeleteView.as_view(), name='bank_delete'),
    path('banks/<int:pk>/', BankDetailView.as_view(), name='bank_detail'),

    # List view of all credits
    path('', CreditListView.as_view(), name='credit_list'),

    # Detail view for a single credit
    path('<int:pk>/', CreditDetailView.as_view(), name='credit_detail'),

    # Create view for a new credit
    path('create/', CreditCreateView.as_view(), name='credit_create'),

    # Update view for an existing credit
    path('<int:pk>/update/', CreditUpdateView.as_view(), name='credit_update'),

    # Delete view for an existing credit
    path('<int:pk>/delete/', CreditDeleteView.as_view(), name='credit_delete'),
]
