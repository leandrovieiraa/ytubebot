# libs
import os, datetime
from utils.utils import Utils
from watcher import Watcher

# draw header
Utils.draw_header()

# log 'Initializing'
Utils.draw_log(status=True, datetime=Utils.get_current_datetime(), message='Initializing system.')

# how many async instances to launch
instances = 1

# init watcher with instances
Watcher(instances)

# draw system end
Utils.draw_system_end()