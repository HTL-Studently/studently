FROM python:3.10
FROM python:3.10

WORKDIR /code

COPY . /code
COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8085

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8085"]