from django.shortcuts import render

# Create your views here.


from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

# from facts import forms
from django.views.generic import TemplateView, ListView, UpdateView

from core.forms import EmployeeForm
from core.models import Employee, City, Region, Job
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import logout as auth_logout



def display_regions(request):

    regions = Region.objects.all()
    cities = City.objects.all()
    return render(request, "core/home_page.html", {'regions': regions, 'cities': cities})


def display_cities(request, name):

    cities = City.objects.filter(region__name=name)
    region = name
    return render(request, "core/cities_page.html", {'cities': cities, 'region':region})


def display_emloyees(request, name):
    q = request.GET.get('job')
    employees = Employee.objects.filter(city__name=name)
    f = []
    city = employees[0].city
    if q:
        f = [y for y in employees if y.job.name == q]
        l = [x.job.name for x in employees if x.job.name == q]
    else:
        f = [y for y in employees]
        l = [x.job.name for x in employees]
    # remove duplications:
    nl = list(dict.fromkeys(l))
    print(f)
    s = []
    for job in nl:
        s.append(l.count(job))
    import json
    return render(request, "core/employees_page.html",
                  {'f': f, 'employees': employees, "city": city, 'nl': json.dumps(nl, ensure_ascii=True),
                   's': json.dumps(s, ensure_ascii=True)})




class EmployeeUpdateView(UpdateView, LoginRequiredMixin):
    form_class = EmployeeForm

    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = '/'

    def get_object(self, queryset=None):
        Employee.objects.get_or_create(
            user=self.request.user
        )
        return self.request.user.employee


def logout(request):
    auth_logout(request)
    return redirect('/')
