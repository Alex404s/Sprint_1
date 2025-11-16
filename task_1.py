time_all = '1h 45m,360s,25m,30m 120s,2h 60s'

list_of_time = time_all.split(',')

list_of_time_sep = []

for time in list_of_time:
    list_of_time_sep.append(time.split())

list_of_time_m = []

for t_list in list_of_time_sep:
    for time_to_m in t_list:
        if 'h' in time_to_m:
            time_to_m = time_to_m.replace('h','')
            time_to_m = int(time_to_m) * 60
            list_of_time_m.append(time_to_m)

        elif 'm' in time_to_m:
            time_to_m = time_to_m.replace('m','')
            time_to_m = int(time_to_m)
            list_of_time_m.append(time_to_m)

        elif 's' in time_to_m:
            time_to_m = time_to_m.replace('s','')
            time_to_m = int(time_to_m) // 60
            list_of_time_m.append(time_to_m)
    time_all_m = sum(list_of_time_m)   

print(time_all_m)     
    