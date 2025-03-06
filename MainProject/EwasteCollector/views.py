from django.shortcuts import render,redirect
from Admin.models import *
from User.models import Ewastebooking
from EwasteCollector.models import *


# Create your views here.

def EWHome(request):
  if 'eid' in request.session:
    ecol=EwasteCollector.objects.get(id=request.session["eid"])
    return render(request,"EwasteCollector/CollectorHomePage.html",{'data':ecol})   
  else:
        return redirect('guest:Home')  

def ECprofile(request):
  if 'eid' in request.session:
    ecol=EwasteCollector.objects.get(id=request.session["eid"])
    return render(request,"EwasteCollector/EcollectorMyProfile.html",{'data':ecol}) 
  else:
        return redirect('guest:Home') 
 
def CollectorChangePass(request):
    if 'eid' in request.session:
        if request.method=="POST":
            ecolcount=EwasteCollector.objects.filter(id=request.session["eid"],EwasteCollector_password=request.POST.get('txt_curr')).count()
            if ecolcount>0:
                ecol=EwasteCollector.objects.get(id=request.session["eid"],EwasteCollector_password=request.POST.get('txt_curr'))
                ecol.EwasteCollector_password=request.POST.get('txt_new')
                ecol.save()
                return redirect("webcollector:ewastecolhome")
        else:
            return render(request,"EwasteCollector/EcollectorChangePassword.html") 
    else:
        return redirect('guest:Home')     

def ViewAllocatedEC(request):
 if 'eid' in request.session:
    ecol=Assignewastebooking.objects.filter(collector=request.session["eid"])
    return render(request,"EwasteCollector/AllocatedEwasteCollectionRequests.html",{'data':ecol})   
 else:
        return redirect('guest:Home')         

def ConfirmEbook(request,cid):
      if 'eid' in request.session:
        wbook=Assignewastebooking.objects.get(id=cid)  
        wbook.aeb_status=2
        wbook.save()
        return redirect('webcollector:ViewmyAllocEC') 
      else:
        return redirect('guest:Home')

def DeleteEbook(request,cid):
      if 'eid' in request.session:
        eb=Assignewastebooking.objects.get(id=cid) 
        bokid=eb.ewastebooking_id
        sbok=Ewastebooking.objects.get(id=bokid)
        sbok.ewastebooking_status=0
        sbok.save()

        eb.delete()
        return redirect('webcollector:ViewmyAllocEC') 
      else:
        return redirect('guest:Home')

def ConfirmedEWCollection(request):
     if 'eid' in request.session:
        eb=Assignewastebooking.objects.filter(collector=request.session["eid"])
        return render(request,"EwasteCollector/ConfirmedEwasteCollectionReq.html",{'res':eb}) 
     else:
        return redirect('guest:Home')

def Yardselect(request,cid):
     if 'eid' in request.session:
        yar=Yard.objects.all()
        eb=Assignewastebooking.objects.get(id=cid)
        if request.method=="POST":
            yardd=Yard.objects.get(id=request.POST.get('ddl_yard'))
            CollectedEwaste.objects.create(collectedewaste_weight=request.POST.get('txt_weight'),yard=yardd,Ewaste=eb)
            eb.aeb_status=3
            eb.save()
            bokid=eb.ewastebooking_id
            ebok=Ewastebooking.objects.get(id=bokid)
            ebok.ewastebooking_status=2
            ebok.save()
            return redirect('webcollector:viewconfimedeb')
        else:

         return render(request,"EwasteCollector/YardSelection.html",{'res':eb,'y':yar}) 
     else:
        return redirect('guest:Home')
     
    
def logout(request):
    
 del request.session['eid']
 return redirect('guest:Home')

        