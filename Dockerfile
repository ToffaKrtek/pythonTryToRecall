FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./app/requirements.txt /code/
RUN pip install mysqlclient
RUN pip install -r requirements.txt
COPY ./app /code/
