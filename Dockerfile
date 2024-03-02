FROM python:3.12 AS base
WORKDIR /app
#EXPOSE 5432
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

FROM base AS build
COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

FROM node:20 AS buildjs
WORKDIR /app
COPY package-lock.json package.json templates ./

RUN npm install
RUN npm run build
RUN npm install --omit=dev

COPY assets/css assets/css

FROM base AS final

COPY requirements.txt requirements.txt
COPY --from=build /app .
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "church_site.wsgi"]