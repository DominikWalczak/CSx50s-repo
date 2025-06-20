import re
import sys


def main():
    answer = convert(input("Hours: "))
    if answer == "ValueError":
        print("ValueError")
        sys.exit(1)
    print(f"{answer}")


def convert(s):
    tab = s.split()
    hour = [0, 0]
    try:
        if len(tab) == 5:
            if len(tab[0].replace(':', ' ').split()) == 2 and len(tab[3].replace(':', ' ').split()) == 2 and tab[2] == "to" and (tab[1] == "AM" or tab[1] == "PM") and (tab[4] == "AM" or tab[4] == "PM"):
                    if tab[1] == "AM":
                        first = tab[0].replace(':', ' ').split()
                        if int(first[0]) <= 12 and int(first[1]) < 60 and int(first[1]) >= 0:
                            if int(first[0]) == 12:
                                hour[0] = "00:" + first[1]
                            else:
                                if int(first[0]) < 10:
                                    first[0] = int(first[0])
                                    hour[0] = "0" + str(first[0])+ ":" + first[1]
                                else:
                                    hour[0] = first[0]+ ":" + first[1]
                        else:
                            raise ValueError
                    elif tab[1] == "PM":
                        second = tab[0].replace(':', ' ').split()
                        if int(second[0]) <= 12 and int(second[1]) < 60 and int(second[1]) >= 0:
                            if int(second[0]) == 12:
                                hour[1] = "12:" + second[1]
                            else:
                                second[0] = int(second[0]) + 12
                                hour[0] =  str(second[0]) + ":" + str(second[1])
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                    if tab[4] == "AM":
                        first = tab[3].replace(':', ' ').split()
                        if int(first[0]) <= 12 and int(first[1]) < 60 and int(first[1]) >= 0:
                            if int(first[0]) == 12:
                                hour[1] = "00:" + first[1]
                            else:
                                if int(first[0]) < 10:
                                    first[0] = int(first[0])
                                    hour[1] = "0" + str(first[0])+ ":" + first[1]
                                else:
                                    hour[1] = first[0]+ ":" + first[1]
                        else:
                            raise ValueError
                    elif tab[4] == "PM":
                        second = tab[3].replace(':', ' ').split()
                        if int(second[0]) <= 12 and int(second[1]) < 60 and int(second[1]) >= 0:
                            if int(second[0]) == 12:
                                hour[1] = "12:" + second[1]
                            else:
                                second[0] = int(second[0]) + 12
                                hour[1] =  str(second[0]) + ":" + second[1]
                        else:
                            raise ValueError
                    else:
                        raise ValueError


            elif len(tab[0].replace(':', ' ').split()) == 1 and len(tab[3].replace(':', ' ').split()) == 1 and tab[2] == "to" and (tab[1] == "AM" or tab[1] == "PM") and (tab[4] == "AM" or tab[4] == "PM"):

                        if tab[1] == "AM":
                            first = tab[0].replace(':', ' ').split()
                            if int(first[0]) <= 12:
                                if int(first[0]) == 12:
                                    hour[0] = "00:00"
                                else:
                                    if int(first[0]) < 10:
                                        hour[0] = "0" + first[0]+ ":00"
                                    else:
                                        hour[0] = first[0]+ ":00"
                            else:
                                raise ValueError
                        elif tab[1] == "PM":
                            second = tab[0].replace(':', ' ').split()
                            if int(second[0]) <= 12:
                                if int(second[0]) == 12:
                                    hour[0] = "12:00"
                                else:
                                    second[0] = int(second[0]) + 12
                                    hour[0] =  str(second[0]) + ":00"
                            else:
                                raise ValueError
                        else:
                            raise ValueError
                        if tab[4] == "AM":
                            first = tab[3].replace(':', ' ').split()
                            if int(first[0]) <= 12:
                                if int(first[0]) == 12:
                                    hour[1] = "00:00"
                                else:
                                    if int(first[0]) < 10:
                                        hour[1] = "0" + first[0]+ ":00"
                                    else:
                                        hour[1] = first[0]+ ":00"
                            else:
                                raise ValueError
                        elif tab[4] == "PM":
                            second = tab[3].replace(':', ' ').split()
                            if int(second[0]) <= 12:
                                if int(second[0]) == 12:
                                    hour[1] = "12:00"
                                else:
                                    if int(second[0]) < 10:
                                        second[0] = int(second[0]) + 12
                                        hour[1] = str(second[0]) + ":00"
                                    else:
                                        hour[1] = second[0] + ":00"
                            else:
                                raise ValueError
                        else:
                            raise ValueError

            else:
                raise ValueError
        else:
            raise ValueError
        return str(hour[0]) + " " + tab[2] + " " + str(hour[1])




    except ValueError:
        return "ValueError"


if __name__ == "__main__":
    main()
