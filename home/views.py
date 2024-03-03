from django.shortcuts import render, redirect
from django.contrib.auth import authenticate ,login as dj_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import SignupForm
from pdf.models import Pdf
from django.db.models import Q


# Create your views here.
def home(request):
    query = request.GET.get('q')
    pdf_files = Pdf.objects.all()

    if query:
        pdf_files = pdf_files.filter(
            Q(title__icontains=query) |
            Q(author__username__icontains=query) |
            Q(product_type__icontains=query)
            # Adjust 'username' to the actual field on the User model you want to search on
        )

    return render(request, './home/home.html', {'pdf_files': pdf_files, 'query': query})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)

            # Log in the user
            user = authenticate(username=username, password=password)
            dj_login(request, user)

            return redirect('home')  # Replace 'home' with your home page URL
    else:
        form = SignupForm()

    return render(request, './join/signup.html' , {'form': form})




def login(request):
    page = 'login'

    # Check if the user is already logged in
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Invalid username or password')
            return redirect("login")

    if 'next' in request.POST:
        return redirect(request.POST['next'])

    return render(request, './join/login.html')




def contact(request):
    return render(request, './others/contact.html')

def aboutus(request):
    return render(request, './others/aboutus.html')

def termsofuse(request):
    return render(request, './others/termsofuse.html')
