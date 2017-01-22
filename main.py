import sys
import collections
from geometry import *


def main():
    shapes = ShapeList()  # object containing all shapes added by the user
    shapes_dict_unsorted = {"1": Square, "2": Circle, "3": Triangle, "4": EquilateralTriangle, "5": Rectangle,
                            "6": RegularPentagon}
    shapes_dict = collections.OrderedDict(sorted(shapes_dict_unsorted.items()))

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
            shape_type = select_shape(shapes_dict)
            shape = shape_type.from_input()
            shapes.add_shape(shape)
        elif option == "2":
            print(shapes.get_shapes_table())
        elif option == "3":
            largest_shape = shapes.get_largest_shape_by_perimeter()
            print("Largest shape is %s with id: %s" % (largest_shape, largest_shape.idx))
        elif option == "4":
            largest_shape = shapes.get_largest_shape_by_area()
            print("Largest shape is %s with id: %s" % (largest_shape, largest_shape.idx))
        elif option == "5":
            shape_type = select_shape(shapes_dict)
            print(shape_type.get_area_formula())
            print(shape_type.get_perimeter_formula())
        elif option == "0":
            sys.exit()


def select_shape(shapes_dict):
    """
    Display all type of shape object for user.

    Args: shapes_dict
    Return:
        type of shape object
    """
    for k, v in shapes_dict.items():
        print('%s - %s' % (k, v.__name__))
    choose = input("Select number of shape: ")
    shape_type = shapes_dict[choose]
    return shape_type


if __name__ == "__main__":
    main()
