import sentry_sdk

sentry_sdk.init(
    dsn="https://d901eeec1256243ee9f4cf5e48777329@o4508471040409600.ingest.de.sentry.io/4508473091227728",
)


def resolved_generate_error():
    resolved_error = 1/1
    return resolved_error


def new_generate_error():
    my_list = []
    new_error = my_list[1]
    return new_error


def main():
    print('Привет! Это пример Sentry. Сейчас будем генерировать ошибку')
    resolved_generate_error()
    new_generate_error()


if __name__ == '__main__':
    main()
