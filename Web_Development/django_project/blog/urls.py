from django.urls import path
from . import views



urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	# path('', views.index, name='index'),
	# path('post/<int:pk>/', views.detail, name='detail'),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
	path('post/<int:pk>/update/', views.PostUpdateView.as_view(template_name='blog/update.html'), name='update'),
	path('archives/<int:year>/<int:month>/',views.archives, name='archives'),
	path('category/<int:pk>/', views.category, name = 'category'),
	path('tag/<int:pk>/', views.TagView.as_view(), name = 'tag'),
	path('post/new/', views.PostCreateView.as_view(), name='post-new'),

]

