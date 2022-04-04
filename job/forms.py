from django.forms import ModelForm
from .models import Apply

class ApplyForm(ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email', 'website', 'cv','cover_letter']