from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DeleteView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from users.models import User
from foods.models import Food, Food_Category, Table
from users.forms import RegistrationForm, UserAuthenticationForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Registration Pages

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('users:home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/register.html', context)


def login_view(request):
    
    context = {}

    user = request.user 
    if user.is_authenticated:
        return redirect('users:home')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('users:home')
    else:
        form = UserAuthenticationForm()
        
    context['login_form'] = form
    return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('users:home')


# def user_view(request):

#     if not request.user.is_authenticated:
#         return redirect('login')

#     context = {}

#     if request.POST:
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserUpdateForm(
#             initial= {
#                 'email' : request.user.email,
#                 'username' : request.user.username,
#                 'admin' : request.user.admin,
#                 'staff' : request.user.staff,
#                 'active' : request.user.active,
#                 'confirmed' : request.user.confirmed,
#             }
#         )
#     context['user_form'] = form
#     return render(request, 'admin/profile.html', context)

    

# Home View

class AdminPanelView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        food = Food.objects.all()
        categories = Food_Category.objects.all()
        table = Table.objects.all()
        context['foods'] = food
        context['tables'] = table
        context['categories'] = categories
        User = get_user_model()
        users = User.objects.all()
        context['users'] = users
        return context

# Error Views

def view_404(request, exception):
    return render(request, '404.html')


def view_403(request, exception):
    return render(request, '403.html')


def view_500(request):
    return render(request, '500.html')

# Profile Views

class UserEditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'admin/user-edit.html'
    success_url = '/users/'
    

class ContactView(TemplateView):
    template_name = 'admin/contact.html'

class UsersView(TemplateView):
    template_name = 'admin/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        users = User.objects.all()
        context['users'] = users
        return context

class UserDeleteView(DeleteView):
    model = User
    template_name = 'admin/user-delete.html'
    success_url = reverse_lazy('users:home')

    def get_object(self, queryset=None):
        return User.objects.get(id=self.kwargs.get("id"))

class ProfileActivityView(TemplateView):
    template_name = 'admin/profile-activity.html'







# # # # # # # # # # # # # # Gereksiz # # # # # #  # # # # # # # # # # #


# class ProfileSettingView(TemplateView):
#     template_name = 'admin/profile-setting.html'

# class ProfileBillingView(TemplateView):
#     template_name = 'admin/profile-billing.html'

# class ProfileNotifyView(TemplateView):
#     template_name = 'admin/profile-notify.html'

# # Subscription

# class SubscriptionsView(TemplateView):
#     template_name = 'admin/subscriptions.html'

# class SubscriptionDetailView(TemplateView):
#     template_name = 'admin/subscriptions-detail.html'

# # Support View

# class SupportView(TemplateView):
#     template_name = 'admin/support.html'

# class SupportTopicView(TemplateView):
#     template_name = 'admin/support-topics.html'

# class SupportDetailView(TemplateView):
#     template_name = 'admin/support-topic-detail.html'

# # Ticket Views

# class TicketDetailView(TemplateView):
#     template_name = 'admin/ticket-details.html'

# class TicketsView(TemplateView):
#     template_name = 'admin/tickets.html'

# # Invoice Views

# class InvoicesView(TemplateView):
#     template_name = 'admin/invoices.html'

class InvoiceDetailView(TemplateView):
    template_name = 'admin/invoice-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        users = User.objects.all()
        context['users'] = users
        return context

class InvoicePrintView(TemplateView):
    template_name = 'admin/invoice-print.html'

# # Other Views

# class FaqsView(TemplateView):
#     template_name = 'admin/faqs.html'

# class DownloadView(TemplateView):
#     template_name = 'admin/downloads.html'

# class PricingView(TemplateView):
#     template_name = 'admin/pricing.html'

