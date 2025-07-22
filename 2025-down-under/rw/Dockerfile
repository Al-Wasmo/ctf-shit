FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04@sha256:e6663d542851d4f0450c3cf7d215169e3dc4ae982e24bc99f897ff780f00e504


# Install dependencies and gdb
# RUN apt-get update && \
#     apt-get install -y \
#         gdb \
#         git \
#         python3 \
#         python3-pip \
#         python3-dev \
#         libcapstone-dev \
#         libglib2.0-dev \
#         libncurses-dev \
#         libtinfo5 \
#         libz-dev \
#         curl \
#         tmux \ 
#         neovim \
#         socat

# RUN pip install pwntools
# RUN apt-get install gdbserver


# Optional: Copy your script
COPY rw.py /
COPY x.py /
# COPY pwndbg-dev /pwndbg-dev


# Clone and install mkdir pwndbg && pwndbg
# RUN cd pwndbg-dev && \
#     ./setup.sh


ENV JAIL_CWD=/chal
COPY ./flag.txt /home/ctf/chal/
COPY ./rw.py /home/ctf/chal/pwn
RUN chmod +x  /home/ctf/chal/pwn


# WORKDIR /home/ctf/chal/
# CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 ./pwn",stderr


