from django.shortcuts import render, redirect
from frontend.models import user

# Create your views here.
def frontpage(request):
    return render(request, "integration.html")


from .forms import PostForm

def create_user(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../../frontend/')  # url to integration.html
    else:
        form = PostForm()
    return render(request, 'home.html', {'form': form})