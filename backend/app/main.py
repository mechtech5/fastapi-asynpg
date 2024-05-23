from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from api.api_v1.api import router as api_router
from core.config import get_api_settings
from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from starlette.responses import PlainTextResponse
from starlette.requests import Request


class RedirectHTTPS:
    def __init__(self, secure: bool = Depends(lambda x: x.url.scheme == "https")):
        self.secure = secure

    def __call__(self, request):
        if not self.secure:
            url = request.url.copy_with(scheme="https")
            raise HTTPException(status_code=307, headers={"Location": str(url)})
        return None


def get_app() -> FastAPI:
    api_settings = get_api_settings()

    server = FastAPI(**api_settings.fastapi_kwargs)
    # Add middleware
    origins = [
        "http://localhost:3000",
    ]

    server.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "PATCH", "POST", "DELETE", "OPTIONS", "PUT"],
        allow_headers=["*"],
    )

    # Add HSTS headers manually
    @server.middleware("http")
    async def add_hsts_header(request, call_next):
        response = await call_next(request)
        response.headers["Strict-Transport-Security"] = (
            "max-age=31536000; includeSubDomains"
        )
        response.headers["Content-Security-Policy"] = (
            "default-src 'self' https: 'unsafe-inline' 'unsafe-eval';"
        )
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        return response

    # Add the RateLimitExceeded exception handler
    @server.exception_handler(RateLimitExceeded)
    async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
        return PlainTextResponse(
            "Too many requests, please try again later.", status_code=429
        )

    server.include_router(api_router, prefix="/api/v1")

    @server.get("/", include_in_schema=False)
    def redirect_to_docs() -> RedirectResponse:
        return RedirectResponse(api_settings.docs_url)

    return server


app = get_app()
