
from ubuntu@sha256:72297848456d5d37d1262630108ab308d3e9ec7ed1c3286a32fe09856619a782 

# FROM pwn.red/jail
# COPY --from=app / /srv

COPY main /run
COPY flag.txt libc/libc.so.6* libc/ld-linux-x86-64.so.2* /

RUN chmod +x /run
ENV JAIL_TIME=7
