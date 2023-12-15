FROM python:3.10

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8085

CMD ["uvicorn", "app.main:app", "--host", "studently.fastapi.at", "--port", "8085"]