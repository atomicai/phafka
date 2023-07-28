import sys
from pykafka import KafkaClient
from pykafka.common import OffsetType
from itertools import islice


def main(args):
    try:
        topic = args[0]
    except Exception as ex:
        print("Failed to set topic")

    client = KafkaClient(hosts="127.0.0.1:9092")
    topic = client.topics["thebatai"]
    consumer = topic.get_simple_consumer(
        auto_offset_reset=OffsetType.LATEST, reset_offset_on_start=True
    )

    for message in islice(consumer, 100):
        print(message.value)


if __name__ == "__main__":
    main(sys.argv[1:])
