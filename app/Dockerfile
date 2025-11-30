FROM public.ecr.aws/docker/library/python:3.13-alpine

ARG APP_VERSION=0.1.0

WORKDIR /app

COPY dist/app-${APP_VERSION}-py3-none-any.whl /app/

RUN pip install app-${APP_VERSION}-py3-none-any.whl

CMD ["python", "-m", "app.main"]
