FROM locustio/locust
WORKDIR /home/locust
COPY *.py ./
RUN pip install -U locust