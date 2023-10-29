from inertia import render
# Create your views here.


def index(request):
    context={'dev':'Fidel C'}
    return render(request,'Index',context)