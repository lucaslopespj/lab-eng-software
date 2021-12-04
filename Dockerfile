FROM python:3.9-buster

RUN mkdir /ProjetoLeilao
RUN pip install -U pip

COPY ./requirements.txt ./ProjetoLeilao/requirements.txt
RUN pip install --no-compile  -r /ProjetoLeilao/requirements.txt

ENV PYTHONWARNINGS ignore
ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONUNBUFFERED 1
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY . /ProjetoLeilao/

WORKDIR /ProjetoLeilao
CMD ["run_web.sh"]