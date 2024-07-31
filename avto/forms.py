# forms.py
from django import forms
from avto.models import Auto


class PostForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = [
            "title",
            "image",
            "car_body",
            "price",
            "year",
            "color",
            "description",
            "is_published",
            "date",
        ]
