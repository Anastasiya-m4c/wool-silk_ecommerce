from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'title', 'content', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Leave blank to post as "Anonymous"'
            }),
            'content': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.Select(choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]),
        }
        labels = {
            'name': 'Your Name (optional)',
            'title': 'Review Title',
            'content': 'Your Review',
            'rating': 'Rating'
        }
        help_texts = {
            'name': 'Other visitors will see this name. Leave blank to post anonymously.',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
