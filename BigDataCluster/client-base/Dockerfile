FROM ubuntu

ARG spark_version=3.1.2

RUN apt update -y &&\
    apt install python3.9 -y &&\
    apt install pip -y &&\
    update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1 && \
    apt install -y openjdk-8-jre-headless &&\
    apt install -y openjdk-8-jdk-headless &&\
    export JAVA_HOME=export JAVA_HOME="usr/lib/jvm/java-1.8.0-openjdk-amd64" &&\
    export PATH=$JAVA_HOME/bin:$PATH &&\
    apt install curl -y

CMD [ "bash" ]
