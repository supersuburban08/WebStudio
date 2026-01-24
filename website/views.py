from django.shortcuts import render, redirect


from .models import HeroSection, AboutBlock, VideoGallery, PhotoGallery, ContactMessage

from django.contrib import messages
from django.conf import settings
# from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Home page: Hero + About + Work galleries
def index(request):
    hero = HeroSection.objects.first()
    # about_blocks = AboutBlock.objects.all()
    # videos = VideoGallery.objects.all()
    # photos = PhotoGallery.objects.all()
    
    return render(request, 'website/index.html', {
        'hero': hero,
        # 'about_blocks': about_blocks,
        # 'videos': videos,
        # 'photos': photos
    })

def about(request):
    about_blocks = AboutBlock.objects.all()
    return render(request, 'website/about.html', {
        'about_blocks': about_blocks,
    })


def work(request):
    return render(request, 'website/work.html')

def photos(request):
    photos = PhotoGallery.objects.all()
    return render(request, 'website/photos.html', {
        'photos': photos,
    })

def videos(request):
    videos = VideoGallery.objects.all()
    return render(request, 'website/videos.html', {
        'videos': videos,
    })

# Contact page
def contact(request):
    if request.method == 'POST':
        # Gather form data
        name       = f"{request.POST['first_name']} {request.POST.get('last_name','')}"
        user_email = request.POST['email']
        subject    = request.POST['subject']
        body       = request.POST['message']

        # Save to the database
        ContactMessage.objects.create(
            name=name,
            email=user_email,
            subject=subject,
            message=body
        )

        # Compose the email body
        full_message = f"From: {name} <{user_email}>\n\n{body}"

        # Send the email
        email_msg = EmailMessage(
            subject=subject,
            body=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[user_email],
        )
        email_msg.send(fail_silently=False)

        messages.success(request, "Thanks! We’ve received your message.")
        return redirect('contact')

    return render(request, 'website/contact.html')