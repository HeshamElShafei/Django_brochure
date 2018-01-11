from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from functions import findall,finddata,savedata,updatedata,deldata,findallif,findallexcept
from .models import ClubSignUp
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
	
	return render(request, 'clubs/home.html')

def information(request):
	return render(request, 'clubs/information.html')

def locations(request):
	return render(request, 'clubs/locations.html')

def dubai(request):
	return render(request, 'clubs/dubai.html')

def albarshamixed(request):
	return render(request, 'clubs/albarshamixed.html')

def reefmall(request):
	return render(request, 'clubs/reefmall.html')

def ibnbattuta(request):
	return render(request, 'clubs/ibnbattuta.html')

def businessvillagediera(request):
	return render(request, 'clubs/businessvillagediera.html')

def albarshamixedmembership(request):
	return render(request, 'clubs/albarshamixed_membership.html')

def albarshamixedoptions(request):
	return render(request, 'clubs/albarshamixed_options.html')

def register(request):
	return render(request, 'clubs/register.html')

def reg_store(request):
    if request.method == 'POST':
      name = request.POST['name']
      number = request.POST['number']
      club_name = request.POST['club_name']
      membership = request.POST['membership']
      option = request.POST['option']
      data0 = {"p_name":name, "p_number": number, "p_club_name":club_name, "p_membership":membership, "p_option":option}
      print data0
      res = finddata(ClubSignUp,data0)
      if res == None:
         data = {"p_membership":membership,"p_number":number,"p_name":name,"p_option":option,"p_club_name":club_name}
         res2 = savedata(ClubSignUp, name, number, club_name, membership, option)
         print data 
         if res2 == 1:
            return render(request, 'clubs/home.html')
         else:
            return HttpResponse('<html><script type="text/javascript">alert("Store into db fail!register fail!"); window.location="/"</script></html>')
      else:
         return HttpResponse('<html><script type="text/javascript">alert("The patient has existed!register fail!"); window.location="/patients/"</script></html>')
    return HttpResponse("reg_store")


