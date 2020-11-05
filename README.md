In current directory:
```bash
$ docker build -t cars_for_auction .
...
$ docker run --publish 7000:8000 --detach --name cars cars_for_auction
```