# website/admin.py
from django.contrib import admin
from .models import (
    HeroSection, AboutBlock,
    VideoGallery, PhotoGallery,
    ContactMessage
)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    pass

@admin.register(AboutBlock)
class AboutBlockAdmin(admin.ModelAdmin):
    pass

@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ('name','email','subject','message','created_at')
    list_display    = ('name','email','subject','created_at')
