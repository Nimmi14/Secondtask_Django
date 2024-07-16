# views.py
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Patient, Doctor,Blog
from .forms import PatientSignUpForm, DoctorSignUpForm, BlogPostForm
from django.shortcuts import get_object_or_404

# hospital home page
def hospital_home(request):
    return render(request, 'webapp/hospital.html')

# patient register/signup 
def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/plogin/')  # Redirect to a success page or any desired URL
    else:
        form = PatientSignUpForm()
    return render(request, 'webapp/patientform.html', {'form': form})

# doctor register/signup 
def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dlogin/')  # Redirect to a success page or any desired URL
    else:
        form = DoctorSignUpForm()
    return render(request, 'webapp/doctorform.html', {'form': form})

# patient login form
def patient_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_patient:
                    login(request, user)
                    return redirect('pdash')
                else:
                    messages.error(request, 'User is not a patient.')
            else:
                messages.error(request, 'Invalid username and password.')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = AuthenticationForm()

    return render(request, 'webapp/patientlogin.html', {'form': form})

# doctor login form
def doctor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_doctor:
                    login(request, user)
                    return redirect('ddash')
                else:
                    messages.error(request, 'User is not a patient.')
            else:
                messages.error(request, 'Invalid username and password.')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = AuthenticationForm()

    return render(request, 'webapp/doctorlogin.html', {'form': form})

# logout view
def logout_view(request):
    logout(request)
    return redirect('/')

# patient dashboard
def patient_dashboard(request):
    if request.user.is_authenticated:
        patients = Patient.objects.filter(user=request.user)
        context={'patients':patients}
        return render(request, 'webapp/pdashboard.html',context)
    else:
        return redirect('plogin')

# doctor dashboard
def doctor_dashboard(request):
    if request.user.is_authenticated:
        doctors = Doctor.objects.filter(user = request.user)
        context = {'doctors':doctors}
        return render(request, 'webapp/ddashboard.html',context)
    else:
        return redirect('dlogin')
    
# blog page
def blog_home_page(request):
    draft = Blog.objects.filter(draft = True).order_by('-id')
    context = {'draft':draft}
    return render(request, 'webapp/bloghome.html',context)

# unpublished posts
def published_posts(request): 
    publish = Blog.objects.filter(publish=True).order_by('-id')
    context = {'publish':publish}   
    return render(request, 'webapp/posts.html',context)

# blog post form
def blog_post_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                user = request.user

                if user.is_authenticated:
                    if 'save_to_draft' in request.POST and user.is_doctor:
                        blog_post.user = user
                        blog_post.draft = True
                        blog_post.save()
                        messages.success(request, 'Blog post saved to draft successfully.')
                        form = BlogPostForm()
                    elif user.is_doctor:
                        blog_post.user = user
                        blog_post.publish = True
                        blog_post.save()
                        messages.success(request, 'Blog post published successfully.')
                        form = BlogPostForm()  
                    else:
                        messages.error(request, 'You are not a doctor. Cannot post a blog.')

        else:
            form = BlogPostForm()

        return render(request, 'webapp/blogform.html', {'form': form})
    else:
        return redirect('dlogin')


# publishing posts from unpublished post
def publish_draft_post(request, pk):
    post = Blog.objects.get(pk=pk,draft=True)
    post.publish = True
    post.draft = False  # Set draft to False when publishing
    post.save()
    return redirect('blog-posts')
    
    # Exclude the published post from the drafts queryset
    drafts = Blog.objects.filter(draft=True).exclude(pk=post.pk)
    
    context = {'drafts': drafts}
    return render(request, 'webapp/bloghome.html', context)

# patient see posts uploaded by the doctor
def patient_post_view(request):
    posts = Blog.objects.filter(publish=True).order_by('-id')
    context = {'posts':posts}
    return render(request, 'webapp/dp_posts.html',context)

# delete
def delete_posts(request, pk):
    post = Blog.objects.get(pk=pk)
    post.delete()
    return redirect('blog-posts')