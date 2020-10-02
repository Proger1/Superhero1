from django.forms import ModelForm
from .models import Superhero



class SuperheroForm(ModelForm):
	class Meta:
		model = Superhero
		fields= '__all__'
		