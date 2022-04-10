from fastapi import APIRouter

from services.scraping.manga import MangaService
from services.scraping.home import HomeService

router = APIRouter()

@router.get("/mangas/recent")
async def recent_mangas():
    return await HomeService.recent_mangas()

@router.get("/manga/read")
async def read_chapter(id: str, chapter: str):
    return await MangaService.get_chapter(id, chapter)

@router.get("/mangas/hot")
async def hot_mangas():
    return await HomeService.hot_mangas()

@router.get("/mangas/new")
async def new_mangas():
    return await HomeService.new_mangas()

@router.get("/manga")
async def get_manga(id: str):
    return await MangaService.get_manga(id)