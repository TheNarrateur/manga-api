import aiohttp

from fastapi import HTTPException

async def fetch(endpoint: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                return await response.text()
    except Exception as e:
        raise HTTPException(
            status_code=response.status,
            detail=f"FetchError: {e.with_traceback}"
        )
