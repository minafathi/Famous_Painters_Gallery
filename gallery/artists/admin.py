from django.contrib import admin
from .models import Artist, Painting

class PaintingInline(admin.StackedInline):
    model = Painting

class ArtistAdmin(admin.ModelAdmin):
    inlines = [PaintingInline,]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Painting)
