from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseForbidden
from django.contrib import messages  # ✅ Added for success messages

@login_required
def home(request):
    query = request.GET.get('q')

    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)
        if fm.is_valid():
            product = fm.save(commit=False)
            product.user = request.user  # Assign logged-in user
            product.save()
            messages.success(request, "Product added successfully!")  # ✅ Optional success message
            return redirect("electronics:home")
    else:
        fm = ProductForm()

    if query:
        prod = Product.objects.filter(user=request.user, name__icontains=query)
    else:
        prod = Product.objects.filter(user=request.user)

    return render(request, 'electronics/home.html', {"prod": prod, "form": fm})

@login_required
def update_data(request, id):
    product = get_object_or_404(Product, pk=id)

    if product.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this product.")

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")  # ✅ Optional
            return redirect("electronics:home")
    else:
        form = ProductForm(instance=product)

    return render(request, 'electronics/update.html', {'form': form})

@login_required
def delete_data(request, id):
    product = get_object_or_404(Product, pk=id)

    if product.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this product.")

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully!")  # ✅ Optional
        return redirect("electronics:home")

    return redirect("electronics:home")

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")  # ✅ Success message
            return redirect("electronics:home")
    else:
        form = SignUpForm()
    return render(request, 'electronics/signup.html', {'form': form})

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Assign logged-in user
            product.save()
            messages.success(request, "Product added successfully!")  # ✅ Optional
            return redirect('electronics:home')
    else:
        form = ProductForm()
    return render(request, 'electronics/add_product.html', {'form': form})
