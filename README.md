jabberbot-jira
==============

A jabberbot-python based bot for Jabber to provide insight into your Jira ticketing system

Setup/Usage
===========

To use docker (read as: build your own docker container), simply modify the
config file in the conf directory to match your environments configuration and
then run:
```
docker -t <image_name> .
```
This will create the docker image file.  Then you just need to launch the
container with:
```
docker run <image_name>
```
