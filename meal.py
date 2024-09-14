def main():
    try:
        time = input("What time is it ? Please print in hours:minutes. \n")
        if 7.0 <= convert(time) <= 8.0:
            print("Breakfast time! ")
        elif 12.0 <= convert(time) <= 13.0:
            print("Lunch time! ")
        elif 18.0 <= convert(time) <= 19.0:
            print("Dinner time! ")
        else:
            pass
    except ValueError:
        pass


def convert(time):
    hours, minute = time.split(":")
    hours = float(hours)
    minute = float(minute) * 5 / 3 / 100
    return hours + minute
    


if __name__ == "__main__":
    main()