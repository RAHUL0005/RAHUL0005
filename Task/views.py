from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm, RegForm,LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
#             send_mail(
#     "Subject here",
#     "Here is the message.",
#     "rahul.tr@bksec.com",
#     ["trrahultr2000@example.com"],
#     fail_silently=False,
# )

            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete_task()
    return redirect('task_list')

def home_view(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegForm()

    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('task_list')  # Redirect to the user's dashboard or any desired page
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

from django.shortcuts import render
from django.urls import reverse
from urllib.parse import urlencode

def share_via_whatsapp(request, post_id):
    # Retrieve the blog post details based on post_id
    post = YourPostModel.objects.get(id=post_id)

    # Recipient's phone number to send the message to
    recipient_phone = '9080041196'  # Replace this with the recipient's phone number

    # Construct the message to be shared
    message = f"Check out this blog post: {post.title}. Read more at {request.build_absolute_uri(reverse('post_detail', args=[post_id]))}"

    # Construct the WhatsApp share URL with the recipient's phone number and message
    whatsapp_url = f"https://api.whatsapp.com/send?phone={recipient_phone}&text={urlencode(message)}"

    return render(request, 'task_list.html', {'whatsapp_url': whatsapp_url})
