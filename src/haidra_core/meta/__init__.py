"""Information about and for meta-processes, such as CI/CD, monitoring, and logging."""

import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from haidra_core import default_env_files

use_default_env_files = os.environ.get("HAIDRA_USE_DEFAULT_ENV_FILES", "1").lower() not in ["0", "false", ""]

default_settings_config: SettingsConfigDict

if use_default_env_files:
    default_settings_config = SettingsConfigDict(
        env_file=default_env_files,
        use_attribute_docstrings=True,
    )
else:
    default_settings_config = SettingsConfigDict(
        use_attribute_docstrings=True,
    )


class SharedCISettings(BaseSettings):
    """Shared settings for CI/CD pipelines."""

    model_config = default_settings_config

    tests_ongoing: bool = Field(default=False)
    """Indicates if any CI/CD pipeline is ongoing."""
