 #!/usr/bin/env python


from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(command='python /home/eferrer/Projects/TwitterBot/bot.py')
#job = cron.new(command='python /bot.py')

#job  = cron.new(command='/usr/bin/echo')
job.hour.every(4)
#job.hour.on(12)
job.enable()


cron.write()

if cron.render():
    print cron.render()
