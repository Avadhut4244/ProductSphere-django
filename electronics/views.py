from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

@login_required
def home(request):
    query = request.GET.get('q')  # Get search query from GET parameters

    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("electronics:home")  # using namespaced redirect
    else:
        fm = ProductForm()

    if query:
        prod = Product.objects.filter(name__icontains=query)
    else:
        prod = Product.objects.all()

    return render(request, 'electronics/home.html', {"prod": prod, "form": fm})

@login_required
def update_data(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("electronics:home")
    else:
        form = ProductForm(instance=product)

    return render(request, 'electronics/update.html', {'form': form})

@login_required
def delete_data(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("electronics:home")
    return redirect("electronics:home")

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # optional auto login
            return redirect("electronics:home")
    else:
        form = SignUpForm()
    return render(request, 'electronics/signup.html', {'form': form})

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('electronics:home')
    else:
        form = ProductForm()
    return render(request, 'electronics/add_product.html', {'form': form})
