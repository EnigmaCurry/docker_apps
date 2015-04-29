from    ubuntu:latest
run     apt-get update && \
        apt-get install -y firefox
RUN useradd -m docker && \
    echo "docker:test" | chpasswd && \
    usermod -s /bin/bash docker
ENV HOME /home/docker