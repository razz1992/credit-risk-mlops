"""FastAPI inference service; model loading is added after training."""
from fastapi import FastAPI

app = FastAPI(title="Credit Default Classifier", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "model": "not_loaded"}
