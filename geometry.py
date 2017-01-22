import math


class Shape:
    """
    This is a abstract class representing geometrical shape.
    """

    def __init__(self):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        pass

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        pass

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        pass

    def set_id(self, idx):
        """
        Set id number for shape objects.

        Parameter: idx:
        Return:
            int
        """
        self.idx = idx

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information bout shape
        """
        pass

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.

        Returns:
            str: area formula
        """
        pass

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.

        Returns:
            str: perimeter formula
        """
        pass

    @classmethod
    def from_input(cls):
        """
        Returns new shape with all parameters from user input.

        Returns:
            new shape object
        """
        pass


class Circle(Shape):
    def __init__(self, r):
        Shape.__init__(self)
        self.r = r
        if r < 0:
            raise ValueError("Values of parameters can't be negative.")

    def get_area(self):
        area = math.pi*self.r**2
        return area

    def get_perimeter(self):
        perimeter = 2*math.pi*self.r
        return perimeter

    def __str__(self):
        return "Circle, r = %s" % str(self.r)

    @classmethod
    def get_area_formula(cls):
        return "Area formula: π×r**2"

    @classmethod
    def get_perimeter_formula(cls):
        return "Perimeter formula: 2×π×r"

    @classmethod
    def from_input(cls):
        r = read_digit_from_input("Set r: ")
        return Circle(r)


class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        if a < 0 or b < 0 or c < 0:
            raise ValueError("Values of parameters can't be negative.")

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return area

    def get_perimeter(self):
        perimeter = self.a+self.b+self.c
        return perimeter

    def __str__(self):
        return "Triangle, a = %s, b = %s, c= %s" % (self.a, self.b, self.c)

    @classmethod
    def get_area_formula(cls):
        return "Area formula: (s(s-a)**2(s-b)(s-c))"

    @classmethod
    def get_perimeter_formula(cls):
        return "Perimeter formula: a + b + c"

    @classmethod
    def from_input(cls):
        a = read_digit_from_input("Set a: ")
        b = read_digit_from_input("Set b: ")
        c = read_digit_from_input("Set c: ")
        return Triangle(a, b, c)


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        Triangle.__init__(self, a, b=a, c=a)
        if a < 0:
            raise ValueError("Values of parameters can't be negative.")

    def get_area(self):
        s = (self.a+self.b+self.c)/2
        area = math.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))
        return area

    def get_perimeter(self):
        perimeter = self.a+self.b+self.c
        return perimeter

    def __str__(self):
        return "Equilateral Triangle, a = " + str(self.a)

    @classmethod
    def get_area_formula(cls):
        return "Area formula: (s(s-a)**2(s-b)(s-c))"

    @classmethod
    def get_perimeter_formula(cls):
        return "Perimeter formula: a + a + a"

    @classmethod
    def from_input(cls):
        a = read_digit_from_input("Set a: ")
        return EquilateralTriangle(a)


class Rectangle(Shape):
    def __init__(self, a, b):
        Shape.__init__(self)
        self.a = a
        self.b = b
        if a < 0 or b < 0:
            raise ValueError("Values of parameters can't be negative.")

    def get_area(self):
        area = self.a*self.b
        return area

    def get_perimeter(self):
        perimeter = 2*self.a + 2*self.b
        return perimeter

    def __str__(self):
        return "Rectangle, a = %s, b = %s" % (self.a, self.b)

    @classmethod
    def get_area_formula(cls):
        return "Area formula = a×b"

    @classmethod
    def get_perimeter_formula(cls):
        return "Perimeter formula = 2a + 2b"

    @classmethod
    def from_input(cls):
        a = read_digit_from_input("Set a: ")
        b = read_digit_from_input("Set b: ")
        return Rectangle(a, b)


class Square(Rectangle):

    def __init__(self, a):
        Rectangle.__init__(self, a, b=a)
        if a < 0:
            raise ValueError("Values of parameters can't be negative.")

    def get_area(self):
        area = self.a**2
        return area

    def get_perimeter(self):
        perimeter = self.a * 4
        return perimeter

    def __str__(self):
        return "Square: a = %s" % self.a

    @classmethod
    def get_area_formula(cls):
        return "Area formula: a**2"

    @classmethod
    def get_perimeter_formula(cls):
        return "Perimeter formula: a*4"

    @classmethod
    def from_input(cls):
        a = read_digit_from_input("Set a: ")
        return Square(a)


class RegularPentagon(Shape):
    def __init__(self, a):
        Shape.__init__(self)
        self.a = a
        if a < 0:
            raise ValueError("Values of parameters can't be negative.")

    def get_area(self):
        area = self.a**2 * math.sqrt(5*(5+2*math.sqrt(5)))/4
        return area

    def get_perimeter(self):
        perimeter = 5 * self.a
        return perimeter

    def __str__(self):
        return "Pentagon, a = %s" % self.a

    @classmethod
    def get_area_formula(cls):
        return "Area formula: a**2*(5*(5+2*(5)**2)**2)/4"

    @classmethod
    def get_perimeter_formula(cls):
        return "Perimeter formula: 5a"

    @classmethod
    def from_input(cls):
        a = read_digit_from_input("Set a: ")
        return RegularPentagon(a)


class ShapeList:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """
        Method adds new shape object to list of shapes.

        Parameter: shape
        Raises:
            TypeError: If shape's hasn't Shape class as it's ancestor.
        """
        if isinstance(shape, Shape):
            self.shapes.append(shape)
            shape.set_id(len(self.shapes))
        else:
            raise TypeError

    def get_shapes_table(self):
        """
        Method prints table to console.

        Return:
            str: table
        """
        table = ""
        title_list = ["id", "Class", "__str__", "Perimeter", "Perimeter formula", "Area", "Area formula"]
        len_for_col = []
        for title_iterator in range(len(title_list)):
            len_col = len(title_list[title_iterator])
            len_for_col.append(len_col)

        for shape in self.shapes:
            col = 0
            for data_len in self.get_data_len(shape):
                if data_len > len_for_col[col]:
                    len_for_col[col] = data_len
                col += 1

        how_wide = 1
        for col_len in len_for_col:
            how_wide += col_len + 3
        print('-' * how_wide)

        for title in title_list:
            print("|", end="")
            x = (len_for_col[title_list.index(title)])
            print(("{: <" + str(x + 2) + "}").format(title), end="")
        print("|")
        print('-' * how_wide)

        for shape in self.shapes:
            print("|", end="")
            x = len_for_col[0]
            print(("{: <" + str(x + 2) + "}|").format(shape.idx), end="")
            x = len_for_col[1]
            print(("{: <" + str(x + 2) + "}|").format(type(shape).__name__), end="")
            x = len_for_col[2]
            print(("{: <" + str(x + 2) + "}|").format(shape.__str__()), end="")
            x = len_for_col[3]
            print(("{: <" + str(x + 2) + "}|").format(shape.get_perimeter()), end="")
            x = len_for_col[4]
            print(("{: <" + str(x + 2) + "}|").format(shape.get_perimeter_formula()), end="")
            x = len_for_col[5]
            print(("{: <" + str(x + 2) + "}|").format(shape.get_area()), end="")
            x = len_for_col[6]
            print(("{: <" + str(x + 2) + "}|").format(shape.get_area_formula()))
        print('-' * how_wide)
        return table

    @staticmethod
    def get_data_len(shape):
        """
        Method returns length all of shape elements to build a proper table.

        Parameter: shape
        Returns:
            list of elements lengths as int
        """
        elements_len = []

        len_idx = len(str(shape.idx))
        len_class = len(type(shape).__name__)
        len_str = len(shape.__str__())
        len_perimeter = len(str(shape.get_perimeter()))
        len_perimeter_formula = len(str(shape.get_perimeter_formula()))
        len_area = len(str(shape.get_area()))
        len_area_formula = len(str(shape.get_area_formula()))

        elements_len.append(len_idx)
        elements_len.append(len_class)
        elements_len.append(len_str)
        elements_len.append(len_perimeter)
        elements_len.append(len_perimeter_formula)
        elements_len.append(len_area)
        elements_len.append(len_area_formula)

        return elements_len

    def get_largest_shape_by_area(self):
        """
        Checks for shape with larges area.

        Return:
            shape with largest area
        """
        largest_area = self.shapes[0]
        for figure in self.shapes:
            if figure.get_area() > largest_area.get_area():
                largest_area = figure
        return largest_area

    def get_largest_shape_by_perimeter(self):
        """
        Checks for shape with larges perimeter.

        Return:
            shape with largest perimeter
        """
        largest_perimeter = self.shapes[0]
        for figure in self.shapes:
            if figure.get_perimeter() > largest_perimeter.get_perimeter():
                largest_perimeter = figure
        return largest_perimeter


def read_digit_from_input(label):
    """
    Method read input from user and validate it.

    Parameter: label
    Return:
        digit: validate user input
    """
    a = 0
    is_valid = False
    while not is_valid:
        a_str = input(label)
        if a_str.isdigit():
            a = int(a_str)
            if a > 0:
                is_valid = True
    return a
