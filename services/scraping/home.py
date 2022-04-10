from typing import List
from bs4 import BeautifulSoup
from fastapi import HTTPException

from models.manga import Manga
from utils.html import fetch
from models.chapter import Chapter

class HomeService():
    @staticmethod
    async def recent_mangas() -> List[Chapter]:
        document = await fetch("https://manganato.com/")
        soup = BeautifulSoup(document, "lxml")
        mangas: List[Manga] = []
        items = soup.find_all("div", class_="content-homepage-item")

        if items is None:
            raise HTTPException(
                status_code=404,
                details="404 Not found"
            )

        for i in items:
            manga = Manga(
                id=i.find("a", class_="tooltip item-img").get("href").replace("https://manganato.com/", "").replace("https://readmanganato.com/", ""),
                title=i.find("a", class_="tooltip item-img").get("title"),
                image=i.find("a", class_="tooltip item-img").find("img", class_="img-loading").get("src")
            )
            mangas.append(manga)
        return mangas

    @staticmethod 
    async def hot_mangas() -> List[Manga]:
        document = await fetch("https://manganato.com/genre-all?type=view")
        soup = BeautifulSoup(document, "lxml")
        mangas: List[Manga] = []
        items = soup.find_all("div", class_="content-genres-item")

        if items is None:
            raise HTTPException(
                status_code=404,
                details="404 Not found."
            )

        for i in items:
            manga = Manga(
                id=i.find("a", class_="genres-item-img").get("href"),
                title=i.find("a", class_="genres-item-img").get("title"),
                description=i.find("div", class_="genres-item-description").get_text("\n", strip=True),
                image=i.find("a", class_="genres-item-img").find("img", class_="img-loading").get("src")
            )
            mangas.append(manga)
        return mangas

    @staticmethod
    async def new_mangas() -> List[Manga]:
        document = await fetch("https://readmanganato.com/genre-all?type=newest")
        soup = BeautifulSoup(document, "lxml")
        mangas: List[Manga] = []
        items = soup.find_all("div", class_="content-genres-item")

        if items is None:
            raise HTTPException(
                status_code=404,
                details="404 Not found."
            )
            
        for i in items:
            manga = Manga(
                id=i.find("a", class_="genres-item-img").get("href"),
                title=i.find("a", class_="genres-item-img").get("title"),
                description=i.find("div", class_="genres-item-description").get_text("\n", strip=True),
                image=i.find("a", class_="genres-item-img").find("img", class_="img-loading").get("src")
            )
            mangas.append(manga)
        return mangas