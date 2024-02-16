from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.


def insert_employment_business_data(self):
    import csv
    with open('C:\\Users\\hp\\OneDrive\\Desktop\\Django projects\\Nani\\Scripts\\project38\\app\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:
        IDO = csv.reader(FO)
        next(IDO)
        for i in IDO:
            sr = i[0]
            p = i[1]
            dv = i[2]
            s = i[3]
            st = i[4]
            u = i[5]
            m = i[6]
            su = i[7]
            gr = i[8]
            sr1 = i[9]
            sr2 = i[10]
            sr3 = i[11]
            sr4 = i[12]
            sr5 = i[13]
            EBO = EmployeeBusiness(Series_reference=sr,Period=p,Data_value=dv,Suppressed=s,Status=st,Units=u,Magnitude=m,Subject=su,Group=gr,Series_title_1=sr1,Series_title_2=sr2,Series_title_3=sr3,Series_title_4=sr4,Series_title_5=sr5)
            EBO.save()
    return HttpResponse('<center><h1>Employee data is successfully inserted')





def Employee_data(request):
    EBDO = EmployeeBusiness.objects.all()
    d={'EBDO':EBDO}

    return render(request,'Employee_data.html',d)