total_Cal = []

with open('deer.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    
    cal = 0
    cal_num = []

    for line in lines:
        if line.strip():
            curCal = int(line)
            cal_num.append(curCal)
            cal += curCal
            
        else:
            total_Cal.append([cal, cal_num.copy()])
            cal_num.clear()
            cal = 0

print(max(total_Cal)) # Day 1 Act 1

sorted_total_Cal = sorted(total_Cal, reverse=True)
print(sorted_total_Cal[0][0]+sorted_total_Cal[1][0]+sorted_total_Cal[2][0]) # Day 2 Act 2
