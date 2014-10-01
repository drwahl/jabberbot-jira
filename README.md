jabberbot-jira
==============

A jabberbot-python based bot for Jabber to provide insight into your Jira ticketing system

Setup/Usage
===========

To use docker (read as: build your own docker container), simply modify the
config file in the conf directory to match your environments configuration and
then run:
```
docker -t <container_name> .
```
This will create the docker container.  Then you just need to launch the
container with:
```
docker run <container_name>
```
