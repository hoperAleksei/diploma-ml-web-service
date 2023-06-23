FROM python:3.11

WORKDIR /code

COPY ../requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ../ .

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--root-path", "/api"]

RUN #alembic upgrade head

CMD ["python", "app/main.py"]
