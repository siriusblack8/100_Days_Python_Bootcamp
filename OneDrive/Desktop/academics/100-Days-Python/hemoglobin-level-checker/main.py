print("Hemoglobin level checker")
sex = input("What is your sex assigned at birth? (Male or Female) " )
if sex == "Male":
    hl1 = float(input("What is your hemoglobin level? "))
    if hl1<13.2:
        print("Low hemoglobin level")
    elif hl1>16.6:
        print("Possible blood disorder")
    else:
        print("Normal level")
        
else:
    hl2 = float(input("What is your hemoglobin level? "))
    if hl2<11.6:
        print("Low hemoglobin level")
    elif hl2>15:
        print("Possible blood disorder")
    else:
        print("Normal level")
