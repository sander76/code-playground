from app.config.configuation import get_settings


def go():
    settings = get_settings()

    return settings.setting1
