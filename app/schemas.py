from app import ma
from .models import Client, ClientSession, Restaurant, RestaurantSession, MenuItem, Order, OrderMenuItem

class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client

class ClientSessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClientSession

class RestaurantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Restaurant

class RestaurantSessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RestaurantSession

class MenuItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MenuItem

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

class OrderMenuItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderMenuItem
