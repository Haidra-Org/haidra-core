from pydantic import BaseModel, Field


class ContainsMessage(BaseModel):
    """A model that contains a message field."""

    message: str


class ContainsStatus(BaseModel):
    """A model that contains a status field."""

    status: str


class ContainsReturnCode(BaseModel):
    """A model that contains a return code field."""

    return_code: int = Field(alias="rc")


class ContainsMessageReturnCode(ContainsMessage, ContainsReturnCode):
    """A model that contains both a message and a return code."""
