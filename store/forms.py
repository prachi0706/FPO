from django import forms 
   
# import GeeksModel from models.py 
from .models import Fpo_Registeration 
   
# create a ModelForm 
class Fpo_Registeration_form(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Fpo_Registeration 
        fields = ['fpo_img']
