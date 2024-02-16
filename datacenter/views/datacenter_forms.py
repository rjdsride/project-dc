from django.shortcuts import render, get_object_or_404, redirect
from datacenter.models import Cable
from datacenter.forms import CableForm
from django.urls import reverse
from django.contrib import messages

# Função para criar um novo cabo
def create(request):
    form_action = reverse('datacenter:create')

    if request.method == 'POST':
        form = CableForm(request.POST)

        if form.is_valid():
            # Verifica se os dados do formulário já existem
            existing_cable = Cable.objects.filter(**form.cleaned_data).first()
            if existing_cable:
                messages.warning(request, 'Os dados já existem. Nenhuma alteração foi feita.')
            else:
                cable = form.save()
                messages.success(request, 'O cabo foi criado com sucesso!')
                return redirect('datacenter:update', cable_nep=cable.nep)

        return render(
            request,
            'datacenter/create.html',
            {'form': form, 'form_action': form_action},
        )

    return render(
        request,
        'datacenter/create.html',
        {'form': CableForm(), 'form_action': form_action},
    )

# Função para atualizar um cabo existente
def update(request, cable_nep):
    cable = get_object_or_404(Cable, nep=cable_nep)
    form_action = reverse('datacenter:update', args=(cable_nep,))

    if request.method == 'POST':
        form = CableForm(request.POST, instance=cable)

        if form.is_valid():
            # Verifica se os dados do formulário foram alterados
            if form.has_changed():
                cable = form.save()
                messages.success(request, 'A alteração foi um sucesso!')
            else:
                messages.info(request, 'Não há alterações nos dados.')

            return redirect('datacenter:update', cable_nep=cable.nep)

        return render(
            request,
            'datacenter/create.html',
            {'form': form, 'form_action': form_action},
        )

    return render(
        request,
        'datacenter/create.html',
        {'form': CableForm(instance=cable), 'form_action': form_action},
    )

def delete(request, cable_nep):
    cable = get_object_or_404(Cable, nep=cable_nep)
    cable.delete()
    return redirect('datacenter:index')

#    confirmation = request.POST.get('confirmation', 'no')

#    if confirmation == 'yes':
#        cable.delete()
#        return redirect('datacenter:index')
    
#    return render(
#        request,
#        'datacenter/cable.html',        {
#            'datacenter': cable,
#            'confirmation': confirmation,
#        }
#    )




