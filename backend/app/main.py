from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Data Governance Platform",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "service": "enterprise-data-governance-platform",
    }
