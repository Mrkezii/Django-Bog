from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import PostForm
from .models import Post
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print form.cleaned_data.get("title")
		# message success
		messages.success(request, "successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
	 	"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Post, id =id)
	context = {
	 "title": instance.title,
	 "instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
	"object_list" : queryset,
	 "title": "List"
	}
	return render(request, "post_list.html", context)
	

def post_update(request, id=None):
	instance = get_object_or_404(Post, id =id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href ='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	 	"title": instance.title,
	 	"instance": instance,
	 	"form":form,
	}
	return render(request, "post_form.html", context)
	

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id =id)
	instance.delete()
	messages.success(request, "successfully Deleted")
	return redirect("posts: list")
	

	







