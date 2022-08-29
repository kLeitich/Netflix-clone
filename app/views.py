from django.shortcuts import render,redirect

from app.forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request,'index.html')

def start(request):
    return render(request,"authenticate/start.html")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            # messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request,'authenticate/sign_up.html',context)

def login(request):
    return render(request,'log_in.html')

