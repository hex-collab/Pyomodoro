from datetime import *
import winsound
def alarm():
    winsound.Beep(440, 2000)
def time_manager():
    x = 0
    start_time=datetime.today()
    end_time=start_time+timedelta(seconds=1)
    timer=datetime.today()
    while(end_time>=timer):
        if(timer==end_time):
             x = x + 1
        timer=datetime.today()
    return True
def timer(alloted_time,task_interval_duration,break_duration):
    interval_duration = 0
    check_marks = 0
    mins = 0
    while mins < alloted_time:
        if(time_manager()):
            mins = mins + 1
            interval_duration = interval_duration + 1
        if interval_duration == task_interval_duration:
            alarm()
            print("Break time!")
            mins = mins + break_duration
            check_marks = check_marks + 1
            print("Total time : %d "% (mins))
            print("Total intervals completed : %d"%(check_marks))
            interval_duration = 0
            print("Check marks : "+(" * ") * check_marks)
    print("Total time spend: %d "% (mins))
    print("Total break time: %d"%(check_marks * break_duration))
    print("Total time spend on the task: %d"%(mins - (check_marks * break_duration)))
alloted_time = int(input("Total time to spend(in hours):"))
task_interval_duration = int(input("Time to spend on an interval:"))
break_duration = int(input("Break duration:"))
alloted_time = alloted_time * 60
timer(alloted_time,task_interval_duration,break_duration)
