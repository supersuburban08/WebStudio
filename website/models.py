from django.db import models


class HeroSection(models.Model):
    heading = models.CharField(max_length=100, default="VIEW OUR WORK")
    video = models.FileField(upload_to='hero_videos/')
    button_text = models.CharField(max_length=50, default="View Our Reel")
    button_link = models.URLField(default="#")

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "Main section"
        verbose_name_plural = "Main sections"


class AboutBlock(models.Model):
    text = models.TextField()
    background = models.ImageField(upload_to='about_backgrounds/')

    def __str__(self):
        return self.text[:60]


class PhotoGallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo_gallery/')
    caption = models.TextField(blank=True)

    def __str__(self):
        return self.title


class VideoGallery(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='video_thumbs/')
    video_url = models.URLField()

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject[:30]}"
