import os
from functools import lru_cache
from typing import Any, Dict, List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    BACKEND_ENV: str = os.getenv("BACKEND_ENV", "local")


class APISettings(BaseSettings):
    """This class enables the configuration of your FastAPI instance
    through the use of environment variables.

    Any of the instance attributes can be overridden upon instantiation by
    either passing the desired value to the initializer, or by setting the
    corresponding environment variable.

    Attribute `xxx_yyy` corresponds to environment variable `API_XXX_YYY`.
    So, for example, to override `api_prefix`, you would set the environment
    variable `API_PREFIX`.

    Note that assignments to variables are also validated, ensuring that
    even if you make runtime-modifications to the config, they should have
    the correct types.
    """

    # FastAPI
    api_prefix: str = "/api/v1"
    project_name: str = "NTAI API"
    version: str = "1.0"
    debug: bool = True
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    backend_cors_origins: List[AnyHttpUrl] = []

    # Custom settings
    disable_docs: bool = False

    # Database
    db_async_connection_str: str
    
    # access token
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SECRET_KEY: str

    # smtp details
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USERNAME: str
    SMTP_PASSWORD: str

    SENDGRID_API_KEY: str

    FROM_EMAIL: str
    CLIENT_URL: str
    default_scope: Dict = {"scopes": ["counsellor"]}

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        """This returns a dictionary of the most commonly used keyword
        arguments when initializing a FastAPI instance.

        If `self.disable_docs` is True, the various docs-related arguments
        are disabled, preventing spec from being published.
        """
        fastapi_kwargs: Dict[str, Any] = {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.project_name,
            "version": self.version,
        }
        if self.disable_docs:
            fastapi_kwargs.update(
                {"docs_url": None, "openapi_url": None, "redoc_url": None}
            )
        return fastapi_kwargs

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_app_settings() -> AppSettings:
    return AppSettings()


@lru_cache()
def get_api_settings() -> APISettings:
    """This function returns a cached instance of the APISettings object.

    Caching is used to prevent re-reading the environment every time the API
    settings are used in an endpoint.
    If you want to change an environment variable and reset the cache
    (e.g., during testing), this can be done using the `lru_cache` instance
    method `get_api_settings.cache_clear()`.
    """
    app_settings = get_app_settings()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    envs_dir = os.path.join(current_dir, "..", "core", "envs")
    env_file = os.path.join(envs_dir, f".env.{app_settings.BACKEND_ENV}")
    return APISettings(_env_file=env_file)
