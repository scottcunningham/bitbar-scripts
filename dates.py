#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from pytz import timezone
import pytz

zones = [pytz.utc, timezone('US/Pacific'), timezone('Europe/London'), timezone('Europe/Warsaw')]


def get_times(zones):
    format = '%H:%M:%S'  # %Z%z'
    for zone in zones:
        d = datetime.now(zone)
        yield zone.zone + ' ' + d.strftime(format)


print ' ☃ '.join(list(get_times(zones)))
