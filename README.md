# Ceph corrupted test

```sh
# mimic (broken)
docker build --build-arg CEPH_VERSION=mimic -t ceph-corrupted-test .
# or nautilus (fixed)
docker build --build-arg CEPH_VERSION=nautilus -t ceph-corrupted-test .

docker run ceph-corrupted-test
```
