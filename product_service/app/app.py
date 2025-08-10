from fastapi import FastAPI

app = FastAPI(title="Product Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Headphones"},
        {"id": 3, "name": "Smartphone"}
    ]
