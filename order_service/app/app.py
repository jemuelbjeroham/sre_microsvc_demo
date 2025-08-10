from fastapi import FastAPI

app = FastAPI(title="Order Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/orders")
def get_orders():
    return [
        {"id": 101, "product_id": 1, "user_id": 1, "status": "shipped"},
        {"id": 102, "product_id": 2, "user_id": 2, "status": "pending"},
        {"id": 103, "product_id": 3, "user_id": 3, "status": "delivered"}
    ]
