from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Review
        fields = ("name", "email", "text")
