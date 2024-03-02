from django.shortcuts import render, redirect
from .forms import AddProduct

# Create your views here.

def addpdf(request):
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True, user=request.user)
            return redirect('home')
    else:
        form = AddProduct()

    return render(request, './pdf/pdf.html', {'form': form})