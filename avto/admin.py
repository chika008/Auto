from django.contrib import admin
from avto.models import Auto,Body,Color
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Auto)
class AvtoAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'title',
        'car_body',
        'price',
        'is_published',
        'year',
        'get_image',
        'date',
    )
    list_display_links = ('id', 'title')
    list_filter = ('price', 'is_published', 'year','date')
    list_editable = ('is_published',)
    
    @admin.display(description='Изображение')
    def get_image(self, instance: Auto):
        if instance.image:
            return mark_safe(f'<img src="{instance.image.url}" width="100px">')
        return '-'
    
    @admin.display(description='Изображение')
    def get_full_image(self, instance: Auto):
        if instance.image:
            return mark_safe(f'<img src="{instance.image.url}" width="50%">')
        return '-'
    
    search_fields = (
        'title', 
        'price',
        'color'
        
    )
    

@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'name',
        )
    list_display_links = ('id', 'name')
    search_fields = ('name',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'name',
        )
    list_display_links = ('id', 'name')
    search_fields = ('name',)


