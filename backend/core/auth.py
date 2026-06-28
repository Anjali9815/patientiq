from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
import httpx
from .config import CLERK_SECRET_KEY

security = HTTPBearer()

async def get_jwks():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.clerk.com/v1/jwks")
        return response.json()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    try:
        jwks = await get_jwks()
        header = jwt.get_unverified_header(token)
        key = next(k for k in jwks["keys"] if k["kid"] == header["kid"])
        payload = jwt.decode(token, key, algorithms=["RS256"])
        clerk_id = payload.get("sub")
        if not clerk_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return clerk_id
    except Exception:
        raise HTTPException(status_code=401, detail="Token invalid or expired")