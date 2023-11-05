FROM python:3.11-slim

WORKDIR /service

COPY requirements.txt /service
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

COPY . /service

ENTRYPOINT ["python3"]
CMD ["./src/decision-service.py"]