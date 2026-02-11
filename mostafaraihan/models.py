from django.db import models
from cloudinary.models import CloudinaryField

class TechPost(models.Model):
    title = models.CharField(max_length=100, blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # এই ফিল্ডটি আপডেট সময় ট্র্যাক করবে

    class Meta:
        ordering = ['-updated_at', '-created_at']  # সর্বশেষ আপডেট বা তৈরি পোস্ট প্রথমে

    def __str__(self):
        return self.title or f"Post {self.id}"


class TechImage(models.Model):
    post = models.ForeignKey(TechPost, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image') 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']  # সর্বশেষ আপলোড করা ছবি আগে

    def __str__(self):
        return f"Image {self.id} for {self.post.title}"
