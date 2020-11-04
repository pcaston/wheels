[![Build Status](https://dev.azure.com/openpeerpower/Opp.io/_apis/build/status/wheels?branchName=master)](https://dev.azure.com/openpeerpower/Opp.io/_build/latest?definitionId=11&branchName=master)

# Opp.io Wheels builder

```sh

$ python3 -m builder \
    --apk build-base \
    --index https://wheels.openpeerpower.io \
    --requirement requirements_all.txt \
    --upload rsync \
    --remote user@server:/wheels
```

## Supported file transfer

- rsync

## Folder structure of index folder:

`/alpine-{version}/{arch}/*`
