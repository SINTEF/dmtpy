FROM python:3.8-slim

WORKDIR /dmtpy

COPY src src
COPY requirements-dev.txt .
COPY requirements.txt .
COPY setup.py .
COPY README.md .

RUN pip install -r requirements.txt -r requirements-dev.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

RUN pylint src --errors-only 