FROM public.ecr.aws/docker/library/python:3.13-alpine

WORKDIR /app

COPY dist/app-0.1.0-py3-none-any.whl /app/

RUN pip install app-0.1.0-py3-none-any.whl

CMD python -m app.main