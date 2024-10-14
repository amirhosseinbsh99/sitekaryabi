from django.shortcuts import render,redirect
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Create your views here.
def home_view(request):
    if not request.user.is_authenticated:

        return render(request, 'home/index-before.html')
    else:
       return redirect('accounts:dashboard_view')

def why_this_site(request):
    return render(request, 'home/چرا این سایت.html')

def my_saves(request):
    return render(request,'home/ذخیره های من.html')

def chat(request):
    return render(request,'home/چت.html')

def tutorial(request):
    return render(request, 'home/آموزش ها.html')

def my_investments(request):
    return render(request, 'home/سرمایه گذاری های من.html')


def my_funds(request):
    return render(request, 'home/سرمایه های من.html')

@login_required
def comment(request):
    comments = Comment.objects.all()

    comments = comments.filter(active=True)
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        global q
        q = request.POST.get('q')
        if  q=="" or q==None:
            if not comment_content:
                messages.error(request, 'متن شما خالی است')
            else:
                try:
                    comment = Comment.objects.get(
                        body=comment_content,
                        Username=request.user,
                        active=False,

                    )
                    messages.error(request, 'شما قبل این نظر را ارسال کردید')
                except Comment.DoesNotExist:
                    comment = Comment.objects.create(
                        Username=request.user,
                        body=comment_content,
                        active=False
                    )
                    messages.success(request, 'نظر شما ثبت شد')
                    return render(request, 'home/سوالات ونظرات.html',{'comments': comments})
        else:
            if request.method == 'POST':

                if q:
                    comments = Comment.objects.filter(active=True, body__contains=q)
                else:
                    comments = Comment.objects.filter(active=True)

                return render(request, 'home/سوالات ونظرات.html', {'comments': comments})




    return render(request, 'home/سوالات ونظرات.html',{'comments': comments})

    


