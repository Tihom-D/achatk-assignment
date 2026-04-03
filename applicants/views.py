from django.shortcuts import render, redirect
from .models import Applicant
from .forms import ApplicantForm

def home(request):
    applicants = Applicant.objects.all()
    return render(request, 'applicants/home.html', {'applicants': applicants})

def apply(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ApplicantForm()

    return render(request, 'applicants/apply.html', {'form': form})


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Applicant
from .serializers import ApplicantSerializer

@api_view(['GET'])
def get_applicants(request):
    applicants = Applicant.objects.all()
    serializer = ApplicantSerializer(applicants, many=True)
    return Response(serializer.data)