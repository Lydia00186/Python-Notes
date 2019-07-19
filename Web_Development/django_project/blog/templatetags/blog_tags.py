from ..models import Post, Category, Tag
from django import template

register = template.Library()


@register.simple_tag
def get_recent_posts(num=3):
	return Post.objects.all().order_by('-posted_time')[:num]


@register.simple_tag
def archives():
	return Post.objects.dates('posted_time','month', order = 'DESC')


@register.simple_tag
def get_categories():
	return Category.objects.all()


@register.simple_tag
def get_tags():
	return Tag.objects.all()