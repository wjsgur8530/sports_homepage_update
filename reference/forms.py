from django.forms import ModelForm
from reference.models import Material, Photo


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'content']

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'content']