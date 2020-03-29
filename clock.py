from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


# @sched.scheduled_job('interval', seconds=30)
# def timed_job():
#     from main import mainLoop
#     mainLoop()


@sched.scheduled_job('cron', day_of_week='mon', hour=10)
def schedueld_job():
    from main import mainLoop
    mainLoop()


sched.start()