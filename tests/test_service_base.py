from haidra_core.service_base import ContainsMessage, ContainsMessageReturnCode, ContainsReturnCode, ContainsStatus


def test_fields_as_expected() -> None:
    """Test that the fields of the models are as expected."""
    ContainsStatus.model_validate({"status": "ok"})
    ContainsMessage.model_validate({"message": "Hello, world!"})
    crc = ContainsReturnCode.model_validate({"rc": 0})
    assert hasattr(crc, "return_code"), "`return_code` is more readable than `rc`."

    message_and_return_code = ContainsMessageReturnCode.model_validate({"message": "Hello, world!", "rc": 0})
    assert isinstance(message_and_return_code, ContainsMessageReturnCode)
    assert isinstance(message_and_return_code, ContainsMessage)
    assert hasattr(message_and_return_code, "message")
    assert hasattr(message_and_return_code, "return_code")
