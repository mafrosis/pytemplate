import logging


logger = logging.getLogger('{{cookiecutter.project_name}}')


def ohai(name: str):
    logger.info('Hello %s', name)
