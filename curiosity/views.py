from django.shortcuts import render, reverse
import requests
import json
import os

varbaseurl = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?"
# Front Hazard Camera
varfcamera = "camera=fhaz&earth_date=2019-4-19&page=1&"
#Rear Hazard Camera
varrcamera = "camera=rhaz&earth_date=2019-4-19&page=1&"
# Mast Camera
varmastcamera = "sol=1000&camera=mast&"

# CHEMCAM
varchemcamcamera = "sol=1000&camera=chemcam&"

# MAHLI
varmahlicamera = "camera=mahli&earth_date=2019-4-19&page=1&"

# MARDI
varmardicamera = "sol=100&camera=mardi&"

# NAVCAM
varnavcamcamera = "camera=navcam&earth_date=2019-4-19&page=1&"

varapi = "api_key="
varapikey = os.environ.get('NASA_API')
# 

# Create your views here.
def cfhaz(request):
    url = (varbaseurl+varfcamera+varapi+varapikey)
    curiosityrequest = requests.get(url)
    print(curiosityrequest)
    curiositydata = json.loads(curiosityrequest.text)
    curiosity = curiositydata['photos']
    return render(request, 'curiosity_content.html', {"curiosity": curiosity})


def crhaz(request):
    url = (varbaseurl+varrcamera+varapi+varapikey)
    curiosityrequest = requests.get(url)
    print(curiosityrequest)
    curiositydata = json.loads(curiosityrequest.text)
    curiosity = curiositydata['photos']
    return render(request, 'curiosity_content.html', {"curiosity": curiosity})


def cmast(request):
    url = (varbaseurl+varmastcamera+varapi+varapikey)
    curiosityrequest = requests.get(url)
    print(curiosityrequest)
    curiositydata = json.loads(curiosityrequest.text)
    curiosity = curiositydata['photos']
    return render(request, 'curiosity_content.html', {"curiosity": curiosity})


def cchemcam(request):
    url = (varbaseurl+varchemcamcamera+varapi+varapikey)
    curiosityrequest = requests.get(url)
    print(curiosityrequest)
    curiositydata = json.loads(curiosityrequest.text)
    curiosity = curiositydata['photos']
    return render(request, 'curiosity_content.html', {"curiosity": curiosity})


def cmahli(request):
    url = (varbaseurl+varmahlicamera+varapi+varapikey)
    curiosityrequest = requests.get(url)
    print(curiosityrequest)
    curiositydata = json.loads(curiosityrequest.text)
    curiosity = curiositydata['photos']
    return render(request, 'curiosity_content.html', {"curiosity": curiosity})


def cmardi(request):
    url = (varbaseurl+varmardicamera+varapi+varapikey)
    curiosityrequest = requests.get(url)
    print(curiosityrequest)
    curiositydata = json.loads(curiosityrequest.text)
    curiosity = curiositydata['photos']
    return render(request, 'curiosity_content.html', {"curiosity": curiosity})


def cnavcam(request):
    url = (varbaseurl+varnavcamcamera+varapi+varapikey)
    curiosityrequest = requests.get(url)
    print(curiosityrequest)
    curiositydata = json.loads(curiosityrequest.text)
    curiosity = curiositydata['photos']
    return render(request, 'curiosity_content.html', {"curiosity": curiosity})