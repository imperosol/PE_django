from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .forms import CentreForm
from .models import Centre


@permission_required('centre.add_centre')
@login_required
def add(request):
    context = {'form': CentreForm()}
    return render(request, 'centre/add.html', context)


@permission_required('centre.add_centre')
@login_required
def added(request):
    form = CentreForm(request.POST)
    new_centre = form.save()
    context = {'new': new_centre}
    return render(request, 'centre/added.html', context)


def view_all(request):
    centres = get_list_or_404(Centre)
    context = {'centres': centres}
    return render(request, 'centre/view_all.html', context)
