from fastapi import FastAPI

app = FastAPI(title="CI/CD Course App", version="0.1.0")


@app.get("/")
def read_root() -> dict:
    return {"message": "Hello from the CI/CD mini course!"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


def add(a: int, b: int) -> int:
    """A plain function we can unit test, separate from the HTTP layer."""
    return a + b