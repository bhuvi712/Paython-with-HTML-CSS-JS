airports = [
    {
        "name": "SVP Airport",
        "code": "SVP",
        "country": "India"
    },
    {
        "name": "Los Angeles International Airport",
        "code": "LAX",
        "country": "United States"
    },
    {
        "name": "London Heathrow Airport",
        "code": "LHR",
        "country": "United Kingdom"
    }
]

for airport in airports:
    print(f"{airport['name']} ({airport['code']}) is in {airport['country']}.")
