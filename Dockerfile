FROM ubuntu

MAINTAINER David Wahlstrom

RUN mkdir /opt/jabberbot-jira/

ADD bin/* /opt/jabberbot-jira/
ADD conf/* /opt/jabberbot-jira/conf/

RUN apt-get update && apt-get install -y python-pip
RUN pip install jabberbot soappy xmpppy

CMD ["/opt/jabberbot-jira/jabberbot-jira.py"]
