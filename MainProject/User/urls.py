from django.urls import path
from User import views 
app_name="webuser"

urlpatterns = [
    path('userhome/', views.homepageuser,name="userhome"),
    path('userprofile/', views.UserMyProfile,name="userprofile"),  
    path('useredit/', views.EditProfile,name="useredit"), 
    path('userchangepass/', views.UserChangePass,name="userchangepass"),  
    path('usercomp/', views.UserComplaint,name="usercomp"),
    path('userfeed/', views.UserFeedback,name="userfeed"),  
    path('delcomplaint/<int:cid>',views.DelComp,name="delcomplaint"),
    path('servicebook/', views.ServiceBooking,name="servicebook"),
    path('requestedservice/', views.MyServiceBooking,name="requestedservice"),
    path('delservice/<int:sid>',views.DelServ,name="delservice"),
    path('viewbill/<int:bid>', views.ViewServiceBill,name="viewbill"),
    path('viewpay/<int:blid>', views.PaymentService,name="viewpay"),
    
    
    path('products/', views.ProductListView, name='product_list'),
    path('create-checkout-session/<int:pid>/', views.create_checkout_session, name='create_checkout_session'),
    path('my-orders/', views.my_orders, name='my_orders'),  # ✅ Ensure this exists
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),

  # URL pattern for creating an order
    path('create-order/<int:product_id>/', views.create_order, name='create_order'),

    
    path('userewastereq/', views.UserEWaste,name="userewastereq"), 
    path('viewuserewastereq/', views.ViewUserEWaste,name="viewuserewastereq"), 
    path('product/', views.Prodview,name="product"),
    path('logout/', views.logout,name="logout"), 

    # path('create/', views.create_order, name='create_order'),
    # path('success/', views.order_success, name='order_success'),
    # path('my-orders/', views.user_orders, name='user_orders'),
    # path('orders/', views.user_orders, name='user_orders'),  # Add this line
    # path('payment-success/', views.order_success, name='order_success'),
]   

