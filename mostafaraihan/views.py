from django.shortcuts import render, get_object_or_404, redirect
from .models import TechPost
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    posts = TechPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

# -------------------- TechPost Detail --------------------
def techpost_detail(request, pk):
    """
    Single TechPost detail page
    """
    post = get_object_or_404(TechPost, pk=pk)
    return render(request, 'techpost_detail.html', {'post': post})

# -------------------- All Posts Page --------------------
def post(request):
    """
    All posts page: নতুন পোস্ট প্রথমে
    """
    posts = TechPost.objects.all().order_by('-created_at')
    return render(request, 'post.html', {'posts': posts})

# -------------------- Contact Form --------------------
def contact(request):
    """
    Contact form: email পাঠাবে এবং success/error message দেখাবে
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                email,
                ['raihan.invite@gmail.com'], 
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")

        return redirect('index')

    return render(request, 'contact.html')

def sitemap(request):
    return render(request, 'sitemap.xml', content_type='application/xml')


def robots(request):
    return render(request, 'robots.txt', content_type='text/plain')