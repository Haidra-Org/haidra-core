from pydantic import SecretStr

from haidra_core.ai_horde import AIHordeClientSettings, AIHordeWorkerSettings
from haidra_core.ai_horde.settings import AIHordeServerSettings


def test_ai_horde_client_settings() -> None:
    """Verify AIHordeClientSettings with default values."""
    settings = AIHordeClientSettings(api_key=SecretStr("test_api_key"))
    assert settings.api_key.get_secret_value() == "test_api_key"
    assert settings.ai_horde_url.encoded_string() == "https://aihorde.net/api/"
    assert settings.alt_horde_urls[0].encoded_string() == "https://stablehorde.net/api/"
    assert settings.ratings_url.encoded_string() == "https://ratings.aihorde.net/api/"
    assert settings.logs_folder == "./logs"


def test_ai_horde_worker_settings() -> None:
    """Verify AIHordeWorkerSettings with custom values."""
    settings = AIHordeWorkerSettings(
        api_key=SecretStr("test_worker_api_key"),
        aiworker_cache_home="./__worker_models",
    )
    assert settings.api_key.get_secret_value() == "test_worker_api_key"
    assert settings.ai_horde_url.encoded_string() == "https://aihorde.net/api/"
    assert settings.alt_horde_urls[0].encoded_string() == "https://stablehorde.net/api/"
    assert settings.ratings_url.encoded_string() == "https://ratings.aihorde.net/api/"
    assert settings.logs_folder == "./logs"
    assert settings.aiworker_cache_home == "./__worker_models"


def test_ai_horde_server_settings() -> None:
    """Verify AIHordeServerSettings with default values."""
    import os

    original_horde_url = os.environ.get("HORDE_URL")
    original_ai_horde_url = os.environ.get("AI_HORDE_URL")

    os.environ["HORDE_URL"] = "https://test.local/api/"

    if original_ai_horde_url is not None:
        del os.environ["AI_HORDE_URL"]

    settings = AIHordeServerSettings()
    assert settings.ai_horde_url.encoded_string() == "https://test.local/api/"

    del os.environ["HORDE_URL"]

    os.environ["AI_HORDE_URL"] = "https://test2.local/api/"
    settings = AIHordeServerSettings()
    assert settings.ai_horde_url.encoded_string() == "https://test2.local/api/"

    del os.environ["AI_HORDE_URL"]

    if original_horde_url is not None:
        os.environ["HORDE_URL"] = original_horde_url

    if original_ai_horde_url is not None:
        os.environ["AI_HORDE_URL"] = original_ai_horde_url


def test_settings_by_environment_variable() -> None:
    """Test settings can be overridden by environment variables."""
    import os

    from haidra_core.ai_horde.settings import AIHordeWorkerSettings

    aiworker_cache_home = os.environ.get("AIWORKER_CACHE_HOME")
    original_cache_home = aiworker_cache_home

    if aiworker_cache_home is None:
        aiworker_cache_home = "./__worker_models"
        os.environ["AIWORKER_CACHE_HOME"] = aiworker_cache_home

    settings = AIHordeWorkerSettings()

    assert settings.aiworker_cache_home == aiworker_cache_home

    if original_cache_home is None:
        del os.environ["AIWORKER_CACHE_HOME"]
    else:
        os.environ["AIWORKER_CACHE_HOME"] = original_cache_home
