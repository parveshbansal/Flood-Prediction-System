from django.shortcuts import render
import requests
from testapp import forms
from testapp.models import User
# Create your views here.
def home_view(request):
	res2=requests.get('https://api.thingspeak.com/channels/641798/fields/1/last.json?api_key=T49ZYG8UVGE6L0D7&results=2')
	val2=res2.json()
	a=dict(val2)
	a=val2['field1']
	a=int(a)
	print(a)
	return render(request,'testapp/home.html',{'a':a})
def level(request):
	res1=requests.get( 'https://api.thingspeak.com/channels/581721/fields/1/last.json?api_key=1EDOLPJ6NVUAJJSD&results=2')
	val1=res1.json()
	res2=requests.get( 'https://api.thingspeak.com/channels/581721/fields/3/last.json?api_key=1EDOLPJ6NVUAJJSD&results=2')
	val2=res2.json()
	val1=dict(val1)
	val2=dict(val2)
	k2=val1["field1"]
	k3=val2["field3"]
	my_dict={'level':k2,'flowrate':k3}
	return render(request,'testapp/level.html',context=my_dict)
def reg(request):
	form=forms.StudentForm()
	if request.method=='POST':
		form=forms.StudentForm(request.POST)
		if form.is_valid():
			form.save(commit=True)  #here inside one is optional
			print('data submit in db succesfully')
			print('student name:',form.cleaned_data['name'])
			name=form.cleaned_data['name']
			phoneno=form.cleaned_data['phoneno']
			villege=form.cleaned_data['village']
			resp=requests.post('https://api.thingspeak.com/update?api_key=I7MROKR0HPZX59Z6&field1='+name+'&field2='+str(villege)+'&field3='+str(phoneno))
			return render(request,'testapp/result.html',{'name':form.cleaned_data['name']})
	return render(request,'testapp/register.html',context={'form':form})
def res(request):
	return render(request,'testapp/result.html')
def about(request):
	return render(request,'testapp/about.html')