"""main.py"""

import logging
from boxsdk import JWTAuth, Client

logging.basicConfig(level=logging.INFO)
logging.getLogger("boxsdk").setLevel(logging.CRITICAL)


def main():
    """
    Simple script to demonstrate the use of events
    """

    auth = JWTAuth.from_settings_file("./.jwt.config.json")
    auth.authenticate_instance()
    client = Client(auth)

    events = client.events().get_admin_events_streaming(
        stream_position=0,
        event_types=[
            "LOGIN",
        ],
    )

    for event in events["entries"]:
        print(
            event.created_at,
            event.event_id,
            event.event_type,
            event.ip_address,
            event.source.name,
        )


if __name__ == "__main__":
    main()
