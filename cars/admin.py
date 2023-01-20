from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from django.contrib import admin
from django.utils.html import format_html
from .models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'color', 'condition', 'price', 'state', 'fuel_type', 'thumbnail', 'is_featured')
    list_display_links = ('title', 'thumbnail',)
    list_filter = ('fuel_type', 'is_featured')
    list_editable = ('is_featured',)
    # fields = ('title', 'description', 'car_photo')
    search_fields = ('title', 'year', 'fuel_type', 'color', 'condition')
    save_on_top = True
    save_as = True

    def thumbnail(self, object):
        if object.car_photo:
            return format_html(f'<img src="{object.car_photo.url}" width="100">')
        else:
            return 'No photo yet'

    #
    thumbnail.short_description = 'Photo'


class CarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields["description"].required = False

    class Meta:
        model = Car
        fields = ("description",)
        widgets = {
          "text": CKEditor5Widget(
              attrs={"class": "django_ckeditor_5"}, config_name="description"
          )
        }

