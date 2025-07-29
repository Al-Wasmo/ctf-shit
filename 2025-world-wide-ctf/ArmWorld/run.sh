#!/bin/bash
# qemu-aarch64-static ./chal
# qemu-system-aarch64 -M virt -S ./chal
qemu-aarch64 -g 1234 ./chal
# qemu-aarch64 ./chal
