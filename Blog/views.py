from django.shortcuts import render,HttpResponse,redirect
from Blog.models import Post ,BlogComment
from django.contrib.auth.models import User
from django.contrib import messages
from Blog.templatetags import extras


# Create your views here.
def blogHome(request):
    allposts=Post.objects.all()
    context={'allposts':allposts}
    return render(request,'Blog/home.html',context)


def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    post.views=post.views + 1 
    post.save()
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    repdict={}
    for reply in replies:
        if reply.parent.id not in repdict.keys():
            repdict[reply.parent.id]=[reply]
        else:
            repdict[reply.parent.id].append(reply)


    
    context={'post':post,'comments':comments,"user":request.user,"replydict":repdict}
    return render(request,'Blog/post.html',context)
    
def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postId=request.POST.get("postId")
        post=Post.objects.get(id=postId)
        parentId=request.POST.get("parentId")
        if parentId=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            messages.success(request,"Your comment has been posted succesfully")
        else:
            print(parentId)
            parent=BlogComment.objects.get(id=parentId)
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
            messages.success(request,"Your reply has been posted succesfully")

        comment.save()
        
        

      
    return redirect(f"/blog/{post.slug}")