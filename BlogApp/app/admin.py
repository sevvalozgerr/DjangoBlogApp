from django.contrib import admin

from app.models import Post, Profile, Tag, Comments, WebsiteMeta

# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Profile)
admin.site.register(WebsiteMeta)
