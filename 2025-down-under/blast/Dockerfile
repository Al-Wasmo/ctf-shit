FROM ghcr.io/downunderctf/docker-vendor/nsjail@sha256:e09057add76c4df3ac662a0f7233f788870efb50904074acadbbc44c2a0b0447



RUN apt update
RUN apt install patchelf

COPY nsjail.cfg /home/ctf/
COPY libc/libm.so.6 libc/ld-linux-x86-64.so.2 libc/libc.so.6 libc/libgfortran.so.5 libc/libgcc_s.so.1 /home/ctf/chal/
COPY main /home/ctf/chal/pwn
COPY FLAG.TXT /home/ctf/chal/FLAG.TXT
RUN chmod +x /home/ctf/chal/pwn


libgfortran.so.5