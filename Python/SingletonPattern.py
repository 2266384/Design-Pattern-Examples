import logging

logging.basicConfig(level=logging.INFO)


# Define the AppConfig class
class AppConfig:
    def __init__(self, environment: str):
        self.environment = environment


# Created an instance of AppConfig called 'config'
# If you import this module into other scripts they access the same object as it
# only gets created when python first imports the module
config = AppConfig(environment="development")


# Functions that use the shared instance
def process_request() -> None:
    logging.info("Environment: %s", config.environment)


def generate_report() -> None:
    logging.info("Report environment: %s", config.environment)


# Call both functions
process_request()
generate_report()

# Validate two references are using the same object
first_ref = config
second_ref = config
assert first_ref is second_ref