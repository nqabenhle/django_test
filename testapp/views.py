from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Homepage: Marvel Cinemetic Universe</h1>")

def movies(request):
    marvel_movies = [
        "Iron Man",
        "Captain America: The Winter Soldier",
        "Hulk",
        "Thor",
        "Spider-Man",
        "The Avengers",
        "Iron Man 2",
        "Thor: The Dark World",
        "The Avengers: The Age of Ultron",
        "Spiderman: Homecoming",
        "Captain America: Civil War",
        "Doctor Strange",
        "Iron Man 3"
        "Thor: Ragnarok",
        "The Avengers: Infinity War",
        "The Avengers: End Game",
    ]

    return JsonResponse({"movies": marvel_movies}, status=200)

def characters(request):
    marvel_characters = [
        {"madeUpName": "Ironman", "RealName":"Tony Stark"},
        {"madeUpName": "Spiderman", "RealName":"Peter Parker"},
        {"madeUpName": "The Scarlet Witch", "RealName":"Wanda Maximoff"},
        {"madeUpName": "Hulk", "RealName":"Bruce Banner"},
        {"madeUpName": "Antman", "RealName":"Scott"},
        {"madeUpName": "Hawkeye", "RealName":"Clint"},
        {"madeUpName": "Black Panther", "RealName":"T'Challa"},
    ]

    return JsonResponse({"characters": marvel_characters}, status=200)