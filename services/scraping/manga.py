from bs4 import BeautifulSoup
from typing import List

from fastapi import HTTPException 

from models.chapter import Chapter
from utils.html import fetch
from models.manga import Manga 

class MangaService():
    @staticmethod 
    async def get_manga(id: str):
        document = await fetch(f"https://manganato.com/{id}")
        if document is None:
            return 
        
        soup = BeautifulSoup(document, "lxml")
        info = soup.find("div", class_="story-info-right")
        chapters: List[Chapter] = []
        
        if info is None:
            raise HTTPException(
                status_code=404,
                detail="404 Not found: Invalid manga ID."
            )

        for i in soup.find_all("li", class_="a-h"):
            chapter_id = i.find("a").get("href")
            chapter_title = i.find("a").get("title")

            chapter = Chapter(
                id=chapter_id,
                title=chapter_title
            )
            chapters.append(chapter) 

        manga_title = info.find("h1").get_text("", strip=True)
        manga_description = soup.find("div", class_="panel-story-info-description").get_text(" ", strip=True).replace("Description : ", "")
        manga_image = soup.find("img", class_="img-loading").get("src")
        
        manga = Manga(
            id=id,
            title=manga_title,
            description=manga_description,
            image=manga_image,
            chapters=chapters,
        )   
        return manga

    @staticmethod
    async def get_chapter(id: str, chapter: str):
        document = await fetch(f"https://readmanganato.com/{id}/{chapter}")
        soup = BeautifulSoup(document, "lxml")
        images = []
        img = soup.find_all("img")

        if img is None:
            raise HTTPException(
                status_code=404,
                detail="404 Not found: img tag couldn't be found."
            )

        for i in img:
            images.append(i.get("src"))
            print(i.get("src"))

        chapter = Chapter(
            id=id,
            title=soup.find("div", class_="panel-chapter-info-top").find("h1").text,
            images=images
        )
        return chapter
