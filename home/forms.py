from django.forms import ModelForm
from .models import *

class AuthorForm(ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"



