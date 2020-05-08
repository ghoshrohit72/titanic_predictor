from django.shortcuts import render
from . import fake
from . import ml_prediction

def home(request):
    return render(request, 'index.html')

def result(request):
    pclass = int(request.GET["pclass"])
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parched = int(request.GET["parched"])
    fare = int(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])
    prediction = ml_prediction.prediction_model(pclass, sex, age, sibsp, parched, fare, embarked,title)
    return render(request, 'result.html', {'prediction': prediction})