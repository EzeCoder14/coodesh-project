import asyncio

async def handle(action: str, parameters: dict):
    await asyncio.sleep(1)
    return {
        "provider": "ups",
        "action": action,
        "response": f"<UPSResponse><Status>Success</Status><Action>{action}</Action></UPSResponse>"
    }
