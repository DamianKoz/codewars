def format_duration(seconds):
    if not seconds:
        return "now"
    print(seconds)
    secs = seconds % 60 #!
    seconds -= secs
    minutes = seconds // 60
    mins = minutes % 60 #!
    minutes -= mins
    hours = minutes // 60
    hrs = hours % 24
    hours -=hrs
    days = hours // 24
    dys = days % 365
    days-=dys
    years = days // 356
    yrs = years 

    print(secs, mins, hrs, dys)
    result =format_result([secs, mins,hrs,dys, yrs])
    print(result)
    return result

def format_result(nums):
    units = ["second", "minute", "hour", "day", "year"]
    print(f"\nNUMS: {nums}")
    result = ""
    index_of_last_item = get_index_of_last_item(nums)
    for i in range(len(nums)-1,-1,-1):
        time = nums[i]
        if not time:
            continue
        if result == "":
            pass
        elif i == index_of_last_item: 
            result += " and "
        else:
            result += ", "
        if time:
            time_unit = units[i]
            amount = nums[i]
            result += f"{amount} {time_unit}"
        if time > 1:
            result +="s"

    return result
    
def get_index_of_last_item(nums):
    for i in range(len(nums)):
        if nums[i]:
            return i

# format_duration(1) #, "1 second"
# format_duration(62) # "1 minute and 2 seconds"

format_duration(253374061) # '8 years, 12 days, 13 hours, 41 minutes and 1 second'