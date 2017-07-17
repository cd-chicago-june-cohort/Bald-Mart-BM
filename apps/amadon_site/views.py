from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime

def index(request):

    if 'items_allday' not in request.session:
        request.session['items_allday'] = []

    

    request.session['products']=[
        {'product_id': 0, 'product': 'Fleece-lined Coding Dojo Kung Fu Pants', 'price': 249.99},
        {'product_id': 1, 'product': 'Bright Yellow Hooded Windbreaker w/ Zippers', 'price': 79.99},
        {'product_id': 2, 'product': 'Extra Large Purple Velcro Fanny Pack', 'price': 49.99},
        {'product_id': 3, 'product': 'Solid Gold Self-Lubricating Hamster Wheel', 'price': 5399.99}
    ]
    
    print request.session['products'][1]['price'] #prints 79.99
    return render(request, 'amadon_site/index.html')




def checkout(request):

    if request.method == 'POST':



        # print request.POST['id']
        # print request.POST['quantity']

        request.session['quantity'] = int(request.POST['quantity'])

        item_name = request.session['products'][int(request.POST['id'])]['product']
        request.session['item_name'] = item_name

        request.session['price'] = float(request.session['products'][int(request.POST['id'])]['price'])

        request.session['cost'] = float(request.session['price'] * request.session['quantity'])

        return render(request, 'amadon_site/checkout.html')


    else:

        return redirect('/')


def reset(request):

    request.session.flush()
    return redirect('/')