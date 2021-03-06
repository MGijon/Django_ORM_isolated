#!/usr/bin/env python


def init_django():
    import django
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            "db",
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "TEST_CHARSET": "UTF8",
                "NAME": "dabatase.db",
                "TEST_NAME": ":memory:",
            }
        },
    )
    django.setup()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    init_django()
    execute_from_command_line()
