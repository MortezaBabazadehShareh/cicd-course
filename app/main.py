from fastapi import FastAPI

app = FastAPI(title="CI/CD Course App", version="0.1.0")


@app.get("/")
def read_root() -> dict:
    return {"message": "I WANT TO CHECK THE DEPLOYMENT!"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok, now this the second commit of mine to show how the CI/CD that we designed works"}


def add(a: int, b: int) -> int:
    """A plain function we can unit test, separate from the HTTP layer."""
    return a - b