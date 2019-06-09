import random

def dice(str): #message.content.strip("!r")

    str = str.strip()
    try:
        separate = str.split("+",2)
    except:
        separate = [str]
    print(separate)
    nums = separate[0].split('d')
    try:
        mod = int(separate[1])
    except:
        mod = ""

    if int(nums[0])>100 or int(nums[1])>100:
        return "``` Overflow Error ```"

    rolls = []
    sum = 0
    for _ in range(int(nums[0])):
        roll = random.randint(1,int(nums[1]))
        rolls.append(roll)
        sum += roll

    outStuff = "``` "
    for x in rolls:
        outStuff += "{} + ".format(x)
    if mod is not "":
        outStuff += "{} ".format(mod)
        sum += mod
    else:
        outStuff = outStuff[:-2]
    outStuff += "= {} ```".format(sum)

    return outStuff

#dice(" 4 d 10 + 1")