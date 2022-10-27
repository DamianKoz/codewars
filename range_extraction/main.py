def solution(args):
    result = ""
    last_index = len(args)-1
    i = 0
    while i < (len(args)):   
        temp = []
        current_num = args[i]
        temp.append(current_num)

        # while args[i+1] == args[i]+1 and i < last_index:
        #     temp.append(args[i+1])
        #     i += 1
        #     if i == last_index:
        #         break
        while True:
            next_num = None
            if i < last_index:
                next_num = args[i+1]
            inside_current_num = args[i]
            if next_num == inside_current_num+1:
                temp.append(args[i+1])
            else:
                break
            i += 1
            if i == last_index:
                break

        if len(temp) >=3:
            result += f"{temp[0]}-{temp[len(temp)-1]},"
        else:
            for num in temp:
                result += f"{num},"
        i += 1
    print(f"RESULT: {result}")
            
    # your code here

# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

solution([-63, -60, -57, -55, -54, -53, -52, -50, -48, -47, -46, -44, -43, -42, -39, -38, -36, -35, -32, -30, -29, -26, -25, -22, -21, -18])
#  '-3--1,2,10,15,16,18-20'