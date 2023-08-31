FROM amazonlinux:latest
RUN yum -y install which unzip python3-pip
RUN pip3 install boto3 pytz
ADD importUser.py /usr/local/bin/importUser.py
WORKDIR /tmp
USER nobody
ENTRYPOINT ["/usr/local/bin/importUser.py"]
