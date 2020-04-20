from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, Category
from django.views.generic import (ListView, DetailView, CreateView , UpdateView, DeleteView, TemplateView) 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin


class BlogIndex(ListView):
    model       =   Post
    ordering    =   '-created_on'
    paginate_by = 4

#class BlogDetail(LoginRequiredMixin, DetailView):
    #model       =   Post


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)   
    context = {"post": post }
    return render(request,"blog/post_detail.html", context)


class BlogCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','body','image','categories']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class BlogUpdateView(SuccessMessageMixin, LoginRequiredMixin,UpdateView):
	model = Post
	fields = ['title','body','image','categories']
	success_message = "Post Updated!"

class BlogDeleteView(LoginRequiredMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('blog_index')
	


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    paginator = Paginator(posts, 4)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
        
    context = {
        "category": category,
        "page_obj": posts
    }
    return render(request, "blog/blog_category.html", context)