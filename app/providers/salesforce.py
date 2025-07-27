import asyncio

async def handle(action: str, parameters: dict):
    await asyncio.sleep(1)
    return {
        "provider": "salseforce",
        "action": action,
        "response": f"Simulated Salesforce response for {action}"
    }