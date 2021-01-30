from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
from  .models import post
from .models import User

# Create your views here.


''' def home(request):
    context ={
        'posts':post.objects.all(),
    }
    return render(request,'blog/home.html',context)
 '''

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post   


def createPost(request):
    if request.method == 'POST':
        title = request.POST['blog-title']
        content = request.POST['blog-content']
        author_id = request.POST['user_id']
        new_post = post.objects.create(title=title,content=content,author_id=author_id)
        new_post.save()
        return redirect('blog-home')
    
    return render(request,'blog/update_post.html')  


def updatePost(request,pk):
    if request.method == 'POST':
        title = request.POST['blog-title']
        content = request.POST['blog-content']
        author_id = request.POST['user_id']
        new_post = post.objects.get(pk=pk)
        new_post.title = title
        new_post.content = content
        new_post.save()
        return redirect('blog-home')

    post_content=post.objects.filter(pk=pk)
    content = { 'posts' :post_content }
    return render(request,'blog/update_post.html',content)     

def deletePost(request,pk):
    post.objects.filter(pk=pk).delete()

    return redirect('blog-home')

def userPost(request,id):
    allUserPost = post.objects.filter(author_id=id)
    firstuser = post.objects.filter(author_id=id).first()
    name = firstuser.author
    content = { 'userPosts' :allUserPost ,'userName':name}
    return render(request,'blog/user_post.html',content) 


def about(request):
    return render(request,'blog/about.html',{'title':'About Page Updated'})  



def searchUser(request):
    if request.method == 'GET':
        username = request.GET.get('search_user')
        user_id = User.objects.filter(username=username).first()
        user_post = post.objects.filter(author_id=user_id).all()
        content = {'allUserPost':user_post}
        
        return render(request,'blog/search_user.html',content) 
