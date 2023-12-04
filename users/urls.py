from django.urls import path
from .views import *



app_name = 'users'

urlpatterns = [
    # Home Page
    path('home/', AdminPanelView.as_view(), name = 'home'),

    # Delete Profile
    path('delete/<int:id>/', UserDeleteView.as_view(), name = 'delete'),

    # Profile
    # path('profile/', user_view, name = 'profile'),
    path('profile/activity/', ProfileActivityView.as_view(), name = 'profile-activity'),
    path('edit/users/<int:pk>/', UserEditView.as_view(), name = 'edit'),
    
    # Others
    path('users/', UsersView.as_view(), name = 'users'),
    path('contact/', ContactView.as_view(), name = 'contact'),









    # # # # # # # # # # # # # Gereksiz # # # # # # # # # # # # # # #


    # path('profile/notify/', ProfileNotifyView.as_view(), name = 'profile-notify'),
    # path('profile/billing/', ProfileBillingView.as_view(), name = 'profile-billing'),
    # path('profile/setting/', ProfileSettingView.as_view(), name = 'profile-setting'),

    # path('faqs/', FaqsView.as_view(), name = 'faqs'),
    # path('downloads/', DownloadView.as_view(), name = 'downloads'),
    # path('pricing/', PricingView.as_view(), name = 'pricing'),

    # # Subscriptions
    # path('subscriptions/', SubscriptionsView.as_view(), name = 'subscriptions'),
    # path('subscriptions/details/', SubscriptionDetailView.as_view(), name = 'subscription-detail'),

    # # Support 
    # path('support/', SupportView.as_view(), name = 'support'),
    # path('support/topics/', SupportTopicView.as_view(), name = 'support-topic'),
    # path('support/topics/detail', SupportDetailView.as_view(), name = 'support-detail'),

    # # Invoices
    # path('invoices/', InvoicesView.as_view(), name = 'invoices'),
    path('invoice/detail/', InvoiceDetailView.as_view(), name = 'invoice-detail'),
    path('invoice/print/', InvoicePrintView.as_view(), name = 'invoice-print'),

    # # Tickets
    # path('tickets/', TicketsView.as_view(), name = 'tickets'),
    # path('ticket/detail/', TicketDetailView.as_view(), name = 'ticket-detail'),
]