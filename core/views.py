from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
from core.forms import *

# Create your views here.

def dashboard(request):
	return render(request, "core/dashboard.html")



def checkout(request):
	 checkout_data = checkout_form()
	 if (request.method=="POST"):
	    checkout_data = checkout_form(request.POST)
	 if checkout_data.is_valid():
			Item_Name = checkout_data.cleaned_data['name']
			StudentID = checkout_data.cleaned_data['studentID']
			Quantity = checkout_data.cleaned_data['quantity']
			print(Item_Name)
			print(StudentID)
			print(Quantity)

	 context = {'checkout_data':checkout_data}
	 return render(request, "core/checkout.html",context)



def impact(request):
	return render(request, "core/impact.html")



def inventory(request):

	item_data = additem_form()
	if (request.method=="POST"):
		item_data = additem_form(request.POST)
		if item_data.is_valid():
			Name = item_data.cleaned_data['name']
			Expiry = item_data.cleaned_data['expiry_D']
			Price = item_data.cleaned_data['price']
			Quantity = item_data.cleaned_data['quantity']
			print(Name)
			print(Expiry)
			print(Price)
			print(Quantity)

	context = {'item_data':item_data}
	return render(request, "core/inventory.html", context)
