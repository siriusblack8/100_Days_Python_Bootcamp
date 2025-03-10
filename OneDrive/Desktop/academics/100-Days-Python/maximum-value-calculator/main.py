print("Maximum value finder")
val_list = [int(x) for x in input("Enter the numbers separated by space: ").split()]
max_val = max(val_list)
print(max_val)
#i = len(val_list)
max_value = 0
for y in val_list:
    if y>max_value:
        max_value = y 
    else:
        continue
print(max_value)
