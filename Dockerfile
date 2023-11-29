FROM python:3.11 AS base
WORKDIR /app
EXPOSE 5432
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

FROM node:20 AS build
COPY . app
WORKDIR /app

RUN npm install
RUN npm run build
RUN npm install --omit=dev

FROM base AS final

COPY requirements.txt requirements.txt
COPY --from=build /app .
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "church_site.wsgi"]