from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, Gauge
import psutil

app = FastAPI(title="Product Service")

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
CPU_USAGE = Gauge('process_cpu_seconds_total', 'CPU time used by process')
MEMORY_USAGE = Gauge('process_resident_memory_bytes', 'Resident memory size in bytes')

def update_system_metrics():
    CPU_USAGE.set(psutil.Process().cpu_percent(interval=None) / 100)  # CPU % as fraction
    MEMORY_USAGE.set(psutil.Process().memory_info().rss)             # RSS in bytes

@app.middleware("http")
async def metrics_middleware(request, call_next):
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    response = await call_next(request)
    return response

@app.get("/metrics")
def metrics():
    update_system_metrics()
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)

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
