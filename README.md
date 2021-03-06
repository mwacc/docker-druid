Modified Docker based Druid and Superset environment with external metastore in Postgre

Windows users
=============
allocate at least 6 GB RAM and 2 CPUs to docker.
execute in powershell
`$Env:COMPOSE_CONVERT_WINDOWS_PATHS=1`
before running docker-compose commands to resolve windows paths conversion

Create external volumes
======================
To overcome this [issue]: https://github.com/mattermost/mattermost-docker/issues/178, external volume shall be created in advance
`docker volume create postgres`


Docker Druid
================

[![Docker Build Status](https://img.shields.io/docker/build/rusnyder/druid.svg)][dockerhub]
[![Docker Image Stats](https://images.microbadger.com/badges/image/rusnyder/druid.svg)](https://microbadger.com/images/rusnyder/druid)
[![Docker Pulls](https://img.shields.io/docker/pulls/rusnyder/druid.svg)][dockerhub]
Tags:

- latest ([Dockerfile](https://github.com/rusnyder/docker-druid/blob/master/Dockerfile))

[dockerhub]: https://hub.docker.com/r/rusnyder/druid

What is Druid?
==================

Druid is an open-source analytics data store designed for business intelligence (OLAP) queries on event data. Druid provides low latency (real-time) data ingestion, flexible data exploration, and fast data aggregation. Existing Druid deployments have scaled to trillions of events and petabytes of data. Druid is most commonly used to power user-facing analytic applications.


How to use?
===========

Druid being a complex system, the best way to get up and running with a cluster is to use the docker-compose file provided.

Clone our public repository:

```
git clone git@github.com:rusnyder/docker-druid.git
```

and run :

```
docker-compose up
```

The compose file is going to launch :

- 1 [zookeeper](https://hub.docker.com/r/znly/zookeeper/) node
- 1 postgres database

and the following druid services :

- 1 broker
- 1 overlord
- 1 middlemanager
- 1 historical

as well as the following UIs :

- Swiv
- Metabase
- Superset

The image contains the full druid distribution and use the default druid cli. If no command is provided the image will run as a broker.

If you plan to use this image on your local machine, be carefull with the JVM heap spaces required by default (some services are launched with 15gb heap space).

The docker-compose file was tested on Windows 10 in PowerShell

Superset init
==============
run the following command for initialization
`docker exec -it superset superset-init`



Documentation
=============

Work in progress

Configuration
=============

Available environment options:

- `DRUID_XMX` '-'
- `DRUID_XMS` '-'
- `DRUID_NEWSIZE` '-'
- `DRUID_MAXNEWSIZE` '-'
- `DRUID_HOSTNAME` '-'
- `DRUID_PORT` '-'
- `DRUID_ZK_HOST` '-'

Authors
=======

- Jean-Baptiste DALIDO <jb@zen.ly>
- Clément REY <clement@zen.ly>
- Russell Snyder <ru.snyder@gmail.com>
