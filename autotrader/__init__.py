# -*- coding: utf-8 -*-
import urllib3

from autotrader import exceptions
from autotrader.api import use
from autotrader.log import logger

from autotrader.init_trader import Trader

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
