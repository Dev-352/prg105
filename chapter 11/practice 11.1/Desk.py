import officeFurniture


class Desk(officeFurniture):

    def __init__(self, material, length, width, height, price, location_drawers, number_drawers):
        officeFurniture.__init__(self, material, length, width, height, price)
        self.__location_drawers = location_drawers
        self.__number_drawers = number_drawers

    def set_location_drawers(self, location_drawers):
        self.__location_drawers = location_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_location_drawers(self):
        return self.__location_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    # return string
    def __str__(self):
        desk = ' qty-%d each: $%s total= $%s' % (self.__number_drawers, '{0:,.2f}'.format(self.__price),
                                                 '{0:,.2f}'.format(self.__price * self.__number_drawers))
        return officeFurniture.__str__()+desk
