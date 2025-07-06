from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def getPosts(request):
    template_name = 'postapp/list.html'
    posts = Post.objects.all()
    context={'posts':posts}
    return render(request, template_name=template_name, context=context)


def getPost(request, pk):
    template_name = 'postapp/detail.html'
    post = get_object_or_404(Post, id=pk)
    # comments = post.comments.all()
    comments = post.comments.filter(parent__isnull=True).order_by('-created_on')
    comment_form = CommentForm()

    tags = post.tag.all()
    print(tags)

    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            cf = comment_form.save(commit=False)
            cf.post = post

            parent_obj = None
            parent_id = request.POST.get("parentId")
            if parent_id:
                # parent_obj = Comment.objects.get(pk=parent_id)
                parent_obj = Comment.objects.filter(pk=parent_id).first()
            if parent_obj:
                cf.parent = parent_obj
            cf.save()
            comment_form = CommentForm()

    context={'post':post, "comment_form":comment_form, "comments":comments, 'tags':tags}
    return render(request, template_name=template_name, context=context)


def getPostsByTag(request, tagName):
    template_name = 'postapp/list.html'
    posts = Post.objects.filter(tag__name=tagName).all()
    return render(request=request, template_name=template_name, context={'posts':posts})