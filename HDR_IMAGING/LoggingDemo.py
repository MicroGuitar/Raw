#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
__author__ = 'gimbu'
__data__ = '30/03/17'

import logging
a = 666
import logging
logging.basicConfig(filename='example.log', filemode='w', format='%(asctime)s: %(levelname)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
logging.warning('%s before you', a)
