from django.shortcuts import render

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(avalaible = True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category) 
    return render(request, 'shopt/product/list.html', {'category': category,
                                                       'categories': categories,
                                                       'products': products})

def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, avalaible=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product':product,
                  'cart_product_form': cart_product_form})       
