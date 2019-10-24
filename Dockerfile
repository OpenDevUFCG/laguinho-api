FROM python:alpine

EXPOSE 80
ENV FLASK_APP="laguinho"

WORKDIR /opt

# copy project files to /opt
COPY . /opt/

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
 && pip install pipenv \
 && pipenv install \
 && apk del .build-deps

ENTRYPOINT ["pipenv", "run", "start", "--port", "80"]
