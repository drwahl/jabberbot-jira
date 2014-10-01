FROM ubuntu

MAINTAINER David Wahlstrom

RUN mkdir /opt/jabberbot-jira/

ADD bin/ /opt/jabberbot-jira
ADD conf/jabberbot-jira.conf /opt/jabberbot-jira/conf/

RUN apt-get update && apt-get install -y python-pip python-xmpp
RUN pip install jabberbot soappy

CMD ["/opt/jabberbot-jira/jabberbot-jira.py"]
