FROM ubuntu:14.04

MAINTAINER Tingyu Wang "twang66@gwu.edu"

#Update repos
Run apt-get update

Run apt-get install -y --no-install-recommends \
    git \
    make \
    gcc-4.8 \
    g++-4.7 \
    libboost1.54-dev

#github SSL certs are being rejected right now...
#clone repo at appropriate tag for paper submission
Run env GIT_SSL_NO_VERIFY=true git clone https://github.com/barbagroup/fmm-bem-relaxed.git

#Make examples
WORKDIR /fmm-bem-relaxed/examples
RUN make all
