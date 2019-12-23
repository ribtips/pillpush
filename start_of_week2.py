#!/usr/bin/python3

import time
import json

def start_of_week():
  #current_time = time.gmtime()
  current_time = time.localtime()
  current_epoch = int(time.time())
  week_start_epoch = current_epoch - (current_time[6] * 3600 * 24 + current_time[3] * 3600 + current_time[4] * 60 + current_time[5])
  #week_start_time = time.strftime('%m/%d/%Y %H:%M:%S',time.gmtime(week_start_epoch))
  week_start_time = time.strftime('%m/%d/%Y %H:%M:%S',time.localtime(week_start_epoch))
  #current_time = time.strftime('%m/%d/%Y %H:%M:%S',time.gmtime(current_epoch))
  current_time = time.strftime('%m/%d/%Y %H:%M:%S',time.localtime(current_epoch))
  print("Current time: ",current_time);
  print("\nWeek Start: ",week_start_time);
  print("\n")
  return week_start_epoch

#def define_days(week_start_epoch,test_epoch):
def define_days(week_start_epoch):
  half_day = 43200
  last_week = 604800
  day_times = {
   "CurrMonAM":{'start':week_start_epoch,'end':week_start_epoch + half_day * 1 - 1,'match':"NoMatch",'current':0},
   "CurrMonPM":{'start':week_start_epoch + half_day * 1 ,'end':week_start_epoch + half_day * 2 - 1,'match':"NoMatch",'current':0},
   "CurrTueAM":{'start':week_start_epoch + half_day * 2 ,'end':week_start_epoch + half_day * 3 - 1,'match':"NoMatch",'current':0},
   "CurrTuePM":{'start':week_start_epoch + half_day * 3 ,'end':week_start_epoch + half_day * 4 - 1,'match':"NoMatch",'current':0},
   "CurrWedAM":{'start':week_start_epoch + half_day * 4 ,'end':week_start_epoch + half_day * 5 - 1,'match':"NoMatch",'current':0},
   "CurrWedPM":{'start':week_start_epoch + half_day * 5 ,'end':week_start_epoch + half_day * 6 - 1,'match':"NoMatch",'current':0},
   "CurrThuAM":{'start':week_start_epoch + half_day * 6 ,'end':week_start_epoch + half_day * 7 - 1,'match':"NoMatch",'current':0},
   "CurrThuPM":{'start':week_start_epoch + half_day * 7 ,'end':week_start_epoch + half_day * 8 - 1,'match':"NoMatch",'current':0},
   "CurrFriAM":{'start':week_start_epoch + half_day * 8 ,'end':week_start_epoch + half_day * 9 - 1,'match':"NoMatch",'current':0},
   "CurrFriPM":{'start':week_start_epoch + half_day * 9 ,'end':week_start_epoch + half_day * 10 - 1,'match':"NoMatch",'current':0},
   "CurrSatAM":{'start':week_start_epoch + half_day * 10 ,'end':week_start_epoch + half_day * 11 - 1,'match':"NoMatch",'current':0},
   "CurrSatPM":{'start':week_start_epoch + half_day * 11 ,'end':week_start_epoch + half_day * 12 - 1,'match':"NoMatch",'current':0},
   "CurrSunAM":{'start':week_start_epoch + half_day * 12 ,'end':week_start_epoch + half_day * 13 - 1,'match':"NoMatch",'current':0},
   "CurrSunPM":{'start':week_start_epoch + half_day * 13 ,'end':week_start_epoch + half_day * 14 - 1,'match':"NoMatch",'current':0},
   "PrevMonAM":{'start':week_start_epoch - last_week,'end':week_start_epoch + half_day * 1 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevMonPM":{'start':week_start_epoch + half_day * 1 - last_week,'end':week_start_epoch + half_day * 2 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevTueAM":{'start':week_start_epoch + half_day * 2 - last_week,'end':week_start_epoch + half_day * 3 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevTuePM":{'start':week_start_epoch + half_day * 3 - last_week,'end':week_start_epoch + half_day * 4 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevWedAM":{'start':week_start_epoch + half_day * 4 - last_week,'end':week_start_epoch + half_day * 5 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevWedPM":{'start':week_start_epoch + half_day * 5 - last_week,'end':week_start_epoch + half_day * 6 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevThuAM":{'start':week_start_epoch + half_day * 6 - last_week,'end':week_start_epoch + half_day * 7 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevThuPM":{'start':week_start_epoch + half_day * 7 - last_week,'end':week_start_epoch + half_day * 8 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevFriAM":{'start':week_start_epoch + half_day * 8 - last_week,'end':week_start_epoch + half_day * 9 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevFriPM":{'start':week_start_epoch + half_day * 9 - last_week,'end':week_start_epoch + half_day * 10 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevSatAM":{'start':week_start_epoch + half_day * 10 - last_week,'end':week_start_epoch + half_day * 11 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevSatPM":{'start':week_start_epoch + half_day * 11 - last_week,'end':week_start_epoch + half_day * 12 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevSunAM":{'start':week_start_epoch + half_day * 12 - last_week,'end':week_start_epoch + half_day * 13 - 1 - last_week,'match':"NoMatch",'current':0},
   "PrevSunPM":{'start':week_start_epoch + half_day * 13 - last_week,'end':week_start_epoch + half_day * 14 - 1 - last_week,'match':"NoMatch",'current':0},
  }
  return day_times

def check_times(day_times,the_time):
 for tod,time_range in day_times.items(): 
  if (the_time >= time_range['start'] and the_time <= time_range['end']):
   time_range['match'] = time.strftime('%m/%d/%Y %H:%M:%S',time.localtime(the_time))
   time_range['current'] = 1
   print(time_range['match']," is a match in: ",tod,"which is between",time_range['start'],"and",time_range['end'])
   break
 #return day_times
   
def get_times():
 fp = open('status.txt')
 button_presses = []
 week_start_epoch = start_of_week()
 while True:
  line = fp.readline()
  if "---" in line:
   time_from_file = line.split()
#   define_days(week_start_epoch,18000+int(time_from_file[2]))
   button_presses.append(18000+int(time_from_file[2]))
  if not line:
   break
 return button_presses


week_start_epoch = start_of_week()
day_times = define_days(week_start_epoch)
button_presses = get_times()
for the_time in button_presses:
 if (the_time > week_start_epoch - 604800):
#  print("The time I got was: ",the_time)
  check_times(day_times,the_time) 

day_times_json = json.dumps(day_times)
with open('data.json','w') as outfile:
 json.dump(day_times_json,outfile)





