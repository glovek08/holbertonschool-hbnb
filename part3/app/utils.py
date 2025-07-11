# fmt: off

def check_api_payload(
    payload: dict[str], model: dict[str]
) -> bool:
    return set(payload.keys()) == set(model.keys())
