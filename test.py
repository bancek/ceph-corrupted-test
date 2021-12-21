import hashlib
import os
import time

import requests

base = "http://localhost:8080"

print("Authenticating")

res = requests.get(
    base + "/auth/v1.0",
    headers={
        "X-Auth-User": "test:test",
        "X-Auth-Key": "test",
    },
)
res.raise_for_status()

session = requests.session()
session.headers = {"X-Auth-Token": res.headers["X-Auth-Token"]}

print("Creating container")

container_url = base + "/swift/v1/test"

session.put(container_url).raise_for_status()

print("Creating random content")

content = os.urandom(16 * 1024 * 1024)
content_hash = hashlib.md5(content).hexdigest()

print("Content hash: " + content_hash)

print("Uploading object")

obj_url = container_url + "/testobj"

session.put(obj_url, data=content).raise_for_status()

print("Downloading object")

res = session.get(obj_url)
res.raise_for_status()

downloaded_content = res.content
downloaded_content_hash = hashlib.md5(downloaded_content).hexdigest()

print("Downloaded content hash: " + downloaded_content_hash)

assert len(downloaded_content) == len(content)
assert content_hash == downloaded_content_hash

print("Downloading object with sleep")

res = session.get(obj_url, stream=True)
res.raise_for_status()

print("Got response")
print("Sleeping 35 seconds")

time.sleep(35)

downloaded_content = res.content
downloaded_content_hash = hashlib.md5(downloaded_content).hexdigest()

print("Downloaded content hash: " + downloaded_content_hash)

assert len(downloaded_content) == len(content)
assert content_hash == downloaded_content_hash
