from django.contrib import admin

# Register your models here.
from .models import Post, Tag , About , Skill , Skill_Name ,  About_Name , Other_Post  

admin.site.register(Post)
admin.site.register(Other_Post)
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(About_Name)
admin.site.register(Skill)
admin.site.register(Skill_Name)
 