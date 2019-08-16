from . import views
from django.urls import path, include

urlpatterns = [
    path('pdfcreate/<int:donation_id>/', views.donation_receipt, name='donation' ),
]

