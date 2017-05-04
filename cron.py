 #!/usr/bin/env python

from secrets import *
from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(command=path)
#job = cron.new(command='python /bot.py')

#job  = cron.new(command='/usr/bin/echo')
job.hour.every(4)
#job.minute.every(3)
job.enable()


cron.write()

if cron.render():
    print cron.render()
