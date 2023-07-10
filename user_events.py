"""main.py"""

import logging
from app.config import AppConfig

from app.box_client import get_client

logging.basicConfig(level=logging.INFO)
logging.getLogger("boxsdk").setLevel(logging.CRITICAL)

conf = AppConfig()


def main():
    """
    Simple script to demonstrate the use of events
    """

    client = get_client(conf)

    stream_position = 0
    events = client.events().get_events(
        limit=10, stream_position=stream_position, stream_type="all"
    )
    stream_position = events["next_stream_position"]

    for event in events["entries"]:
        print(
            f"Got {event.event_type} on {event.created_at}: {event.source.type} {event.source.id} {event.source.name}"
        )


if __name__ == "__main__":
    main()
