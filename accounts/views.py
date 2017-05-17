from django.shortcuts import render
from django.utils import timezone
from .models import Post
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'accounts/post_list.html', {'posts': posts})

def register(request):
	if request.method =='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def profile(request):
	args = {'user': request.user}
	return render(request, 'accounts/profile.html', args)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    args = {'post': post}
    return render(request, 'accounts/post_detail.html', args)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    	return render(request, 'accounts/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'accounts/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'accounts/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')