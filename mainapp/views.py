from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import todo_dates, Items
import datetime

# Create your views here.
@login_required
def mytodos(request):

    selected_date = str(datetime.date.today())
    items = []
    try:
        todo_dates(date=selected_date, link = request.user).save()
    except:
        pass

    tododate = todo_dates.objects.filter(date = selected_date, link_id = request.user.id).first()
    items = Items.objects.filter(link_id = tododate.id)
    if request.method == "POST":
        print(request.POST,'----',request.POST['select_date'],request.user)
        selected_date = request.POST['select_date']
        tododate = todo_dates.objects.filter(date = selected_date, link_id = request.user.id).first()
        try:
            items = []
            items = Items.objects.filter(link_id = tododate.id)
        except:
            return HttpResponse("Date Not Found")
        finally:
            print('Next statement is Exeguting Add Operation')
            if request.POST.get('add'):
                print('Exeguting Add Operation Started')
                add_item = Items()

                add_item.content = request.POST['Add_text']

                add_item.link = tododate

                #tododate[0].link = request.user.id
                if add_item.content == "":
                    pass
                else:
                    print("Failed To Save")
                    add_item.save()

            print('Save Operation Next')
            if request.POST.get('save'):
                print('Save Operation Exeguting')
                for item in items:
                    if request.POST.get(str(item.id)) == "clicked":
                        item.completed = True
                        item.completed_on = datetime.date.today()
                    else:
                        item.completed = False
                        item.completed_on = None
                    item.content = request.POST.get('data' + str(item.id))
                    item.save()

            if request.POST.get('delete'):
                Items.objects.filter(id = request.POST.get('delete')).delete()
            
            
            return render(request,'mytodos.html',{'selected_date':selected_date, 'items':items})

    return render(request,'mytodos.html',{'selected_date':selected_date, 'items':items})


def contact(request):
    cf = ContactForm()
    return render(request,'contact.html',{'cf':cf})

def about(request):
    return render(request,'about.html',{})


def home(request):
    return render(request,'home.html',{})


def donate(request):
    return render(request,'donate.html',{})