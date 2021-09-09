from django.http import HttpResponse

# Create your views here.
import django_grade_compare.settings
from authentication.models import CustomUser

def login(request):
    return HttpResponse("Hello World")