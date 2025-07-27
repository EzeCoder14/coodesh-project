from fastapi import Header, HTTPException

async def verify_auth(
    authorization: str = Header(None),
    x_api_key: str = Header(None)
):
    if authorization and authorization.startswith("Bearer "):
        return # Simulate OAuth
    elif authorization and authorization.startswith("Basic "):
        return # Simulate basic auth
    elif x_api_key == "valid_api_key":
        return # Simulate API Key
    raise HTTPException(status_code=401, detail="Unauthorized")