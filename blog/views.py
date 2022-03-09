from django.shortcuts import render, redirect
from .models import Blog
from django.views.generic import \
    (ListView, DetailView, TemplateView, CreateView,DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
# def homepage(req):
#     blogs = Blog.objects.all()
#     context = {
#         'blogs': blogs
#     }
#     return render(req, 'blog/homepage.html', context)


class HomepageListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    extra_context = {'title': 'My Homepage project'}
    ordering = ['-post_created']
    template_name = 'blog/homepage.html'
    paginate_by = 3


# def aboutUs(req):
#     return render(req, 'blog/about.html')

class AboutTemplateView(TemplateView):
    extra_context = {'title': 'About Section'}
    template_name = 'blog/about.html'


class PostDetailsView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/postDetail.html'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    extra_context = {'btn_name': 'Create'}
    fields = ['title','content']
    context_object_name = 'form'
    template_name = 'blog/postEdit.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    extra_context = {'btn_name': 'Update'}
    fields = ['title','content']
    context_object_name = 'form'
    template_name = 'blog/postEdit.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        messages.warning(self.request, '403 Forbidden - Warning!!! You are not authorized to edit this post!')
        return redirect('blog:homepage')
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    context_object_name = 'blog'
    extra_context = {'btn_name': 'Delete'}
    success_url = reverse_lazy('blog:homepage')
    template_name = 'blog/postDelete.html'

    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        messages.warning(self.request, '403 Forbidden - Warning!!! You are not authorized to delete this post!')
        return redirect('blog:homepage')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    