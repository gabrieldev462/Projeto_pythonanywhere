from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product
from django import forms


# Formulário para Produto
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "image", "stock"]

# Listar produtos
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

# Criar produto
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "products/product_form.html", {"form": form})

# Editar produto
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "products/product_form.html", {"form": form, "product": product})

# Deletar produto
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "products/product_confirm_delete.html", {"product": product})

# Adicionar estoque
def product_add_stock(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        amount = int(request.POST.get("amount", 0))
        product.stock += amount
        product.save()
        return redirect("product_list")
    return render(request, "products/product_stock_form.html", {"product": product, "action": "Adicionar"})

# Remover estoque
def product_remove_stock(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        amount = int(request.POST.get("amount", 0))
        if amount > product.stock:
            amount = product.stock
        product.stock -= amount
        product.save()
        return redirect("product_list")
    return render(request, "products/product_stock_form.html", {"product": product, "action": "Remover"})
