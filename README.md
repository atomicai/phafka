# phafka

> This repo is a "hello world" to kickstart <a href="https://kafka.apache.org">kafka</a> dev providing with the simplest possible installation alongside the pub/sub mechanism.

The pub/sub mechanics is a well-known way to exchange data between your microservices. However, <a href="https://kafka.apache.org">kafkas</a> way is a little bit complicated. So hope, this little snippets `phafka/pub.py` and `phafka/sub.py` will help to understand without doing nightmare devops.

### Installation

All you to do to get started is a running <a href="https://docs.docker.com/compose/gettingstarted/">docker</a> and <a href="https://pypi.org/project/pykafka/">pykafka</a> python package. So, make sure docker is running and you have `pykafka` in your environment otherwise `pip install pykafka==2.8.0` and you are ready to go.



### Running

First, notice the environment variable inside `docker-compose.yaml` file which says: 

```python
KAFKA_CREATE_TOPICS: "thebatai:1:1"
```

It automatically defines the topic `thebatai` setting `1` partition and `1` replicas. Feel free to play around with these parameters and set your own `topic_name` with custom partition schema and any replicas count you want.

Finally, fire up the kafka by running: `docker-compose up -d` 





### Publishing

```bash
python phafka/pub.py thebatai hellokafka
```

### Subscribing

```bash
python phafka/sub.py thebatai
```



> ©️ May the odds be ever in your favour 
