from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.admin import AdminSite
from django.urls import path, reverse
from django.http import HttpResponseRedirect
from .models import TechPost, TechImage
from django.contrib.auth.models import Group, User

# Unregister default models you don't want
admin.site.unregister(Group)
admin.site.unregister(User)


# -------- Custom AdminSite --------
class CustomAdminSite(AdminSite):
    site_header = "Amdad Admin Panel"
    site_title = "Amdad Dashboard"
    index_title = "Portfolio Management"

    def get_urls(self):
        urls = super().get_urls()

        def custom_index(request):
            if not request.user.is_authenticated:
                return self.login(request)
            # Redirect to TechPost changelist page
            return HttpResponseRedirect(reverse('admin:mostafaraihan_techpost_changelist'))

        return [path('', custom_index, name='index')] + urls


custom_admin_site = CustomAdminSite(name='custom_admin')


# --------- TechImage Inline --------
class TechImageInline(admin.TabularInline):
    model = TechImage
    extra = 1
    fields = ('image_preview', 'image', 'uploaded_at')
    readonly_fields = ('image_preview', 'uploaded_at')
    ordering = ('-uploaded_at',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="100" height="100" '
                f'style="object-fit:cover; border-radius:8px; border:1px solid #ddd;" />'
            )
        return "No Image"

    image_preview.short_description = "Preview"


# --------- TechPost Admin --------
@admin.register(TechPost, site=custom_admin_site)
class TechPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'image_count')
    search_fields = ('title', 'note')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-updated_at', '-created_at')  # সর্বশেষ আপডেট বা তৈরি পোস্ট শীর্ষে
    date_hierarchy = 'updated_at'
    inlines = [TechImageInline]

    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = "Images"
