from django.shortcuts import render

content = [
    {
        "flight_id": 2500,
        "airline": "Star travelers",
        "price": 400,
        "currency": "USD",
        "from": "Krakow",
        "to": "Tokyo"
    },
    {
        "flight_id": 22212,
        "airline": "Star travelers",
        "price": 350,
        "currency": "USD",
        "from": "Krakow",
        "to": "Hong Kong"
    }
]

def home(request):
    return render(request, 'search_app/home.html', {'content': content, 'title': 'Flight search'})

def test_path(request):
    return render(request, 'search_app/test.html')

