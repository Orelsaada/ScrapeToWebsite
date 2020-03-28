from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=30)
def timed_job():
    from main import mainLoop
    mainLoop()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=2)
def schedueld_job():
    print("Every day at 2.")


sched.start()