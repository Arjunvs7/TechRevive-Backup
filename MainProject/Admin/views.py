from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Technician.models import Servicebill
from Guest.models import User
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
import random
from Admin.models import Assignservicebook, Servicebook  






def delete_completed_service(request, sid):
    if 'aid' in request.session:  # Check if admin is logged in
        try:
            assigned_service = Assignservicebook.objects.get(id=sid)
            # Get the related service booking, which might be None
            service_booking = assigned_service.servicebooking  

            # Delete the service booking if it exists
            if service_booking:
                service_booking.delete()
            # Delete the assigned service regardless
            assigned_service.delete()

            return redirect('webadmin:viewcompleted')  # Redirect to completed services page
        except Assignservicebook.DoesNotExist:
            return redirect('webadmin:viewcompleted')  # If service does not exist, still redirect
    else:
        return redirect('guest:Home')  # Redirect to home if not logged in


# def delete_completed_service(request, sid):
#     if 'aid' in request.session:  # Check if admin is logged in
#         try:
#             assigned_service = Assignservicebook.objects.get(id=sid)

#             # Get the related service booking
#             service_booking = assigned_service.servicebooking  

#             # Delete both entries
#             service_booking.delete()
#             assigned_service.delete()

#             return redirect('webadmin:viewcompleted')  # Redirect to completed services page
#         except Assignservicebook.DoesNotExist:
#             return redirect('webadmin:viewcompleted')  # If service does not exist, still redirect
#     else:
#         return redirect('guest:Home')  # Redirect to home if not logged in

    
# Create your views here.

# def district(request):
#     if 'aid' in request.session:
#         dis=District.objects.all()
#         if request.method=="POST":
#             District.objects.create(district_name=request.POST.get('txt_dname'))
#             return render(request,"Admin/District.html",{'res':dis})
#         else:
#             return render(request,"Admin/District.html",{'res':dis})
#     else:
#         return redirect('guest:Home')  

def deldis(request,did):
     if 'aid' in request.session:
        dis=District.objects.get(id=did)
        dis.delete()
        return redirect("webadmin:district")   
     else:
        return redirect('guest:Home')  

def pl(request):
     if 'aid' in request.session:
        di=District.objects.all()
        pl=Place.objects.all()
        if request.method=="POST":
         p=Place.objects.filter(place_name__icontains=request.POST.get("txt_pname"))
         if p:
             return render(request,"Admin/Place.html",{'di':di,'pl':pl,'msg':"Data already exists"})
         else:
            dis=District.objects.get(id=request.POST.get('ddl_dis'))
            Place.objects.create(place_name=request.POST.get('txt_pname'),district=dis)
            return render(request,"Admin/Place.html",{'di':di,'pl':pl,'msg':"Data Inserted"})
        else:
            return render(request,"Admin/Place.html",{'di':di,'pl':pl})
     else:
        return redirect('guest:Home') 
    
def DelPlace(request,pid):
    if 'aid' in request.session:
        place=Place.objects.get(id=pid)  
        place.delete()
        return redirect('webadmin:place') 
    else:
        return redirect('guest:Home')    

def category(request):
    if 'aid' in request.session:
        cat=Category.objects.all()
        if request.method=="POST":
         c=Category.objects.filter(category_name__icontains=request.POST.get("txt_cname"))
         if c:
             return render(request,"Admin/Category.html",{'result':cat,'msg':"Data already exists"})
         else:            
            Category.objects.create(category_name=request.POST.get('txt_cname'))
            return render(request,"Admin/Category.html",{'result':cat,'msg':"Data Inserted"})
        else:
            return render(request,"Admin/Category.html",{'result':cat})  
    else:
        return redirect('guest:Home')    

def delcat(request,catid):
    if 'aid' in request.session:
        cate=Category.objects.get(id=catid) 
        cate.delete()
        return redirect("webadmin:category") 
    else:
        return redirect('guest:Home')  

def addbrand(request):
    if 'aid' in request.session:
        br=Brand.objects.all()
        if request.method=="POST":
         b=Brand.objects.filter(brand_name__icontains=request.POST.get("txt_bname"))
         if b:
             return render(request,"Admin/Brand.html",{'result':br,'msg':"Data already exists"})
         else:               
            Brand.objects.create(brand_name=request.POST.get('txt_bname'))
            return render(request,"Admin/Brand.html",{'result':br,'msg':"Data Inserted"})
        else:
            return render(request,"Admin/Brand.html",{'result':br}) 
    else:
        return redirect('guest:Home')    

def delbrand(request,bid):
    if 'aid' in request.session:
        brand=Brand.objects.get(id=bid) 
        brand.delete()
        return redirect("webadmin:brand")  
    else:
        return redirect('guest:Home')  

def Userlist(request):
     if 'aid' in request.session:
        newuser=User.objects.all()
        return render(request,"Admin/Userlist.html",{'data':newuser})  
     else:
        return redirect('guest:Home')   
  
def DelUser(request,uid):
     if 'aid' in request.session:
        user=User.objects.get(id=uid)  
        user.delete()
        return redirect('webadmin:userlist') 
     else:
        return redirect('guest:Home') 

# def techreg(request):
#      if 'aid' in request.session:
#         cat=Category.objects.all()
#         tech_list = Technician.objects.all()  # Fetch all technicians from DB
#         if request.method=="POST":
#          t=Technician.objects.filter(technician_email__icontains=request.POST.get("txt_email"))
#          if t:
#              return render(request,"Admin/Technicianregistration.html",{'cat':cat,'msg':"Email id already in use"})
#          else:                
#             c=Category.objects.get(id=request.POST.get('ddl_cat'))
#             Technician.objects.create(technician_name=request.POST.get('txt_name'),technician_gender=request.POST.get('rad_gender'),technician_contact=request.POST.get('txt_num'),technician_email=request.POST.get('txt_email'),technician_password=request.POST.get('txt_pass'),technician_photo=request.FILES.get('file_photo'),technician_experience=request.POST.get('txt_experience'),technician_address=request.POST.get('txt_address'),category=c)
#             return render(request,"Admin/Technicianregistration.html",{'cat':cat,'msg':"Technician Registered"})
#         else:
#             return render(request,"Admin/Technicianregistration.html",{'cat':cat})
#      else:
#         return redirect('guest:Home') 
def techreg(request):
    if 'aid' in request.session:
        cat = Category.objects.all()
        tech_list = Technician.objects.all()  # Fetch all technicians from DB
        if request.method == "POST":
            t = Technician.objects.filter(technician_email__icontains=request.POST.get("txt_email"))
            if t:
                return render(request, "Admin/Technicianregistration.html", {
                    'cat': cat,
                    'tech_list': tech_list,
                    'msg': "Email id already in use"
                })
            else:                
                c = Category.objects.get(id=request.POST.get('ddl_cat'))
                Technician.objects.create(
                    technician_name=request.POST.get('txt_name'),
                    technician_gender=request.POST.get('rad_gender'),
                    technician_contact=request.POST.get('txt_num'),
                    technician_email=request.POST.get('txt_email'),
                    technician_password=request.POST.get('txt_pass'),
                    technician_photo=request.FILES.get('file_photo'),
                    technician_experience=request.POST.get('txt_experience'),
                    technician_address=request.POST.get('txt_address'),
                    category=c
                )
                # Refresh the technician list after registration
                tech_list = Technician.objects.all()
                return render(request, "Admin/Technicianregistration.html", {
                    'cat': cat,
                    'tech_list': tech_list,
                    'msg': "Technician Registered"
                })
        else:
            return render(request, "Admin/Technicianregistration.html", {
                'cat': cat,
                'tech_list': tech_list
            })
    else:
        return redirect('guest:Home')

        
        # TECHnician deletion
def deltechnician(request, tid):
    if 'aid' in request.session:
        technician = Technician.objects.get(id=tid)
        technician.delete()
        return redirect('webadmin:technician')
    else:
        return redirect('guest:Home')

# def deltechnician(request, tid):
#     if 'aid' in request.session:
#         try:
#             technician = Technician.objects.get(id=tid)
#             technician.delete()
#             return redirect('webadmin:technicianlist')  # Redirect to the technician list page
#         except Technician.DoesNotExist:
#             return redirect('webadmin:technicianlist')  # Optionally handle the error case
#     else:
#         return redirect('guest:Home')

def Homepageadmin(request):
 if 'aid' in request.session:
    admin=Admin.objects.get(id=request.session["aid"])
    usercount=User.objects.all().count()
    techcount=Technician.objects.all().count()
    eccout=EwasteCollector.objects.all().count()
    scount=Servicebook.objects.filter(Servicebook_status=4).count()
    return render(request,"Admin/Adminhomepage.html",{'data':admin,'uc':usercount,'tc':techcount,'ec':eccout,'sc':scount})    
 else:
        return redirect('guest:Home')    

def ViewUserComplaints(request):
  if 'aid' in request.session:
    comp=Complaint.objects.filter(complaint_status=0)
    return render(request,"Admin/ViewComplaints.html",{'res':comp})  
  else:
        return redirect('guest:Home')   

def ComplaintReplyD(request,cid):
  if 'aid' in request.session:
    compl=Complaint.objects.get(id=cid)  
    if request.method=="POST":
        compl.complaint_reply=request.POST.get('txt_reply')
        compl.complaint_status=1
        compl.save()
        return redirect('webadmin:viewucomp') 
    else:
     return render(request,"Admin/Complaintreply.html") 
  else:
        return redirect('guest:Home')   
    
def ViewUserFeedbacks(request):
   if 'aid' in request.session:
    feedb=Feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{'res':feedb})    
   else:
        return redirect('guest:Home')  

def DelFeedback(request,fid):
     if 'aid' in request.session:
        feedb=Feedback.objects.get(id=fid)  
        feedb.delete()
        return redirect('webadmin:viewufeed') 
     else:
        return redirect('guest:Home')  

def ViewServiceBooking(request):
 if 'aid' in request.session:
    serv=Servicebook.objects.filter(Servicebook_status=0)
    return render(request,"Admin/ViewUserService.html",{'res':serv})  
 else:
        return redirect('guest:Home')  

def DelServ(request,sid):
     if 'aid' in request.session:
        serv=Servicebook.objects.get(id=sid)  
        serv.delete()
        return redirect('webadmin:viewaccservice') 
     else:
        return redirect('guest:Home') 

def AcceptServ(request,sid):
     if 'aid' in request.session:
        serv=Servicebook.objects.get(id=sid)  
        serv.Servicebook_status=1
        serv.save()
        return redirect('webadmin:viewservice') 
     else:
        return redirect('guest:Home') 

def RejectServ(request,sid):
      if 'aid' in request.session:
        serv=Servicebook.objects.get(id=sid)  
        serv.Servicebook_status=2
        serv.save() 
        return redirect('webadmin:viewservice')
      else:
        return redirect('guest:Home')  

def ViewAcceptedServiceBooking(request):
  if 'aid' in request.session:
    serv=Servicebook.objects.filter(Q(Servicebook_status=1) | Q(Servicebook_status=3))
    return render(request,"Admin/ViewAcceptedService.html",{'res':serv})
  else:
        return redirect('guest:Home')      

def ViewRejectedServiceBooking(request):
 if 'aid' in request.session:
    serv=Servicebook.objects.filter(Servicebook_status=2)
    return render(request,"Admin/ViewRejectedService.html",{'res':serv}) 
 else:
        return redirect('guest:Home')    

def AssignServiceBooking(request,aid):
     if 'aid' in request.session:
        serv=Servicebook.objects.get(id=aid)
        tech=Technician.objects.all()
        if request.method=="POST":
            t=Technician.objects.get(id=request.POST.get('ddl_tech'))
            Assignservicebook.objects.create(technician=t,servicebooking=serv,asb_status=1)
            serv.Servicebook_status=3
            serv.save()
            return redirect('webadmin:viewaccservice')
        else:
         return render(request,"Admin/AssignServiceBooking.html",{'data':serv,'tech':tech})
     else:
        return redirect('guest:Home')   
    
def ViewCompletedService(request):
 if 'aid' in request.session:
    servd=Assignservicebook.objects.all()
    return render(request,"Admin/ViewCompletedService.html",{'res':servd})  
 else:
        return redirect('guest:Home')      

def DelServC(request,sid):
     if 'aid' in request.session:
        serv=Assignservicebook.objects.get(id=sid)  
        servid=serv.servicebooking
        servb=Servicebook.objects.get(id=servid)
        servb.delete()
        serv.delete()
        return redirect('webadmin:viewcompleted') 
     else:
        return redirect('guest:Home') 


 
def AlertEm(request,sid):
  if 'aid' in request.session:
    servd=Assignservicebook.objects.get(id=sid) 
    email=servd.servicebooking.user.user_email
    name=servd.servicebooking.user.user_name
    send_mail( 
                'Respected Sir/Madam' +name, #subject 
                "Sorry your payment status is pending.", #body 
                settings.EMAIL_HOST_USER, 
                [email],  )
    return redirect('webadmin:viewcompleted') 
  else:
        return redirect('guest:Home') 
  
def ViewEwasteRequest(request):
 if 'aid' in request.session:
    ereq=Ewastebooking.objects.filter(ewastebooking_status=0)
    return render(request,"Admin/UserCollectionRequest.html",{'res':ereq})  
 else:
        return redirect('guest:Home') 

def CollectorReg(request):
    if 'aid' in request.session:
        coll=EwasteCollector.objects.all()
        if request.method=="POST":
         elec=EwasteCollector.objects.filter(EwasteCollector_email__icontains=request.POST.get("txt_email"))
         if elec:
             return render(request,"Admin/EwasteCollectorRegistration.html",{'result':coll,'msg':"Email id already in use"})
         else:              
            EwasteCollector.objects.create(EwasteCollector_name=request.POST.get('txt_name'),EwasteCollector_contact=request.POST.get('txt_num'),EwasteCollector_email=request.POST.get('txt_email'),EwasteCollector_password=request.POST.get('txt_pass'),EwasteCollector_photo=request.FILES.get('file_photo'),EwasteCollector_proof=request.FILES.get('file_lphoto'),EwasteCollector_vehicleno=request.POST.get('txt_vnumber'),EwasteCollector_vehiclemodel=request.POST.get('txt_vname'),EwasteCollector_vehicleimg=request.FILES.get('file_vphoto'))
            return render(request,"Admin/EwasteCollectorRegistration.html",{'result':coll,'msg':"Registered Successfully"})
        else:
            return render(request,"Admin/EwasteCollectorRegistration.html",{'result':coll})
    else:
        return redirect('guest:Home')   
    
    
def DelEcollector(request,eid):
     if 'aid' in request.session:
        ecol=EwasteCollector.objects.get(id=eid)  
        ecol.delete()
        return redirect('webadmin:ewastecollector') 
     else:
        return redirect('guest:Home')       

def AssignCollector(request,aid):
     if 'aid' in request.session:
        ebook=Ewastebooking.objects.get(id=aid)
        ecol=EwasteCollector.objects.all()
        if request.method=="POST":
            ec=EwasteCollector.objects.get(id=request.POST.get('ddl_collector'))
            Assignewastebooking.objects.create(collector=ec,ewastebooking=ebook,aeb_status=1)
            ebook.ewastebooking_status=1
            ebook.save()
            return redirect('webadmin:ewastecollection')
        else:
         return render(request,"Admin/AssignEwasteCollection.html",{'data':ebook,'eco':ecol})
     else:
        return redirect('guest:Home')
    
    #Adding yard

# def YardAdd(request):
#     if 'aid' in request.session:
#         yar=Yard.objects.all()
#         if request.method=="POST":
#          y=Yard.objects.filter(yard_name__icontains=request.POST.get("txt_yname"))
#          if y:
#              return render(request,"Admin/AddYard.html",{'res':yar,'msg':"Data already exists"})
#          else:     
#             Yard.objects.create(yard_name=request.POST.get('txt_yname'))
#             return render(request,"Admin/AddYard.html",{'res':yar,'msg':"Data Inserted"})
#         else:
#          return render(request,"Admin/AddYard.html",{'res':yar})
#     else:
#         return redirect('guest:Home')

from django.shortcuts import render, redirect
from .models import District, Yard

def YardAdd(request):
    msg = ""
    di = District.objects.all()  # Fetch all districts
    if request.method == "POST":
        district_id = request.POST.get("ddl_dis")
        yard_name = request.POST.get("txt_yname")

        if district_id and yard_name:
            district = District.objects.get(id=district_id)
            Yard.objects.create(yard_name=yard_name, district=district)
            msg = "Yard added successfully!"
        else:
            msg = "Please select a district and enter a yard name!"

    res = Yard.objects.all()
    return render(request, "Admin/AddYard.html", {"di": di, "res": res, "msg": msg})


def delyardA(request,did):
    if 'aid' in request.session:
        y=Yard.objects.get(id=did)
        y.delete()
        return redirect("webadmin:Yardadd")  
    else:
        return redirect('guest:Home')
     
def TypeAd(request):
    if 'aid' in request.session:
        ty=Type.objects.all()
        if request.method=="POST":
         pty=Type.objects.filter(type_name__icontains=request.POST.get("txt_pname"))
         if pty:
             return render(request,"Admin/Type.html",{'res':ty,'msg':"Data already exists"})
         else:                 
            Type.objects.create(type_name=request.POST.get('txt_pname'))
            return render(request,"Admin/Type.html",{'res':ty,'msg':"Data Inseted"})
        else:
         return render(request,"Admin/Type.html",{'res':ty})
    else:
        return redirect('guest:Home')

def deltype(request,did):
     if 'aid' in request.session:
        ty=Type.objects.get(id=did)
        ty.delete()
        return redirect("webadmin:Typeadd")   
     else:
        return redirect('guest:Home') 



from decimal import Decimal
from django.shortcuts import redirect, render, get_object_or_404
from Admin.models import Product, Type

def ProductAdd(request):
    if 'aid' in request.session:
        typr = Type.objects.all()
        if request.method == "POST":
            ty = get_object_or_404(Type, id=request.POST.get('ddl_type'))
            # Retrieve the price string from the form; default to '0.00' if not provided.
            price_str = request.POST.get('txt_price', '0.00')
            try:
                price_value = Decimal(price_str)
            except Exception:
                price_value = Decimal("0.00")
            
            Product.objects.create(
                Product_name=request.POST.get('txt_pname'),
                product_image=request.FILES.get('file_photo'),
                Product_description=request.POST.get('txt_pdescp'),
                type=ty,
                price=price_value  # Here, price_value is defined above.
            )
            return redirect('webadmin:prodadd')
        else:
            return render(request, "Admin/AddProduct.html", {'typ': typr})
    else:
        return redirect('guest:Home')

# def ProductAdd(request):
#     if 'aid' in request.session:
#         typr=Type.objects.all()
#         if request.method=="POST":
#             ty=Type.objects.get(id=request.POST.get('ddl_type'))
#             Product.objects.create(Product_name=request.POST.get('txt_pname'),product_image=request.FILES.get('file_photo'),Product_description=request.POST.get('txt_pdescp'),type=ty,price=price_value)
#             return redirect('webadmin:prodadd')
#         else:
#             return render(request,"Admin/AddProduct.html",{'typ':typr})
#     else:
#         return redirect('guest:Home') 
    
    
def ProductView(request):
 if 'aid' in request.session:
    pro=Product.objects.all()
    return render(request,"Admin/ViewProducts.html",{'res':pro})   
 else:
        return redirect('guest:Home')  

def GalleryView(request,cid):
    if 'aid' in request.session:
        p=Product.objects.get(id=cid)
        if request.method=="POST":
            Gallery.objects.create(gallery_image=request.FILES.get('file_photo'),product=p)
            return redirect('webadmin:viewprod')
        else:

         return render(request,"Admin/AddGallery.html",{'res':p})   
    else:
        return redirect('guest:Home')   

def RemoveProduct(request,did):
     if 'aid' in request.session:
        pr=Product.objects.get(id=did)
        pr.delete()
        return redirect("webadmin:viewprod")     
     else:
        return redirect('guest:Home')      
     
def logout(request):
    
 del request.session['aid']
 return redirect('guest:Home')    

def BillReport(request):
    if 'aid' in request.session:
        if request.method=="POST":
            frdate=request.POST.get('frdate')
            todate=request.POST.get('todate')
            data=Servicebill.objects.filter(servicebill_date__gte=frdate,servicebill_date__lte=todate)
            return render(request,"Admin/ReportOnBill.html",{'data':data,'f':frdate,'t':todate}) 
        return render(request,"Admin/ReportOnBill.html")
    else:
        return redirect('guest:Home')   
    
def ServiceReport(request):
    if 'aid' in request.session:
        if request.method=="POST":
            frdate=request.POST.get('frdate')
            todate=request.POST.get('todate')
            data=Servicebook.objects.filter(Servicebook_date__gte=frdate,Servicebook_date__lte=todate,Servicebook_status=4,payment_status=1)
            return render(request,"Admin/ReportOnCompletedServices.html",{'data':data,'f':frdate,'t':todate}) 
        return render(request,"Admin/ReportOnCompletedServices.html")
    else:
        return redirect('guest:Home')   
    
def EwasteBReport(request):
    if 'aid' in request.session:
        if request.method=="POST":
            frdate=request.POST.get('frdate')
            todate=request.POST.get('todate')
            data=Ewastebooking.objects.filter(ewastebooking_date__gte=frdate,ewastebooking_date__lte=todate,ewastebooking_status=2)
            return render(request,"Admin/ReportOnEwastebooking.html",{'data':data,'f':frdate,'t':todate}) 
        return render(request,"Admin/ReportOnEwastebooking.html")
    else:
        return redirect('guest:Home')       
    
def district(request):
      if 'aid' in request.session:
        
        dist=District.objects.all()  
        if request.method=='POST':
            d=District.objects.filter(district_name__icontains=request.POST.get("txt_dname"))

            if d:
                return render(request,"Admin/District.html",{'res':dist,'msg':"Data already exists"})
            else:
                District.objects.create(district_name=request.POST.get('txt_dname'))
                return render(request,"Admin/District.html",{'res':dist,'msg':"Data Inserted"})
        else:
            return render(request,"Admin/District.html",{'res':dist})    
      else:
          return redirect('guest:Home')
      

def delete_complaint(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    complaint.delete()
    
    # Redirect to the correct complaint listing page
    return redirect('webadmin:view_complaints')  # Ensure this is the correct URL name

def view_complaints(request):  # Ensure this function exists
    complaints = Complaint.objects.all()
    return render(request, 'Admin/ViewComplaints.html', {'res': complaints})


# from django.db.models import Sum
# from django.db.models.functions import TruncMonth
# from django.http import JsonResponse  # Use JsonResponse instead of DRF Response
# from django.shortcuts import render
# from User.models import Order  # Ensure correct import

# def monthly_sales(request):
#     sales_data = (
#         Order.objects
#         .annotate(month=TruncMonth('order_date'))  # Group by month
#         .values('month')
#         .annotate(total_sales=Sum('total_amount'))  # Sum total sales
#         .order_by('month')
#     )

#     # Convert queryset to list of dictionaries with formatted dates
#     sales_list = [
#         {'month': entry['month'].strftime('%Y-%m'), 'total_sales': entry['total_sales']}
#         for entry in sales_data
#     ]

#     return JsonResponse(sales_list, safe=False)  # Use JsonResponse instead of DRF's Response

# def sales_chart(request):
#     return render(request, "Admin/Saleschart.html")

from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.shortcuts import render
from User.models import Order  # Ensure correct import

def monthly_sales(request):
    sales_data = (
        Order.objects
        .annotate(month=TruncMonth('created_at'))  # ✅ Group by month
        .values('month')
        .annotate(total_sales=Sum('total_price'))  # ✅ Sum sales per month
        .order_by('month')
    )

    # Convert queryset to list with formatted month strings 
    sales_list = [
        {'month': entry['month'].strftime('%Y-%m'), 'total_sales': float(entry['total_sales'] or 0)}
        for entry in sales_data
    ]

    return JsonResponse(sales_list, safe=False)  # ✅ Return JSON response

from django.shortcuts import render, reverse

def sales_chart(request):
    return render(request, "Admin/Saleschart.html")


from django.db.models import Sum
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from django.http import JsonResponse
from django.shortcuts import render
from User.models import Order

def sales_data(request):
    filter_type = request.GET.get('filter', 'month')  # Default: month

    if filter_type == 'day':
        sales_data = (
            Order.objects
            .annotate(period=TruncDay('created_at'))
            .values('period')
            .annotate(total_sales=Sum('total_price'))
            .order_by('period')
        )
    elif filter_type == 'week':
        sales_data = (
            Order.objects
            .annotate(period=TruncWeek('created_at'))
            .values('period')
            .annotate(total_sales=Sum('total_price'))
            .order_by('period')
        )
    else:  # Default: month
        sales_data = (
            Order.objects
            .annotate(period=TruncMonth('created_at'))
            .values('period')
            .annotate(total_sales=Sum('total_price'))
            .order_by('period')
        )

    # Convert queryset to list with formatted date strings
    sales_list = [
        {'period': entry['period'].strftime('%Y-%m-%d' if filter_type == 'day' else '%Y-%m'), 
         'total_sales': float(entry['total_sales'] or 0)}
        for entry in sales_data
    ]

    return JsonResponse(sales_list, safe=False)

def sales_chart(request):
    return render(request, "Admin/Saleschart.html")

def report(request):
    return render(request, "Admin/Report.html")

def bill_report(request):
    return render(request, 'Admin/ReportOnBill.html')

def ewaste_report(request):
    return render(request, 'Admin/ReportOnCompletedServices.html')

def completed_service(request):
    return render(request, 'Admin/ReportOnEwastebooking.html')

def sales_report(request):
    return render(request, 'Admin/Saleschart.html')