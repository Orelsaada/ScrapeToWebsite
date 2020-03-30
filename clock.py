from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='Asia/Jerusalem')


# @sched.scheduled_job('interval', seconds=10)
# def timed_job():
#     from main import mainLoop
#     print('test')
    # mainLoop()


@sched.scheduled_job('cron', day_of_week='tue', hour=10, minute=7)
def schedueld_job():
    from main import mainLoop
    mainLoop()


sched.start()

"""
Time on Heroku servers is 3 hours earlier than local (20:00 local => 17:00 heroku).
"""