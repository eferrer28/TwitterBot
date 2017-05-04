from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(command='python /Projects/TwitterBot/bot.py')
job.minute.every(15)
#job.hour.on(12)

cron.write()
