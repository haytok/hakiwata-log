FROM python:3

WORKDIR /app

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8 \
    LANGUAGE ja_JP:ja \
    LC_ALL ja_JP.UTF-8 \
    TZ JST-9

RUN pip install --upgrade pip

COPY ./* /app/

RUN pip install -r /app/requirements.txt

CMD ["python", "main.py"]
