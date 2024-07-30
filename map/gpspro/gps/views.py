from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *
import json
from json import JSONEncoder
import datetime
# Create your views here.
# class DateTimeEncoder(JSONEncoder):
#         #Override the default method
#         def default(self, obj):
#             if isinstance(obj, (datetime.date, datetime.datetime)):
#                 return obj.isoformat()

def callfunc(data):
    data1= Asset_Cord.objects.values()
    data=list(data)
    data1=list(data1)
    response_data={
        "type": "geojson",
        "data": {
        "type": "FeatureCollection",
        "features":[]
        }
    }
    
    for i1 in data:
        time=Asset_Cord.objects.values().filter(asset=i1['id'])
        time_list=[]
        for i in time:
            time_list.append([i['asset_date_time'],i['asset_cor1'],i['asset_cor2']])
                
        
        time_list.sort(reverse=True)
        
        rtime=time_list[0]
        l=len(i1['asset_id'])
        
        l1=i1['asset_id']
        
        response={
            "type": "Feature",
            "properties": {
                "description":
                    str(str(l)+l1+"<p>"+"description : "+i1['asset_desc']+"<br> type of asset : "+i1['asset_type']+"</p>")#+"<button id="+i1["asset_id"]+"onclick='myFunction(this)'>Hello</button>")
            },
            "geometry": {
                "type": "Point",
                "coordinates": [rtime[1],rtime[2]]
            }
        }
        response_data['data']['features'].append(response)

    

    data=json.dumps(data)
    response_data=json.dumps(response_data)
    
    print(response_data)
    return HttpResponse(response_data,content_type='application/json')


def list_assets(request):
    if request.method=='GET':
        data=Asset.objects.values()
        return callfunc(data)
    



def asset_by_id(request,myid):
    if request.method=='GET':
        data=Asset.objects.values().filter(asset_id=myid)
        return callfunc(data)
    else:
        raise Http404
        



def asset_by_type(request,myid):
    if request.method=='GET':
        data=Asset.objects.values().filter(asset_type=myid)
        return callfunc(data)
    else:
        raise Http404
        
        
def asset_by_timezone(request,myid):
    if request.method=='GET':
        data=Asset.objects.values().filter(asset_id=myid)
        data1= Asset_Cord.objects.values()
        
        data=list(data)
        data1=list(data1)
        response_data={
            "type": "geojson",
            "data": {
            "type": "FeatureCollection",
            "features":[]
            }
        }
        
        for i1 in data:
            time=Asset_Cord.objects.values().filter(asset=i1['id'])
            time_list=[]
            for i in time:
                time_list.append([i['asset_date_time'],i['asset_cor1'],i['asset_cor2']])
                    
            
            time_list.sort(reverse=True)
            
            rtime=time_list
            l=len(i1['asset_id'])
            
            l1=i1['asset_id']
            for k in rtime:
                data2=str(k[0].strftime('%Y-%m-%d %H:%M'))     # converting django datetime field to simple field and string 
                print(data2)
                response={
                    "type": "Feature",
                    "properties": {
                        "description":
                            str(str(l)+l1+"<p>"+"description : "+i1['asset_desc']+"<br> type of asset : "+i1['asset_type']+"<br>  asset date-time zone : "+data2+"</p>")
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [k[1],k[2]]
                    }
                }
                response_data['data']['features'].append(response)

        

        data=json.dumps(data)
        response_data=json.dumps(response_data)
        
        # print(response_data)
        return HttpResponse(response_data,content_type='application/json')
    else:
        raise Http404
