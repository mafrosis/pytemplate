import logging


logger = logging.getLogger('{{cookiecutter.project_name}}')


def hello(name: str):
    logger.info('Hello %s', name)
