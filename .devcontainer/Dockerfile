FROM python:3.11.13

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /root/workspace
COPY requirements.txt /root/workspace/
WORKDIR /working_dir

RUN pip install --upgrade pip\
    && pip install --no-cache-dir setuptools\
    && pip install -r /root/workspace/requirements.txt
