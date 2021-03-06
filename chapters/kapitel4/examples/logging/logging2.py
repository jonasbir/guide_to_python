# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import logging

def do_some_logging(logger):
    logger.debug("Detta är ett testmeddelande...")
    logger.info("Detta är ett informationsmeddelande...")
    logger.warning("Detta är en varning...")
    logger.error("Detta är ett felmeddelande...")
    logger.critical("Detta är ett kritiskt fel...")

logging.basicConfig(level=logging.DEBUG)

mylog = logging.getLogger("mylog")

do_some_logging(mylog)

mylog.setLevel(logging.ERROR)

do_some_logging(mylog)
