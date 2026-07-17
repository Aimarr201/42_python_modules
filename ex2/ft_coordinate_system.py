
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input("Enter new coordinates as floats "
                            "in format 'x,y,z': ")
        splited_coordinates = coordinates.split(",")

        if len(splited_coordinates) == 3:
            try:
                x = float(splited_coordinates[0])
                y = float(splited_coordinates[1])
                z = float(splited_coordinates[2])
                return x, y, z
            except ValueError:
                for value in splited_coordinates:
                    try:
                        float(value)
                    except ValueError as error:
                        print(f"Error on parameter '{value}': {error}")
                        continue
        else:
            print("Invalid syntax")


def coordinate_system() -> None:
    print("Get a first set of coordinates")
    coordinates = get_player_pos()
    x1, y1, z1 = coordinates
    print(f"Got a first tuple: {coordinates}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance = round((math.sqrt(x1**2 + y1**2 + z1**2)), 4)
    print(f"Distance to center: {distance}\n")

    print("Get a second set of coordinates")
    coordinates = get_player_pos()
    x2, y2, z2 = coordinates
    distance = round((math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("")
    coordinate_system()
