FROM python:3.9-buster

RUN mkdir /
RUN pip install -U pip

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-compile  -r requirements.txt

ENV PYTHONWARNINGS ignore
ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONUNBUFFERED 1
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY . /

WORKDIR /
CMD ["run_web.sh"]