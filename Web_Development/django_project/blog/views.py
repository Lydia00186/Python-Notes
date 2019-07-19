from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.core.paginator import Paginator
import markdown



# def index(request):

#     post_list = Post.objects.all()

#     md = markdown.Markdown(extensions=[
# 							'markdown.extensions.extra',
# 							'markdown.extensions.codehilite',
# 							'markdown.extensions.toc',
# 						])
#     for post in post_list:
#         post.content = md.convert(post.content)

#     limit = 2

#     paginator = Paginator(post_list, limit)  

#     # default: start from page 1
#     page = request.GET.get('page','1')  

#     post_list = paginator.page(page) 


#     return render(request, 'blog/index.html', context={'post_list': post_list})




class IndexView(ListView):

	model = Post
	template_name = 'blog/index.html'
	context_object_name = 'post_list'


# We need to insert the markdown into the post.content
	def get_queryset(self):
		post_list = Post.objects.all()

		md = markdown.Markdown(extensions=[
								'markdown.extensions.extra',
								'markdown.extensions.codehilite',
								'markdown.extensions.toc',
							])

		for post in post_list:
			post.content = md.convert(post.content)

		return post_list


	paginate_by =5






# def detail(request, pk):
# 	post = get_object_or_404(Post, pk=pk)

# 	md = markdown.Markdown(extensions=[
# 							'markdown.extensions.extra',
# 							'markdown.extensions.codehilite',
# 							'markdown.extensions.toc',
# 						])

# 	post.content = md.convert(post.content)

# 	post.toc = md.toc

# 	context = {
# 		'post':post
# 	}

# 	return render(request, 'blog/detail.html', context)


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/detail.html'


	def get_object(self, queryset=None):

		post = super(PostDetailView, self).get_object(queryset=None)

		md = markdown.Markdown(extensions=[
								'markdown.extensions.extra',
								'markdown.extensions.codehilite',
								'markdown.extensions.toc',
							])

		post.content = md.convert(post.content)

		post.toc = md.toc

		return post

# To make sure nobody else can update your post (current logged-in user ), we need to import 
# UserPassesTestMixin from the django.contrib.auth.mixins
class PostCreateView(LoginRequiredMixin,CreateView):

	model = Post
	fields = ['title', 'content', 'category', 'excerpt', 'tag']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content', 'category', 'excerpt', 'tag']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False




def archives(request, year, month):

	post_list = Post.objects.filter(posted_time__year = year,
									posted_time__month = month)
	context = {
		'post_list': post_list
	}
	return render(request, 'blog/index.html', context)


def category(request,pk):

	cate = get_object_or_404(Category,pk=pk)

	post_list = Post.objects.filter(category=cate)

	return render(request,'blog/index.html', context={'post_list':post_list})


class TagView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tag=tag)