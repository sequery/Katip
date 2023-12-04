from django import forms
from django.utils.html import conditional_escape
from foods.models import Food, Food_Category, Food_Size, Hall, Table, Order, Order_Items
import secrets

class AddFoodCategoryForm(forms.ModelForm):
    Türkmen = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    English = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    Pусский = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    title = forms.CharField(max_length=1000 ,widget = forms.HiddenInput(), required=False)

    class Meta:
        model = Food_Category
        fields = ['Türkmen', 'English', 'Pусский', 'title', 'description', 'image', 'parent_category', 'drink_category']
        widgets = {
            'description' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'parent_category' : forms.Select(attrs={'class':'form-select select2-hidden-accessible'}),
        }
    def clean(self):
        if self.is_valid():
            title = { "tm" : self.cleaned_data.get("Türkmen"),
                      "en" : self.cleaned_data.get("English"),
                      "ru" : self.cleaned_data.get("Pусский") }
            self.cleaned_data['title'] = title

class AddFoodForm(forms.ModelForm):
    Türkmen = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    English = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    Pусский = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    title = forms.CharField(max_length=1000 ,widget = forms.HiddenInput(), required=False)

    class Meta:
        model = Food
        fields = ['Türkmen', 'English', 'Pусский', 'title', 'description', 'image', 'category', 'discount', 'discount_unit']
        widgets = {
            'description' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'discount' : forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'discount_unit' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'category' : forms.Select(attrs={'class':'form-select select2-hidden-accessible'}),
        }
        
    def clean(self):
        if self.is_valid():
            title = { "tm" : self.cleaned_data.get("Türkmen"),
                      "en" : self.cleaned_data.get("English"),
                      "ru" : self.cleaned_data.get("Pусский") }
            self.cleaned_data['title'] = title 



class AddFoodSizeForm(forms.ModelForm):
    Türkmen = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    English = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    Pусский = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    title = forms.CharField(max_length=1000 ,widget = forms.HiddenInput(), required=False)

    class Meta:
        model = Food_Size
        fields = ['Türkmen', 'English', 'Pусский', 'title', 'price', 'food']
        widgets = {
            'price' : forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'food' : forms.Select(attrs={'class':'form-select select2-hidden-accessible'}),
        }

    def clean(self):
        if self.is_valid():
            title = { "tm" : self.cleaned_data.get("Türkmen"),
                      "en" : self.cleaned_data.get("English"),
                      "ru" : self.cleaned_data.get("Pусский") }
            self.cleaned_data['title'] = title


class AddHallForm(forms.ModelForm):
    Türkmen = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    English = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    Pусский = forms.CharField(max_length=255 ,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    title = forms.CharField(max_length=1000 ,widget = forms.HiddenInput(), required=False)

    class Meta:
        model = Hall
        fields = ['Türkmen', 'English', 'Pусский', 'title']

    def clean(self):
        if self.is_valid():
            title = { "tm" : self.cleaned_data.get("Türkmen"),
                      "en" : self.cleaned_data.get("English"),
                      "ru" : self.cleaned_data.get("Pусский") }
            self.cleaned_data['title'] = title

class AddTableForm(forms.ModelForm):

    class Meta:
        model = Table
        fields = ['number', 'hall']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'hall' : forms.Select(attrs={'class':'form-select select2-hidden-accessible'}),
        }


class AddOrderForm(forms.ModelForm):
    code = forms.CharField(max_length=10 ,widget = forms.HiddenInput(), required=False)

    class Meta:
        model = Order
        fields = ['code', 'table', 'waiter', 'cost', 'discount', 'service_cost', 'total_cost', 'paid', 'bill_taken', 'takeaway']
        widgets = {
            'table' : forms.Select(attrs={'class':'form-select select2-hidden-accessible'}),
            'waiter' : forms.Select(attrs={'class':'form-select select2-hidden-accessible'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'service_cost': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'total_cost': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'paid': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }

    def clean(self):
        if self.is_valid():
            code = secrets.token_hex(nbytes=4)
            code = code.upper()
            self.cleaned_data['code'] = code
            


class AddOrderItemForm(forms.ModelForm):

    class Meta:
        model = Order_Items
        fields = ['order', 'food', 'food_size', 'quantity', 'discount', 'cost', 'total_cost',]
        widgets = {
            'order' : forms.Select(attrs={'class':'form-select select2-hidden-accessible'}),
            'food' : forms.Select(attrs={'class':'form-select select2-hidden-accessible'}),
            'food_size' : forms.Select(attrs={'class':'form-select select2-hidden-accessible'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'total_cost': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }