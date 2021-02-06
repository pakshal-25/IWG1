from django.contrib import admin
from .models import Post
from .models import Image
from .models import Contact
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc'] 
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']



# Register your models here.
admin.site.register(Contact)
