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
        return "Circle, r " % str(self.r)

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
        return " Triangle, a = %s, b = %s, c= %s" % str(self.a, self.b, self.c)


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        Triangle.__init__(self, a, b=a, c=a)
        if a < 0:
            raise ValueError("Values of parameters can't be negative.")

    def __str__(self):
        return "Equilateral Triangle, a = " + str(self.a)

    def get_area(self):
        s = (self.a+self.b+self.c)/2
        area = math.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))
        return area

    def get_perimeter(self):
        perimeter = self.a+self.b+self.c
        return perimeter


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


class ShapeList:
    def __init__(self):
        pass

    def add_shape(self, shape):
        if not isinstance(shape, Shape):
            raise TypeError
        shapes = []
        shapes.append(shape)
        return shapes

    def get_shapes_table(self, table, title_list):
        # len_for_col = []
        # for title_iterator in range(len(title_list)):
        #     len_col = len(title_list[title_iterator])
        #     for row in table:
        #         if len(row[title_iterator]) > len_col:
        #             len_col = len(row[title_iterator])
        #
        #     len_for_col.append(len_col)
        #
        # how_wide = 0
        # for name in title_list:
        #     x = (len_for_col[title_list.index(name)])
        #     how_wide += (len(("|{: <" + str(x + 2) + "}").format(name)))
        # print('-' * how_wide)
        #
        # for name in title_list:
        #     print("|", end="")
        #     x = (len_for_col[title_list.index(name)])
        #     print(("{: <" + str(x + 2) + "}").format(name), end="")
        # print("|")
        # print('-' * how_wide)
        #
        # for row in table:
        #     print("|", end="")
        #     for element in row:
        #         x = (len_for_col[row.index(element)])
        #         print(("{: <" + str(x + 2) + "}|").format(element), end="")
        #     print()
        # print('-' * how_wide)
        pass

    def get_largest_shape_by_perimeter(self):
        pass

    def get_largest_shape_by_area(self):
        pass
