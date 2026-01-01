from fastapi import FastAPI, Depends
from app.auth import get_current_user
from app.rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware
from app.services.scraper import fetch_sector_news
# from app.services.ai_analyzer import analyze_with_gemini
from app.services.markdown_generator import generate_markdown
from app.session_manager import track_session
from fastapi import Request
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

from app.services.ai_analyzer import analyze_with_ai



load_dotenv()

app = FastAPI()


app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})

@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(request: Request, sector: str, user: str = Depends(get_current_user)):
    track_session(user)
    news = await fetch_sector_news(sector)
    # print("News==========>", news)
    analysis = await analyze_with_ai(news, sector)
    # print("Analysis==========>", analysis)
    # print("Request Headers==========>", request.headers)
    return generate_markdown(sector, analysis)

