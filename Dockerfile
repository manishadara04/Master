FROM python:3.12.1
WORKDIR ./app
COPY . ./app
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    aria2 \
    wget \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*
RUN RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
RUN wget -O Bento4-SDK.zip https://github.com/axiomatic-systems/Bento4/archive/refs/heads/master.zip && \
    unzip Bento4-SDK.zip && \
    cd Bento4-master && \
    mkdir build && cd build && \
    cmake .. && \
    make mp4decrypt && \
    cp mp4decrypt /usr/local/bin/ && \
    cd ../.. && \
    rm -rf Bento4-SDK.zip Bento4-master
CMD ["python", "./main.py"]
