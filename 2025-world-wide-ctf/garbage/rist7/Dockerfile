FROM ubuntu AS app

RUN mkdir -p /challenge
WORKDIR /challenge
COPY --chmod=755 chall .
COPY flag.txt .

FROM pwn.red/jail

COPY --from=app / /srv
RUN mkdir -p /srv/app
COPY --chmod=555 ./entrypoint.sh /srv/app/run

ENV JAIL_PIDS=20 JAIL_TIME=1200
