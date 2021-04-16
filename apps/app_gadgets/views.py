from django.shortcuts import render
from .forms import AddToolForm
from django.contrib.auth.decorators import login_required
from .models import TechBox
# Create your views here.

@login_required
def addtool_view(request):
    form = AddToolForm()
    if request.method == "POST":
        form = AddToolForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "app_gadgets/tooladded.html")

    return render(request, "app_gadgets/addtool.html", context={'form': form})


@login_required
def tool_list(request):
    # import pdb;pdb.set_trace()
    data = TechBox.objects.all()
    return render(request, "app_gadgets/toollist.html", context={'data': data})

