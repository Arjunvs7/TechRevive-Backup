from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from Technician.models import Servicebill







# # Create your views here.

#  Create the Checkout View
import stripe
from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from Admin.models import Product  # Import from the Admin app

# Configure Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request, pid):
    # Retrieve the product based on the id passed in the URL
    product = get_object_or_404(Product, id=pid)
    
    # Convert product price (in dollars) to cents (as an integer)
    # For example, if product.price is Decimal('10.00'), amount_in_cents becomes 1000
    amount_in_cents = int(product.price * 100)
    
    if request.method == 'POST':
        try:
            # Create a Stripe Checkout session using the product details and price
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': amount_in_cents,
                        'product_data': {
                            'name': product.Product_name,
                            'description': product.Product_description,
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                # These URLs will be used by Stripe to redirect after payment is processed
                # success_url=request.build_absolute_uri('/payment-success/'),
                # cancel_url=request.build_absolute_uri('/payment-cancel/'),
                success_url=request.build_absolute_uri('/User/payment-success/'),
                cancel_url=request.build_absolute_uri('/User/payment-cancel/'),

            )
            return redirect(session.url)
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)})
    else:
        # Optionally, render a page that confirms the product details before proceeding
        return render(request, 'checkout.html', {'product': product})

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_cancel(request):
    return render(request, 'payment_cancel.html')

# end of new f

from django.shortcuts import render
from Admin.models import Product

def ProductListView(request):
    # Retrieve all products from the Admin app
    products = Product.objects.all()
    return render(request, 'User/ProductListView.html', {'res': products})



def homepageuser(request):
    if 'uid' in request.session:
        user=User.objects.get(id=request.session["uid"])
        return render(request,"User/UserHomePage.html",{'data':user})
    else:
        return redirect('guest:Home')
    

def UserMyProfile(request):
    if 'uid' in request.session:
        user=User.objects.get(id=request.session["uid"])
        return render(request,"User/UserMyProfile.html",{'data':user})
    else:
        return redirect('guest:Home')
    

def EditProfile(request):
    if 'uid' in request.session:
        user=User.objects.get(id=request.session["uid"])
        if request.method=="POST":
            user.user_name=request.POST.get('txt_name')
            user.user_contact=request.POST.get('txt_contact')
            user.user_address=request.POST.get('txt_address')
            user.save()
            return render(request,"User/UserEditProfile.html",{'msg':"Changed Successfully"})
        else:
            return render(request,"User/UserEditProfile.html",{'data':user})
    else:
        return redirect('guest:Home')
    
    
def UserChangePass(request):
    if 'uid' in request.session:
        if request.method=="POST":
            if request.POST.get("txt_new")==request.POST.get("txt_confirm"):
                usercount=User.objects.filter(id=request.session["uid"],user_password=request.POST.get('txt_curr')).count()
                if usercount>0:
                    user=User.objects.get(id=request.session["uid"],user_password=request.POST.get('txt_curr'))
                    user.user_password=request.POST.get('txt_new')
                    user.save()
                    return redirect("webuser:userhome")
            else:
                return render(request,"Guest/UserChangePassword.html",{'msg':" Passwords are not same"})                
        else:
            return render(request,"User/UserChangePassword.html")   
    else:
        return redirect('guest:Home')
         
    
def UserComplaint(request):
    if 'uid' in request.session:
        tech=Technician.objects.all()
        comp=Complaint.objects.filter(user=request.session["uid"])
        if request.method=="POST":
            t=Technician.objects.get(id=request.POST.get('ddl_tech'))
            u=User.objects.get(id=request.session['uid'])
            Complaint.objects.create(complaint_title=request.POST.get('txt_complaint'),complaint_content=request.POST.get('txt_content'),technician=t,user=u)
            return redirect('webuser:usercomp')
        else:
            return render(request,"User/UserComplaints.html",{'tech':tech,'res':comp})
    else:
        return redirect('guest:Home')
    
def UserFeedback(request):
    if 'uid' in request.session:
        if request.method=="POST":
            u=User.objects.get(id=request.session['uid'])
            Feedback.objects.create(feedback_content=request.POST.get('txt_content'),user=u)
            return redirect('webuser:userhome')
        else:
            return render(request,"User/UserFeedback.html")
    else:
        return redirect('guest:Home')
        
    
def DelComp(request,cid):
    if 'uid' in request.session:
        comp=Complaint.objects.get(id=cid)  
        comp.delete()
        return redirect('webuser:usercomp')   
    else:
        return redirect('guest:Home')  


def ServiceBooking(request):
    if 'uid' in request.session:
        cat=Category.objects.all()
        bran=Brand.objects.all()
        u=User.objects.get(id=request.session['uid'])
        if request.method=="POST":
            c=Category.objects.get(id=request.POST.get('ddl_cat'))
            b=Brand.objects.get(id=request.POST.get('ddl_brand'))
            Servicebook.objects.create(Servicebook_details=request.POST.get('txt_details'),Servicebook_address=request.POST.get('txt_address'),category=c,brand=b,user=u)
            return redirect('webuser:servicebook')
        else:
            return render(request,"User/ServiceBooking.html",{'cat':cat,'brand':bran})  
    else:
        return redirect('guest:Home')  
    

def MyServiceBooking(request):
 if 'uid' in request.session:
    serv=Servicebook.objects.filter(user=request.session["uid"])
    return render(request,"User/ViewMyServiceRequests.html",{'res':serv})  
 else:
        return redirect('guest:Home')  

def DelServ(request,sid):
    if 'uid' in request.session:
        serv=Servicebook.objects.get(id=sid)  
        serv.delete()
        return redirect('webuser:requestedservice')  
    else:
        return redirect('guest:Home')   

def ViewServiceBill(request,bid):
    if 'uid' in request.session:
        request.session["bookingid"]=bid
        asbid=Assignservicebook.objects.get(servicebooking=bid)
        servbill=Servicebill.objects.get(assignedservicebooking=asbid)
        return render(request,"User/ViewBill.html",{'data':servbill})
    else:
        return redirect('guest:Home')   


def PaymentService(request,blid):
    if 'uid' in request.session:
        sbill=Servicebill.objects.get(id=blid)
        sbook=Servicebook.objects.get(id=request.session["bookingid"])
        if request.method=="POST":
            sbook.payment_status=1
            sbook.save()
            return redirect('webuser:requestedservice')
        else:
            return render(request,"User/Payment.html")
    else:
        return redirect('guest:Home')   

    # asbid=Assignservicebook.objects.get(servicebooking=bid)
    # servbill=Servicebill.objects.get(assignedservicebooking=asbid)

def UserEWaste(request):
    if 'uid' in request.session:
        if request.method=="POST":
            u=User.objects.get(id=request.session['uid'])
            Ewastebooking.objects.create(ewastebooking_details=request.POST.get('txt_details'),ewastebooking_collectionpoint=request.POST.get('txt_collection'),user=u)
            return render(request,"User/EwasteRequest.html",{'msg':"Submitted Successfully"})  
            
        
        else:
            return render(request,"User/EwasteRequest.html") 
    else:
        return redirect('guest:Home') 
    
def ViewUserEWaste(request):
    if 'uid' in request.session:
        ereq=Ewastebooking.objects.filter(user=request.session["uid"])
        return render(request,"User/ViewMyERequests.html",{'res':ereq}) 
    else:
        return redirect('guest:Home')
    
def Prodview(request):
 if 'uid' in request.session:
    pro=Product.objects.all()
    return render(request,"User/ProductListView.html",{'res':pro})  
 else:
        return redirect('guest:Home')      
         



def logout(request):
    
    del request.session['uid']
    return redirect('guest:Home')
    