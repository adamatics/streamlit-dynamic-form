FROM python:3.10-slim

EXPOSE 8501

RUN pip install poetry
COPY pyproject.toml poetry.lock /tmp
WORKDIR /tmp
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-root

WORKDIR /app
ENV MAIN_APP_FILE="dynamic_form.py"
COPY ./${MAIN_APP_FILE} .
COPY ./form.json .
ADD start_app.sh /app
CMD bash /app/start_app.sh
