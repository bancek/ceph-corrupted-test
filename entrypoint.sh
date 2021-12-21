#!/bin/bash

set -e

rm -rf /tmp/ceph
mkdir /tmp/ceph

/micro-osd.sh /tmp/ceph

echo 'Ceph ready'

exec "$@"
