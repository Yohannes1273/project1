


from django.shortcuts import render,redirect

# Create your views here.
tasks=["foo","bar","baz"]

def index(request):
    return render(request,"tasks/index.html",{
        "tasks":tasks
        
    })
def add(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task: 
            tasks.append(task)
            return redirect("index")  # go back to the task list
    return render(request, "tasks/add.html")
def add2(request):
    return render(request, "tasks/add2.html")
    