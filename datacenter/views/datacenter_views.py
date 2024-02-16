from django.shortcuts import render,  get_object_or_404, redirect
from django.db.models import Q
from datacenter.models import Cable
from django.core.paginator import Paginator

# Create your views here.

def index(request):

    cables = Cable.objects\
        .filter()\
        .order_by('-nep')
    
    paginator = Paginator(cables, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    

    context = {
        'page_obj': page_obj,
        'title': 'Cables -'
    }

    return render (
        request,
        'datacenter/index.html',
        context,
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('datacenter:index')

    cables = Cable.objects\
        .select_related('dev_a', 'dev_b', 'group_dev')\
        .filter(
            Q(nep__icontains=search_value) |
            Q(dev_a__name__icontains=search_value) |
            Q(dev_b__name__icontains=search_value) |
            Q(description__icontains=search_value) |
            Q(group_dev__group_dev__icontains=search_value),
        )\
        .order_by('-nep')
    
    paginator = Paginator(cables, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    print(cables.query)

    context = {
        'page_obj': page_obj,
        'title': 'Search -',
        'search_value': search_value,

    }

    return render (
        request,
        'datacenter/index.html',
        context,
    )

def cable(request, cable_nep):
    single_cable = get_object_or_404(
        Cable, nep=cable_nep
    )

    site_title = f'{single_cable.nep} -'
    
    context = {
        'cable': single_cable, 
        'site_title' : site_title,
    }

    return render(
        request,
        'datacenter/cable.html',
        context,
    )