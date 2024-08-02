def main():
    ''' Includes the challenge portion'''
    time = input("What time is it? ")
    realtime = convert(time)

    if 7 <= realtime <= 8:
        print("breakfast time ")
    elif 12 <= realtime <= 13:
        print("lunch time ")
    elif 18 <= realtime <= 19:
        print("dinner time ")
    else:
        pass

def convert(time):
    rawtime = time.split(":")
    hour = int(rawtime[0])
    minutesandstuff = rawtime[1].split(" ")
    minutes = minutesandstuff[0]
    if len(minutesandstuff)> 1:
        if minutesandstuff[1] == 'p.m.':
            hour += 12
    realtime = int(hour) + (int(minutes) / 60)
    return realtime

if __name__ == "__main__":
    main()
