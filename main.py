from fastapi import FastAPI

app = FastAPI(title="Lipika's Food Services API")


@app.get("/")
def home():
    return {
        "message": "Lipika's Food Services Backend is running!"
    }


@app.get("/menu")
def get_menu():
    return {
        "items": [
            {
                "id": 1,
                "name": "Veg Burger",
                "price": 120
            },
            {
                "id": 2,
                "name": "Pizza",
                "price": 250
            }
        ]
    }
