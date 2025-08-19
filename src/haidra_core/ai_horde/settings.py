from pydantic import AliasChoices, AnyUrl, Field, HttpUrl, SecretStr
from pydantic_settings import BaseSettings

from haidra_core.meta import default_settings_config

DEFAULT_AI_HORDE_URL = HttpUrl("https://aihorde.net/api/")
DEFAULT_ALT_AI_HORDE_URLS: list[AnyUrl] = [HttpUrl("https://stablehorde.net/api/")]
DEFAULT_RATINGS_URL = HttpUrl("https://ratings.aihorde.net/api/")

DEFAULT_ANONYMOUS_API_KEY = "0000000000"

DEFAULT_LOGS_FOLDER = "./logs"
DEFAULT_MODELS_FOLDER = "./models"


class AIHordeSettings(BaseSettings):
    """Base settings for AI Horde configurations."""

    model_config = default_settings_config

    ai_horde_url: AnyUrl = Field(
        default=DEFAULT_AI_HORDE_URL,
        validation_alias=AliasChoices("HORDE_URL", "AI_HORDE_URL"),
    )
    """The URL for this AI Horde instance. If more than one, additional URLs are in the field `alt_horde_urls`."""

    alt_horde_urls: list[AnyUrl] = Field(default=DEFAULT_ALT_AI_HORDE_URLS)
    """Alternative API endpoints for the AI Horde. These should all lead to the same logical AI Horde."""


class AIHordeServerSettings(AIHordeSettings):
    """Base settings for AI Horde server configurations."""


class AIHordeClientSettings(AIHordeSettings):
    """Base settings for an AI Horde client."""

    api_key: SecretStr = Field(default=SecretStr(DEFAULT_ANONYMOUS_API_KEY))
    """The API key used for authenticating requests to the AI Horde."""

    ratings_url: AnyUrl = Field(default=DEFAULT_RATINGS_URL)
    """The API endpoint for AI Horde ratings."""

    logs_folder: str = DEFAULT_LOGS_FOLDER
    """The folder where application logs are stored."""


class AIHordeWorkerSettings(AIHordeClientSettings):
    """Settings for an AI Horde worker."""

    aiworker_cache_home: str = DEFAULT_MODELS_FOLDER
    """The folder where AI worker (or client) files are stored, most notably models and checkpoints."""
