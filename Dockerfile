# syntax=docker/dockerfile:1
FROM python:3.10
RUN pip install --upgrade pip

RUN useradd -m -s /bin/bash -G sudo -p $(openssl passwd -1 password) hue
USER hue
ENV PATH="/home/hue/.local/bin:${PATH}"
ENV FLASK_APP=hue

WORKDIR /app

COPY --chown=hue:hue requirements.txt requirements.txt
RUN pip install --user -r requirements.txt
RUN export FLASK_APP=hue

COPY --chown=hue:hue . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000" ]

LABEL org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.title="PhilipsHue" \
      org.opencontainers.image.authors="hyena <hyena>" \
      org.opencontainers.image.source="https://github.com/thefueley/PhilipsHue" \
      org.opencontainers.image.revision="${BUILD_REF}" \
      org.opencontainers.image.vendor="SEISMOS"