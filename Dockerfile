FROM ubuntu:18.04

RUN apt-get update \
  && apt-get install -y apt-transport-https wget gnupg python3-pip uuid-runtime \
  && pip3 install requests \
  && wget -q -O- 'https://download.ceph.com/keys/release.asc' | apt-key add -

ARG CEPH_VERSION=mimic

RUN echo "deb https://download.ceph.com/debian-${CEPH_VERSION}/ bionic main" > /etc/apt/sources.list.d/ceph.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends ceph-mgr ceph-mon ceph-osd radosgw

COPY micro-osd.sh /
COPY entrypoint.sh /

ENV CEPH_CONF=/tmp/ceph/ceph.conf

ENTRYPOINT [ "/entrypoint.sh" ]

COPY test.py /

CMD [ "python3", "-u", "test.py" ]
