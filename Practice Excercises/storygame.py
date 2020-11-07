vocabulary = {"Quit": "quit exit q",
              "West": "west w",
              "East": "east e",
              "North": "north n",
              "South": "south s"
              }

locations_exits = {
    0: {0: "You have chosen to quit, goodbye.",
        1: "You stand at a cross road.",
        2: "You stand West of the cross roads.",
        3: "You stand East of the cross roads.",
        4: "You stand North of the cross roads.",
        5: "You stand South of the cross roads."
        },
    1: {"Quit": 0,
        "East": 3,
        "West": 2,
        "North": 4,
        "South": 5
        },
    2: {"Quit": 0,
        "East": 3
        },
    3: {"Quit": 0,
        "West": 2
        },
    4: {"Quit": 0,
        "South": 5
        },
    5: {"Quit": 0,
        "North": 4
        }
}


def available_exits():
    print("*" * 7)
    for x in availableExits:
        print("**", x, "**")
    print("*" * 7)


current_loc = 1

while True:
    availableExits = locations_exits[current_loc]
    # print current location
    print(locations_exits[0][current_loc])
    available_exits()
    move = input("Where would you like to go?")

    if current_loc == 0:
        break

    if move in availableExits:
        for key in availableExits.keys():
            print(key)
            continue
