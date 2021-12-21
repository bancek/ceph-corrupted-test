# Ceph corrupted test

```sh
# mimic (broken)
docker build --build-arg CEPH_VERSION=mimic -t ceph-corrupted-test .
# or nautilus (fixed)
docker build --build-arg CEPH_VERSION=nautilus -t ceph-corrupted-test .

docker run -it ceph-corrupted-test
```

Example output:

```
...
ceph version 13.2.10 (564bdc4ae87418a232fc901524470e1a0f76d641) mimic (stable)
...
Ceph ready
Authenticating
Creating container
Creating random content
Content hash: c97757aac412b32a9fd188ce95e7dc95
Uploading object
Downloading object
Downloaded content hash: c97757aac412b32a9fd188ce95e7dc95
Downloading object with sleep
Got response
Sleeping 35 seconds
Downloaded content hash: c8dad67c8e59de096bb4d6d76c44c75a
Traceback (most recent call last):
  File "test.py", line 69, in <module>
    assert content_hash == downloaded_content_hash
AssertionError
```
