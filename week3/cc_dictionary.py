inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snowfall(inches_snow):
    total_inches=0
    for inches in inches_snow:
        total_inches=sum(inches_snow.values())
    print("Total snowfall inches:", total_inches)

print_total_snowfall(inches_snow)
thursday_inches=input("How many inches of snow fell on Thursday?",)
inches_snow['Thursday']=int(thursday_inches)
print_total_snowfall(inches_snow)