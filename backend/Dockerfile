FROM python:3.9-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 80
COPY app /backend/app

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "80"]