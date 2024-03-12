from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import AddUpdateForm
from .models import Updates
from django.contrib.auth.decorators import login_required
# Create your views here.
def updates(request):
    all_updates = Updates.objects.all() 
    return render(request, './updates/updates.html', {'updates': all_updates})

def updatesview(request, update_id):
    update = get_object_or_404(Updates, pk=update_id)
    return render(request, './updates/updatesview.html', {'update': update})

@login_required
def addupdates(request):
    if request.method == 'POST':
        form = AddUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True, user=request.user)
            return redirect('updates')
    else:
        form = AddUpdateForm()

    return render(request, './updates/addupdates.html', {'form': form})


@login_required
def delete_update(request, update_id):
    user = request.user

    # Ensure that the update belongs to the logged-in user
    update_instance = get_object_or_404(Updates, id=update_id, author=user)

    # Delete the update
    update_instance.delete()
    messages.success(request, 'Update deleted.')

    return redirect('updates')

