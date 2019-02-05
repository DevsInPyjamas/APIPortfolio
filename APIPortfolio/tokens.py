import os


def get_tokens():
    if "SECRET_KEY" not in os.environ:
        exit("ERROR: Secret Key required...\nExiting...")
    return {
        "secret": os.environ["SECRET_KEY"]
    }
