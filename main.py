import sys
from geometry import *


def main():

    shapes = ShapeList()  # object containing all shapes added by the user
    while True:
        print("""Learn Geometry.
            What do you want to do?
            (1) Add new shape
            (2) Show all shapes
            (3) Show shape with the largest perimeter
            (4) Show shape with the largest area
            (5) Show formulas
            (0) Exit program""")
        option = input("Select an option: ")
        if option == "1":
            shapes.add_shape(input("Add the shape:"))
        elif option == "2":
            ShapeList.get_shapes_table()
        elif option == "3":
            ShapeList.get_largest_shape_by_perimeter()
        elif option == "4":
            ShapeList.get_largest_shape_by_area()
        elif option == "5":
            Shape.get_perimeter_formula()
            Shape.get_area_formula()
        elif option == "0":
            sys.exit()

if __name__ == "__main__":
    main()
