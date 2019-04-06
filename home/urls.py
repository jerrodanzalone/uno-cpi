from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [

   path('campusHome',views.campusHome, name='campusHome'),
   path('CommunityHome',views.CommunityHome, name='CommunityHome'),
   path('partners/',views.partners,name='partners'),
   path('map', views.countyData, name='map'),
   path('definitions',views.Definitions,name='Definitions'),
   path('registerCampusPartnerUser/', views.registerCampusPartnerUser, name='registerCampusPartnerUser'),
   path('registerCommunityPartnerUser/', views.registerCommunityPartnerUser, name='registerCommunityPartnerUser'),
   path('signupuser/registerCampusPartnerUser/', views.registerCampusPartnerUser, name='registerCampusPartnerUser'),
   path('signupuser/registerCommunityPartnerUser/', views.registerCommunityPartnerUser,name='registerCommunityPartnerUser'),
   path('signup/', views.signup, name='signup'),
   path('signupuser/', views.signupuser, name='signupuser'),
   path('uploadProject/', views.upload_project, name='upload_project'),
   path('uploadCommunity/', views.upload_community, name='upload_community'),
   path('uploadCampus/', views.upload_campus, name='upload_campus'),
   path('uploadIncome/', views.upload_income, name='upload_income'),
   path('missionchart/', views.missionchart, name='missionchart'),
   path('projectInfo/', views.project_partner_info, name='project_partner_info'),
   path('engageType/', views.engagement_info, name='engagement_info'),
   path('engagementtypechart2/' , views.EngagementType_Chart, name = 'EngagementType_Chart'),
   path('countProjectCP/', views.unique_count, name='unique_count'),
   path('AdminHome/', views.AdminHome , name= 'adminhome'),
   path('Adminframe/', views.Adminframe, name='Adminframe'),
   path('recentchanges/', views.recentchanges, name='recentchanges' ),
   path('Contactus',views.Contactus,name='Contactus'),
   path('thanks/', views.thanks, name='thanks'),
   path('projectMap',views.googleprojectdata, name='googleprojectmap'),
   path('legislativeDistrict',views.googleDistrictdata, name='googleDistrictmap'),
   path('communityPartner',views.googlepartnerdata, name='googlehomepage'),
   path('communityPartnerType',views.googlemapdata, name='googlemap'),
   path('activate/<str:uidb64>/<str:token>', views.activate, name='activate')
]
