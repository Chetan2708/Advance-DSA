def customJobScheduling(jobs, time_slots):
    n = len(jobs)
    jobs.sort(key=lambda x: x[1], reverse=True)  #NlogN
    result = [False] * time_slots
    total_profit = 0
#balajiit88@gmail.com
    for i in range(n):
        for j in range(min(time_slots - 1, jobs[i][0] - 1), -1, -1):   # N2
            if result[j] == False:
                result[j] = True
                total_profit += jobs[i][1]  #adding profit 
                print(result)
                print(jobs[i][1])
                print(total_profit)
                break
    return total_profit

job_list = [(1, 1000), (4, 500), (3, 300), (7, 700), (6, 900), (7,400), (6,600), (5,800), (2,200) ,(9,150),(8,1200)]
time_slots_available = 11
print(customJobScheduling(job_list, time_slots_available))