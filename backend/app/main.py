from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="MCDA Studio",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # default for VUE
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=dict)
def root() -> dict:
    return {"status": "ok"}
