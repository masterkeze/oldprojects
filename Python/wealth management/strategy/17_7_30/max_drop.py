values = [1,3,2,4,5,6,7,5,6,8,9,6,7,6,3,5,7]

temp_high = None
temp_low = None
temp_drop = 0
for v in values:
    if temp_high == None:
        temp_high = v
        temp_low = v
        temp_drop = 0
        continue
    if v < temp_high:
        temp_low = min(temp_low,v)
        temp_drop = max((temp_high - temp_low)/temp_high,temp_drop)
    else:
        temp_low = v
        temp_high = v

print(temp_drop)
    
