from . cart import Cart

# Create Context Processors so our cart can work on all pages of site
def cart(request):
    # Return the default data from our cart
    return {'cart': Cart(request)}