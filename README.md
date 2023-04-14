# Docker example  

(python, [FastAPI](https://fastapi.tiangolo.com/), [docker](https://docs.docker.com/))

Example of setting up docker containers interacting with each other

### Launching in Docker

Create and start container:


### Launching in Docker

Create and start container:

```bash

$ export DATA_FILE=<DATA_FILE>
$ export DATA_DIR=<DATA_DIR>
$ export ROWS_NUMBER=<ROWS_NUMBER>
$ export API_PORT=<API_PORT>
$ export DB_PORT=<DB_PORT>
$ docker-compose up

```

Stop lifted containers:

```bash
$ docker-compose stop
```

Start stopped containers:

```bash
$ docker-compose start
```

Stop and delete containers and network:

```bash
$ docker-compose down
```

Remove images:

```bash
$ docker rmi api
$ docker rmi db
$ docker rmi ui
```

Clear logs:

```bash
$ sudo rm -rf logs/*
```

List all networks:

```bash
$ sudo docker network ls
```

Inspect network:

```bash
$ sudo docker network inspect docker_example_docker_example
```