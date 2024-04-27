FROM python:3.12-slim-bookworm AS base
WORKDIR /code
EXPOSE 8000

ARG  UID=1000
ARG  GID=1000

ENV DJANGO_ENV=production \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1

# pip:
ENV PIP_NO_CACHE_DIR=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_DEFAULT_TIMEOUT=100 \
  PIP_ROOT_USER_ACTION=ignore

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

RUN pip install -U pip \
  && pip install -r requirements.txt

# Running as non-root user:
USER web


FROM node:20-slim AS buildjs
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

WORKDIR /code

COPY pnpm-lock.yaml package.json tailwind.config.js ./
COPY templates templates
COPY core/styles core/styles
COPY ./**/forms.py forms/
COPY assets assets

RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
RUN pnpm run build


FROM base AS final

COPY --chown=web:web . /code
# RUN rm -rf assets/vendor
COPY --chown=web:web --from=buildjs /code/assets /code/assets

RUN python3 manage.py collectstatic --no-input

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "church_site.wsgi"]
