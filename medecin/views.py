from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required, login_required
from .models import RegistrationRequest


def view_all(request):
    doctors = User.objects.filter(groups__name='medecin')
    context = {'doctors': doctors}
    return render(request, 'medecin/view_all.html', context)


@login_required
def ask_registering(request):
    previously_requested = RegistrationRequest.objects.filter(user=request.user).exists()
    if previously_requested:
        return redirect('/')
    else:
        return render(request, 'medecin/register_form.html')


@login_required
def show_register_result(request):
    return render(request, 'medecin/register_result.html')


@login_required
def register_result(request):
    if 'confirm-demand' in request.POST:
        obj, created = RegistrationRequest.objects.get_or_create(user=request.user)
        if created:
            return redirect('medecin:show_registered')
    return redirect('/')


@login_required
@permission_required('groups.add_medecin')
def check_requests(request):
    pending_requests = RegistrationRequest.objects.all()
    context = {'requests': pending_requests}
    return render(request, "medecin/check_requests_form.html", context)


@login_required
@permission_required('groups.add_medecin')
def approve_requests(request):
    # get all elements of the post request corresponding to the users to validate
    str_ids = [
        key for key in request.POST
        if key.startswith('id') and request.POST[key] in ['1', '2']
    ]
    # convert elements previously got into usable integer ids
    query_ids = [int(key.removeprefix('id')) for key in str_ids]
    # get all the requests that have been either explicitly confirmed or refused
    pending_requests = RegistrationRequest.objects.filter(user__pk__in=query_ids)
    accepted_users = [
        req.user for req in pending_requests
        if request.POST[f'id{req.user.id}'] == '1'
    ]
    doctors = Group.objects.get(name='medecin')
    doctors.user_set.add(*accepted_users)
    pending_requests.delete()
    return redirect('medecin:view_all')
