def main():
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }
    while True:
        date = input("Date:")
        date = date.strip()
        if date.count(",") == 0 and date.count("/") == 0:
            continue
        if date.count("/") == 1:
            continue
        if date.count(",") == 1:
            datelist = date.split(" ")
            mnth = datelist.pop(0)
            dy = datelist.pop(0)
            if mnth.strip().isnumeric():
                continue
        if date.count("/") == 2:
            datelist = date.split("/")
            mnth = datelist.pop(0)
            dy = datelist.pop(0)
            if mnth.isalpha():
                continue
        if "," in dy:
            daylist = dy.split(",")
            dy = daylist.pop(0)
        yr = datelist.pop(0)
        if mnth in months.keys():
            mnth = months[mnth]
        dy = int(dy)
        mnth = int(mnth)
        if mnth > 12:
            continue
        if dy > 31:
            continue
        print(f"{yr}-{mnth:02}-{dy:02}", end="")
        break


main()
