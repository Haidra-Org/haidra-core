from pydantic import AliasChoices, AnyUrl, Field, HttpUrl, SecretStr
from pydantic_settings import BaseSettings

DEFAULT_AI_HORDE_URL = HttpUrl("https://aihorde.net/api/")
DEFAULT_ALT_AI_HORDE_URLS: list[AnyUrl] = [HttpUrl("https://stablehorde.net/api/")]
DEFAULT_RATINGS_URL = HttpUrl("https://ratings.aihorde.net/api/")

DEFAULT_ANONYMOUS_API_KEY = "0000000000"


class AIHordeServerSettings(BaseSettings):
    """Base settings for AI Horde server configurations."""

    ai_horde_url: AnyUrl = Field(
        default=DEFAULT_AI_HORDE_URL,
        validation_alias=AliasChoices("HORDE_URL", "AI_HORDE_URL"),
    )
    alt_horde_urls: list[AnyUrl] = Field(default=DEFAULT_ALT_AI_HORDE_URLS)


class AIHordeClientSettings(BaseSettings):
    """Base settings for an AI Horde client."""

    api_key: SecretStr = Field(default=SecretStr(DEFAULT_ANONYMOUS_API_KEY))
    """The API key used for authenticating requests to the AI Horde."""

    ai_horde_url: AnyUrl = Field(default=DEFAULT_AI_HORDE_URL)
    """The API endpoint for the AI Horde to interact with."""

    alt_ai_horde_urls: list[AnyUrl] = Field(default=DEFAULT_ALT_AI_HORDE_URLS)
    """Alternative API endpoints for the AI Horde. These should all lead to the same logical AI Horde."""

    ratings_url: AnyUrl = Field(default=DEFAULT_RATINGS_URL)
    """The API endpoint for AI Horde ratings."""

    logs_folder: str = "./logs"
    """The folder where application logs are stored."""


class AIHordeWorkerSettings(AIHordeClientSettings):
    """Settings for an AI Horde worker."""

    aiworker_cache_home: str = "./models"
