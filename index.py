from src.app import App


def handler(payload, context):
    """
    Init the lambda process.
    Read the env variables and decrypt the data
    """
    app = App(payload)
    action = payload.get("action")
    return getattr(app, action)()
