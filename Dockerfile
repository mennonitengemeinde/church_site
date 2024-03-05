FROM python:3.12-slim-bookworm AS base
WORKDIR /code
EXPOSE 8000

ARG  UID=1000 \
  GID=1000

ENV DJANGO_ENV=production \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  # pip:
  PIP_NO_CACHE_DIR=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_DEFAULT_TIMEOUT=100 \
  PIP_ROOT_USER_ACTION=ignore \
  # poetry:
  POETRY_VERSION=1.6.1 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local'

# SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

# hadolint ignore=DL3008
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
  build-essential \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*


RUN groupadd -g "${GID}" -r web \
  && useradd -d '/code' -g web -l -r -u "${UID}" web \
  && chown web:web -R '/code'

# Copy only requirements, to cache them in docker layer
COPY --chown=web:web ./requirements.txt /code/

# Project initialization:
# hadolint ignore=SC2046
# RUN --mount=type=cache,target="$POETRY_CACHE_DIR" \
#   echo "$DJANGO_ENV" \
#   && poetry version \
# Install deps:
# RUN poetry version 
# hadolint ignore=DL3013
RUN pip install -U pip \
  && pip install -r requirements.txt

# Running as non-root user:
USER web


FROM node:20 AS buildjs

WORKDIR /code

COPY package-lock.json package.json tailwind.config.js ./
COPY templates templates
COPY core/styles core/styles
COPY ./**/forms.py forms/
COPY assets assets

RUN npm install && npm run build



FROM base AS final

COPY --chown=web:web . /code
# RUN rm -rf assets/vendor
COPY --chown=web:web --from=buildjs /code/assets /code/assets

RUN python3 manage.py collectstatic --no-input

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "church_site.wsgi"]
