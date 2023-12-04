from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from foods.forms import AddFoodForm, AddFoodCategoryForm, AddFoodSizeForm, AddHallForm, AddOrderForm, AddOrderItemForm, AddTableForm
from foods.models import Food, Food_Category, Food_Size, Hall, Order, Order_Items, Table
import os
from django.template.loader import render_to_string

class CreateHomeView(TemplateView):
    template_name = 'create.html'


# Food Category

class AddFoodCategoryView(CreateView):
    model = Food_Category
    form_class = AddFoodCategoryForm
    template_name = 'food_category/add-food_category.html'
    success_url = '/foods/categories'            


class UpdateFoodCategoryView(UpdateView):
    model = Food_Category
    form_class = AddFoodCategoryForm
    template_name = 'food_category/add-food_category.html'
    success_url = '/foods/categories'


class DetailFoodCategoryView(DetailView):
    model = Food_Category
    template_name = 'food_category/detail-food_category.html'


class DeleteFoodCategoryView(DeleteView):
    model = Food_Category
    template_name = 'food_category/delete-food_category.html'
    success_url = '/foods/categories'


class FoodCategoryListView(ListView):
    model = Food_Category
    template_name = 'food_category/list-food_category.html'


# Food

class AddFoodView(CreateView):
    model = Food
    form_class = AddFoodForm
    template_name = 'food/add-food.html'
    success_url = '/foods/foods'


class UpdateFoodView(UpdateView):
    model = Food
    form_class = AddFoodForm
    template_name = 'food/add-food.html'
    success_url = '/foods/foods'


class DetailFoodView(DetailView):
    model = Food
    template_name = 'food/detail-food.html'


class DeleteFoodView(DeleteView):
    model = Food
    template_name = 'food/delete-food.html'
    success_url = '/foods/foods'


class AddFoodSizeView(CreateView):
    model = Food_Size
    form_class = AddFoodSizeForm
    template_name = 'food/add-food_size.html'
    success_url = '/foods/foods'


class UpdateFoodSizeView(UpdateView):
    model = Food_Size
    form_class = AddFoodSizeForm
    template_name = 'food/add-food_size.html'
    success_url = '/foods/foods'


class DeleteFoodSizeView(DeleteView):
    model = Food_Size
    template_name = 'food/delete-food_size.html'
    success_url = '/foods/foods'


class FoodListView(ListView):
    model = Food
    template_name = 'food/list-food.html'


# Hall

class AddHallView(CreateView):
    model = Hall
    form_class = AddHallForm
    template_name = 'hall/add-hall.html'
    success_url = '/foods/halls'


class UpdateHallView(UpdateView):
    model = Hall
    form_class = AddHallForm
    template_name = 'hall/add-hall.html'
    success_url = '/foods/halls'


class DeleteHallView(DeleteView):
    model = Hall
    template_name = 'hall/delete-hall.html'
    success_url = '/foods/halls'


class DetailHallView(DetailView):
    model = Hall
    template_name = 'hall/detail-hall.html'


class HallListView(ListView):
    model = Hall
    template_name = 'hall/list-hall.html'


# Table

class AddTableView(CreateView):
    model = Table
    form_class = AddTableForm
    template_name = 'table/add-table.html'
    success_url = '/foods/tables'


class UpdateTableView(UpdateView):
    model = Table
    form_class = AddTableForm
    template_name = 'table/add-table.html'
    success_url = '/foods/tables'


class DeleteTableView(DeleteView):
    model = Table
    template_name = 'table/delete-table.html'
    success_url = '/foods/tables'


class DetailTableView(DetailView):
    model = Table
    template_name = 'table/detail-table.html'

class TableListView(ListView):
    model = Table
    template_name = 'table/list-table.html'


# Orders

class AddOrderView(CreateView):
    model = Order
    form_class = AddOrderForm
    template_name = 'order/add-order.html'
    success_url = '/foods/orders'



class DeleteOrderView(DeleteView):
    model = Order
    template_name = 'order/delete-order.html'
    success_url = '/foods/orders'



class UpdateOrderView(UpdateView):
    model = Order
    form_class = AddOrderForm
    template_name = 'order/add-order.html'
    success_url = '/foods/orders'



class DetailOrderView(DetailView):
    model = Order
    template_name = 'order/detail-order.html'

    def post(self, request, *args, **kwargs):
        
        order = Order.objects.get(id = self.get_object().id)
        ordered_items = Order_Items.objects.filter(order = order)
        change = order.paid - order.total_cost
        # Invoice Recording Area
        handle1=open('invoices/clients/invoice.txt','w+')
        handle1.write("--------------- Market Ady ---------------")
        def newline():
            return handle1.write("\n")
        newline()
        handle1.write("Wagty : ")
        handle1.write(str(order.created))
        newline()
        handle1.write("Amal : ")
        handle1.write(str(order.code))
        newline()
        handle1.write("Alynanlar : ")
        newline()
        for ordered_item in ordered_items:
            handle1.write(str(ordered_item.food.title['tm']))
            handle1.write(" ")
            handle1.write(str(ordered_item.food_size.title['tm']))
            handle1.write(" version")
            handle1.write("  x ")
            handle1.write(str(ordered_item.quantity))
            handle1.write("                   ")
            handle1.write(str(ordered_item.discount))
            handle1.write(" %     ")
            newline()
        newline()
        handle1.write("----------------------------------------------------")
        newline()
        handle1.write("Jemi :   ")
        handle1.write(str(order.total_cost))
        newline()
        handle1.write("----------------------------------------------------")
        newline()
        handle1.write("Berlen :   ")
        handle1.write(str(order.paid))
        newline()
        handle1.write("Gaytargy :   ")
        handle1.write(str(order.paid - order.total_cost))
        newline()
        newline()
        handle1.write("Kassir :   ")
        handle1.write(str(order.waiter.name))
        handle1.write(" ")
        handle1.write(str(order.waiter.surname))
        newline()
        newline()
        newline()
        handle1.write("Sowdanyz Ucin Sag Bolun !!")
        handle1.close()
        
        
        # Saving To Records

        handle1=open('invoices/Record.txt','a+')
        newline()
        handle1.write("----------------------------------------------------")
        newline()
        handle1.write("Wagty : ")
        handle1.write(str(order.created))
        newline()
        handle1.write("Amal : ")
        handle1.write(str(order.code))
        newline()
        handle1.write("Alynanlar : ")
        newline()
        for ordered_item in ordered_items:
            handle1.write(str(ordered_item.food.title['tm']))
            handle1.write(" ")
            handle1.write(str(ordered_item.food_size.title['tm']))
            handle1.write(" version")
            handle1.write("  x ")
            handle1.write(str(ordered_item.quantity))
            handle1.write("                   ")
            handle1.write(str(ordered_item.discount))
            handle1.write(" %     ")
            newline()
        newline()
        handle1.write("Jemi :   ")
        handle1.write(str(order.total_cost))
        newline()
        handle1.write("Berlen :   ")
        handle1.write(str(order.paid))
        newline()
        handle1.write("Gaytargy :   ")
        handle1.write(str(order.paid - order.total_cost))
        newline()
        handle1.write("Kassir :   ")
        handle1.write(str(order.waiter.name))
        handle1.write(" ")
        handle1.write(str(order.waiter.surname))
        handle1.close()
        handle1 = open('C:\\Users\\User\\Desktop\\DjangoAdmin\\templates\\receipt1.html', 'w')
        context = {
            'order' : order,
            'ordered_items' : ordered_items,
            'change' : change
        }
        html = render_to_string('receipt.html', context)
        handle1.write(html)
        handle1.close()
        print("Here : " + html)
        os.system('python invoices/rec.py')
        return render(request, 'receipt1.html')

class OrdersListView(ListView):
    model = Order
    template_name = 'order/list-orders.html'
    a = 0
# Order Items

class AddOrderItemView(CreateView):
    model = Order_Items
    form_class = AddOrderItemForm
    template_name = 'order/add-order_item.html'
    success_url = '/foods/orders'
