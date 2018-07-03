FROM python:3.4
WORKDIR ./

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install graphviz

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

RUN jupyter notebook --generate-config

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]

VOLUME ["/app"]
WORKDIR /app

EXPOSE 8888
