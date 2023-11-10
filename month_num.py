def main():
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    user_month = str(input("Enter Month Number: "))
    try:
        user_month = int(user_month)
    except ValueError:
        print("please enter an integer")
    else:
        if user_month >= 1 and user_month <= 12:
            print(f"{months[user_month]} is the Month")
        else:
            print("please enter valid month")


if __name__ == "__main__":
    main()
