"""
URL configuration for django_rest_learn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product import views as productview
from employee import views as employeeview
from invoice import views as invoiceview
from inventory import views as inventoryview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('product-list/',productview.productList_view),
    path('product/<int:pk>',productview.product_view),
    path('product-create/',productview.productCreate_view),
    path('employee/',employeeview.employee_view),   
    path('employee/<int:pk>',employeeview.employee_view),
    path('invoice/',invoiceview.Invoice_view.as_view()),
    path('invoice/<int:pk>',invoiceview.Invoice_view.as_view()),

    path('inventory-list/',inventoryview.inventoryList.as_view()),
    path('inventory-create/',inventoryview.inventoryCreate.as_view()),
    path('inventory/<int:pk>',inventoryview.inventoryRetrieve.as_view()),
    path('inventory-update/<int:pk>',inventoryview.inventoryUpdate.as_view()),
    path('inventory-delete/<int:pk>',inventoryview.inventoryDestroy.as_view()),
]
