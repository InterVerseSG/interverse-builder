import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.catalog import CATALOG
from app.schemas import BuildCommand, UnrealInstruction
from app.validator import validate_command

app = FastAPI(
    title="InterVerse Builder",
    version="0.2.0",
    description="Safe scene-command validation service for InterVerseSG and Unreal Engine.",
)

allowed_origins = [
    origin.strip()
    for origin in os.getenv("ALLOWED_ORIGINS", "*").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "InterVerse Builder",
        "version": "0.2.0",
        "status": "online",
    }


@app.get("/healthz")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/api/v1/catalog")
def catalog() -> dict[str, dict[str, int | str | bool]]:
    return {
        key: {
            "blueprint_class": item.blueprint_class,
            "max_quantity": item.max_quantity,
            "destructive": item.destructive,
        }
        for key, item in CATALOG.items()
    }


@app.post("/api/v1/build/validate", response_model=UnrealInstruction)
def build_validate(command: BuildCommand) -> UnrealInstruction:
    return validate_command(command)
