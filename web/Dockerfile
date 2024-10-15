FROM python:3

ARG SERVER="1"
COPY . /
WORKDIR /
RUN pip install --no-cache-dir -r /requirements.txt \
    && chmod +x /run.sh
ENV SERVER="1"
ENTRYPOINT [ "./run.sh" ]
