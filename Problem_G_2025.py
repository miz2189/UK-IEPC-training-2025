

ncases = int(input())

store_cases =[0]*ncases

for i in range(ncases):
    inp = list(map(int,input().split()))
    store_cases[i] = inp

points = 0

for day_left, nt_points, t_points, fresh_days, break_days in store_cases:
    if day_left <= fresh_days:
        print(day_left*nt_points)
    elif (day_left -fresh_days) <= break_days:
        print(fresh_days*nt_points + (day_left - fresh_days)*t_points)
    elif nt_points == t_points:
         print(day_left*t_points)
       

    else:
        points = []
        points.append(fresh_days*nt_points + (day_left - fresh_days)*t_points)
        
    
        #full day, break , full day , break 
        d_copy = day_left

        point = 0
        tire = False
        fday = 0 #counts how many fresh days have been used
        cycle = day_left//(fresh_days+break_days)
        rem = day_left%(fresh_days+break_days)
        if rem == 0:
            point = cycle * nt_points * fresh_days + t_points * break_days
        else:
             point = cycle * nt_points * fresh_days
        day_left = day_left - cycle * (fresh_days+break_days)

        if day_left <= fresh_days:
                point += day_left*nt_points
        elif (day_left -fresh_days) <= break_days:
            point += fresh_days*nt_points + (day_left - fresh_days)*t_points

        points.append(point)
        
        #check n-1 case
        cycle = d_copy//(fresh_days+break_days) - 1
        rem = d_copy%(fresh_days+break_days)
        
        
        point = cycle * nt_points * fresh_days + (rem + break_days) * t_points + fresh_days * nt_points

        points.append(point)
        
        
        #calculating all possibilites and getting the max from possible answers
        print(max(points))



