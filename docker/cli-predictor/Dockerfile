FROM python:3.13-slim

WORKDIR /app

COPY data /app/data
COPY wine_color_predictor /app/wine_color_predictor
COPY pyproject.toml /app

RUN pip install .

ENTRYPOINT [ "python", "wine_color_predictor/cli_predictor.py" ]