from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Stock
from .forms import StockForm


def view_detail(request):
    context = {
        'head_row': [''] + Stock.get_list_vaccin_label(),
        'body_rows': Stock.get_detail()
    }
    return render(request, 'stock/view_stock.html', context)


def view_global(request):
    context = {
        'head_row': ['centre', 'doses'],
        'body_rows': Stock.get_global()
    }
    return render(request, 'stock/view_stock.html', context)


@permission_required('stock.add_stock')
@login_required
def add(request):
    context = {'form': StockForm()}
    return render(request, 'stock/add.html', context)


@permission_required('stock.add_stock')
@login_required
def added(request):
    vaccin = request.POST.get('vaccin_id')
    centre = request.POST.get('centre_id')
    try:
        to_update = get_object_or_404(Stock, vaccin_id=vaccin, centre_id=centre)
        to_update.doses += int(request.POST.get('doses'))
        to_update.save()
    except Http404:  # unexisting tuple in db, creation of a new one
        form = StockForm(request.POST)
        to_update = form.save()
    context = {'stock': to_update}
    return render(request, 'stock/added.html', context)
