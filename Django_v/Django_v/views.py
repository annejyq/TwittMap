# Declare relationship with html files and websites. Transmitting varibles between them.
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from datetime import datetime

import json
import time
import os
import re
import requests


def tweeterAPI(request):
    return render(request, 'map.html')


def search(request):
    keyword = request.POST['x']     #Find twitter about keyword 'x'
    response = es_search(keyword)
    res = response['hits']['hits']
    res = json.dumps(res)
    return HttpResponse(res,content_type='application/json')


def geosearch(request):
    location = request.POST['location'].split(",")     #Find twitter around a chosen location
    location[0] = float(location[0])
    location[1] = float(location[1])
    distance = request.POST['distance']
    print 'location: %s, radius: %s' % (location, distance)

    response = es_geosearch(location, distance, 2000) # search at most 2000 tweets
    print 'geosearch response: %s' % response
    response = response['hits']['hits']
    response = json.dumps(response)
    return HttpResponse(response, content_type='application/json')


#Send Post Request to ElasticSearch
def es_search(keyword):
    data = {"size": 2000,"query": {"query_string": { "query": keyword }}}
    search_address = 'https://search-twittmap-z7jgounce6usksgcxt4kbsruvi.us-east-1.es.amazonaws.com/twittmap/tweets/_search'
    response = requests.post(search_address, data=json.dumps(data))
    print response
    return response.json()

#Geo index is set to "geo_point" variable
def es_geosearch(location, distance, size):
        data = {
            "size": size,
            "query": {
                "bool": {
                    "must": {
                        "match_all": {}
                    },
                    "filter": {
                        "geo_distance": {
                            "distance": '%skm' % (distance),
                            "geo": location
                        }
                    }
                }
            }
        }
    search_address = 'https://search-twittmap-z7jgounce6usksgcxt4kbsruvi.us-east-1.es.amazonaws.com/twittmap/tweets/_search'
    response = requests.post(search_address, data=json.dumps(data))
    print response
    return response.json()

