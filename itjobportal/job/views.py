from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, JobApplyForm
from .models import Job, Category, UserRequest
from django.contrib.auth.models import User


def frontpage(request):

    jobs = Job.objects.filter(is_active=True)
    categories = Category.objects.all()

    chosen_category = request.GET.get('category', '')
    if chosen_category:
        jobs = jobs.filter(category__slug=chosen_category)
    
    context = {
        'categories': categories,
        'jobs': jobs,
        'chosen_category': chosen_category
    }

    return render(request, 'job/frontpage.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'job/signup.html', {'form': form})


def about(request):
    return render(request, 'job/about.html')


def contacts(request):
    return render(request, 'job/contacts.html')


def job(request, slug):
    job = get_object_or_404(Job, slug=slug)

    context = {'job': job}

    return render(request, 'job/job.html', context)


@login_required
def apply_job(request, id):

    form = JobApplyForm(request.POST or None)

    user = get_object_or_404(User, id=request.user.id)
    applicant = UserRequest.objects.filter(user=user, job=id)

    if not applicant:
        if request.method == 'POST':

            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = user
                instance.save()

        else:
            return redirect("/")
    return redirect("/")


@login_required
def user_requests(request):
    return render(request, "job/requests.html")


@login_required
def profile(request):
    return render(request, "job/profile.html")


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')       
        user.profile.location = request.POST.get('location')
        user.profile.skills = request.POST.get('skills')
        user.profile.linkedin = request.POST.get('linkedin')

        user.save()

        return redirect('profile')
    return render(request, "job/edit_profile.html")

