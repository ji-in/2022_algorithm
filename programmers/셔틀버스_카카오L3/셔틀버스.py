from collections import defaultdict

def make_time(t):
    hour, minute = t//60, t%60
    return str(hour).zfill(2) + ':' + str(minute).zfill(2)

def solution(n, t, m, timetable):
    answer = ''
    # 1. timetable 정렬
    crews = []
    for time in timetable:
        hour, minute = int(time[:2]), int(time[3:])
        crews.append(60*hour+minute)
    crews.sort()
    # 2. 셔틀버스 시간대 결정
    buses = defaultdict(list)
    bus_start = 60*9 # 9:00
    bus_timetable = []
    for i in range(n):
        buses[bus_start] = []
        bus_timetable.append(bus_start)
        bus_start += t

    for crew in crews:
        for bus in buses:
            if crew <= bus and len(buses[bus]) < m:
                buses[bus].append(crew)
                break

    late_time = bus_timetable[-1]
    if len(buses[late_time]) < m: # 버스 자리 남을 때
        return make_time(late_time)
    else:
        time = 0
        crew_list = buses[late_time]
        if m == 1:
            time = crew_list[0] - 1
        else:
            time = crew_list[m-2]
            if time < late_time:
                time = late_time
            if time >= crew_list[m-1]:
                time = crew_list[m-1] - 1
        return make_time(time)