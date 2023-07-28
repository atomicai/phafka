import sys
from pykafka import KafkaClient


def main(args):
    try:
        topic = args[0]
        message = args[1]
    except Exception as ex:
        print("Failed to set topic or message")

    client = KafkaClient(hosts="localhost:9092")
    topic = client.topics["thebatai"]
    producer = topic.get_sync_producer()
    producer.produce(message.encode("ascii"))


if __name__ == "__main__":
    main(sys.argv[1:])
