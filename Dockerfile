FROM python:3.9 

COPY . .

EXPOSE 8000 

RUN python -m pip install -r requirements.txt 

CMD ["uvicorn", "main:app", "--reload", "--port=8000"]