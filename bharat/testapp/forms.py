from django import forms
from testapp.models import User
class StudentForm(forms.ModelForm):
	class Meta:
		model=User
		fields='__all__'
	def clean(self):
		print('total form validation')
		total_clean_data=super().clean()
		inputname=total_clean_data['phoneno']
		inputname=str(inputname)
		if len(inputname)<10:
			raise forms.ValidationError('Phone no must be 10 digit')