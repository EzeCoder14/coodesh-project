from . import salesforce, ups

def get_provider_handler(provider: str):
    if provider.lower() == "salesforce":
        return salesforce.handle
    elif provider.lower() == "ups":
        return ups.handle
    else:
        raise ValueError(f"Unsupported provider: {provider}")