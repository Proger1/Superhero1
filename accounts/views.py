from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
# Create your views here.
from .models import *
from .forms import SuperheroForm
from django.core.paginator import Paginator 

def home(request):
    superheroes = Superhero.objects.all()
    paginator = Paginator(superheroes, 5)#5 сколько элементов на странице
    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number) 
    #context = {'superheroes' :superheroes}
    
    if page.has_next():
    	next_url = f'?page={page.next_page_number()}'
    else:
    	next_url= ''


    if page.has_previous():
    	prev_url = f'?page={page.previous_page_number()}'
    else:
    	prev_url= ''



    return render(request, 'accounts/dashboard.html', context={'superheroes': superheroes, 'page': page,  'next_page_url': next_url, 'prev_page_url': prev_url})       

#{'superheroes': page, элементы базы данных отображаються на странице по количеству картинок
#context={'superheroes': page.object_list}
#context={'page': page,

def superheroes(request):
	superheroes = Superhero.objects.all()

	return render(request, 'accounts/superheroes.html', {'superheroes' :superheroes})


def createSuperhero(request):
    form = SuperheroForm()
    if request.method == 'POST':
    	# print('Printing POST:',request.POST)
    	form = SuperheroForm(request.POST,request.FILES)
    	if form.is_valid():
    		form.save()
    		return redirect('/') #Возврат на главную

    context = {'form':form}

    return render(request, 'accounts/superhero_form.html',context)



def editSuperhero(request, pk):

    superhero=Superhero.objects.get(id=pk)
    form=SuperheroForm(instance=superhero)

    if request.method == 'POST':
    	# print('Printing POST:',request.POST)
    	form = SuperheroForm(request.POST, request.FILES, instance=superhero)
    	if form.is_valid():
    		form.save()
    		return redirect('/') #Возврат на главную
    context = {'form':form}
    return render(request, 'accounts/superhero_form.html',context) 



def deleteSuperhero(request,pk):
    superhero=Superhero.objects.get(id=pk)
    if request.method == "POST":
        superhero.delete() 
        return redirect('/') #Возврат на главную 
    context={'item' :superhero}
    return render(request, 'accounts/delete.html',context)
