from django.urls import path
from Admin import views 
app_name="webadmin"
from .views import monthly_sales, sales_chart
from Admin.views import sales_chart ,sales_data




urlpatterns = [
    path('district/', views.district,name="district"),
    path('del/<int:did>', views.deldis,name="deldis"),
    path('place/', views.pl,name="place"),
    path('delplace/<int:pid>',views.DelPlace,name="delplace"),
    path('category/', views.category,name="category"),
    path('cat/<int:catid>', views.delcat,name="delcat"),
    path('brand/', views.addbrand,name="brand"),
    path('brand/<int:bid>', views.delbrand,name="delbrand"),
    path('userlist/', views.Userlist,name="userlist"),
    path('deluser/<int:uid>',views.DelUser,name="deluser"),
    path('technician/', views.techreg,name="technician"),
    path('deltechnician/<int:tid>/', views.deltechnician, name="deltechnician"),

    path('view_complaints/', views.ViewUserComplaints, name='view_complaints'),  # Use the correct function name
    path('delete_complaint/<int:id>/', views.delete_complaint, name='delete_complaint'),

    path('adminhome/', views.Homepageadmin,name="adminhome"),
    path('viewucomp/', views.ViewUserComplaints,name="viewucomp"),  
    path('compreply/<int:cid>',views.ComplaintReplyD,name="compreply"),
    path('viewufeed/', views.ViewUserFeedbacks,name="viewufeed"),
    path('delfeed/<int:fid>',views.DelFeedback,name="delfeed"),
    path('viewservice/', views.ViewServiceBooking,name="viewservice"),
    path('delservice/<int:sid>',views.DelServ,name="delservice"),
    path('accservice/<int:sid>',views.AcceptServ,name="accservice"),
    path('rejservice/<int:sid>',views.RejectServ,name="rejservice"),
    path('viewaccservice/', views.ViewAcceptedServiceBooking,name="viewaccservice"),
    path('viewrejservice/', views.ViewRejectedServiceBooking,name="viewrejservice"),
    path('assignserv/<int:aid>', views.AssignServiceBooking,name="assignserv"),
    path('viewcompleted/', views.ViewCompletedService,name="viewcompleted"),
    path('delcservice/<int:sid>',views.DelServC,name="delcservice"),
    path('delete-completed-service/<int:sid>/', views.delete_completed_service, name="delete_completed_service"),

    path('alertemail/<int:sid>',views.AlertEm,name="alertemail"),
    path('ewastecollection/', views.ViewEwasteRequest,name="ewastecollection"),
    path('ewastecollector/', views.CollectorReg,name="ewastecollector"),
    path('delewastec/<int:eid>',views.DelEcollector,name="delewastec"),
    path('assignewastecollector/<int:aid>', views.AssignCollector,name="assignewastecollector"),
    path('Yardadd/', views.YardAdd,name="Yardadd"),
    path('delyard/<int:did>', views.delyardA,name="delyard"),
    path('Typeadd/', views.TypeAd,name="Typeadd"),
    path('deltyp/<int:did>', views.deltype,name="deltyp"),
    path('prodadd/', views.ProductAdd,name="prodadd"),
    path('viewprod/', views.ProductView,name="viewprod"),
    path('viewgal/<int:cid>', views.GalleryView,name="viewgal"),
    path('removprod/<int:did>', views.RemoveProduct,name="removprod"),
    path('repbill/', views.BillReport,name="repbill"),
    path('servbrep/', views.ServiceReport,name="servbrep"),
    path('ewastebrep/', views.EwasteBReport,name="ewastebrep"),

    path('api/monthly_sales/', monthly_sales, name='monthly_sales'),  # ✅ API for sales data
    path('sales-chart/', sales_chart, name='sales-chart'),  # ✅ Page to display the graph

    path('sales-chart/', sales_chart, name='sales-chart'),
    path('api/sales-data/', sales_data, name='sales-data'),  # API for sales data

    path('report/', views.report, name='report'),

    path('bill-report/', views.bill_report, name='bill_report'),
    path('ewaste-report/', views.ewaste_report, name='ewaste_report'),
    path('completed-service/', views.completed_service, name='completed_service'),
    path('sales-report/', views.sales_report, name='sales_report'),
    


     path('logout/', views.logout,name="logout"), 
]  