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

    print("Long polling for events...")
    events = client.events().generate_events_with_long_polling()
    for event in events:
        print(
            "\t",
            event.created_at,
            event.event_type,
            event.source.type,
            event.source.id,
            event.source.name,
        )


if __name__ == "__main__":
    main()
