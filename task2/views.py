from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#tasks = ["Task:1", "Task:2", "Task:3"]
#tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index2(request):
    if "tasks" not in request.session:
        request.session["tasks"]= []
        
    return render(request, "task2/index2.html", {
        #"tasks": tasks
        "tasks":request.session["tasks"]
        
    })

def add2(request): 
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # ✅ Append the new task to the global list
            #tasks.append(new_task)
            #request.session["tasks"].append(new_task)
            #request.session.modified = True
            request.session["tasks"]+=[task]
            

            # Redirect back to index page after adding
            return redirect("index2") 
        else:
            # If the form is not valid, re-render with error messages
            return render(request, "task2/add2.html", {
                "form": form
            })
    
    # If GET request, show empty form
    return render(request, "task2/add2.html", {
        "form": NewTaskForm()
    })
