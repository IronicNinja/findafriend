from django.shortcuts import render
from .forms import UserQuestionForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully submitted this form!')
            return redirect('wait')
    else:
        form = UserQuestionForm()
    return render(request, 'qform/register.html', {'form': form})

def wait(request):
    return render(request, 'qform/wait.html', {'title': 'wait here'})