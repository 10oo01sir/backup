# -*- coding: utf-8 -*-
import ConfigParser
import logging

__author__ = 'TwinDB Development Team'
__email__ = 'dev@twindb.com'
__version__ = '2.0.1'

log = logging.getLogger(__name__)


def setup_logging(logger, debug=False):

    fmt_str = "%(asctime)s: %(levelname)s:" \
              " %(module)s.%(funcName)s():%(lineno)d: %(message)s"

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(logging.Formatter(fmt_str))
    logger.handlers = []
    logger.addHandler(console_handler)
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)


def get_directories_to_backup(config):
    backup_dirs = []
    try:
        backup_dirs_value = config.get('source', 'backup_dirs')
        backup_dirs = backup_dirs_value.strip('"\'').split()
        log.debug('Directories to backup %r', backup_dirs)

    except ConfigParser.NoOptionError:
        log.debug('Not backing up files')

    return backup_dirs
