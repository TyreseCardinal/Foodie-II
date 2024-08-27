from flask import request, jsonify
from app import db, api
from .models import Client, ClientSession, Restaurant, RestaurantSession, MenuItem, Order, OrderMenuItem
from .schemas import (
    ClientSchema, ClientSessionSchema, RestaurantSchema, RestaurantSessionSchema,
    MenuItemSchema, OrderSchema, OrderMenuItemSchema
)
from flask_restful import Resource

# Client routes
class ClientResource(Resource):
    def get(self):
        clients = Client.query.all()
        return jsonify(ClientSchema(many=True).dump(clients))

    def post(self):
        data = request.json
        new_client = Client(**data)
        db.session.add(new_client)
        db.session.commit()
        return jsonify(ClientSchema().dump(new_client)), 201

class ClientDetailResource(Resource):
    def delete(self, id):
        client = Client.query.get_or_404(id)
        db.session.delete(client)
        db.session.commit()
        return '', 204

    def patch(self, id):
        client = Client.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(client, key, value)
        db.session.commit()
        return jsonify(ClientSchema().dump(client))

api.add_resource(ClientResource, '/api/clients')
api.add_resource(ClientDetailResource, '/api/clients/<int:id>')

# Client Session routes
class ClientSessionResource(Resource):
    def get(self):
        sessions = ClientSession.query.all()
        return jsonify(ClientSessionSchema(many=True).dump(sessions))

    def post(self):
        data = request.json
        new_session = ClientSession(**data)
        db.session.add(new_session)
        db.session.commit()
        return jsonify(ClientSessionSchema().dump(new_session)), 201

api.add_resource(ClientSessionResource, '/api/client_sessions')

# Restaurant routes
class RestaurantResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        return jsonify(RestaurantSchema(many=True).dump(restaurants))

    def post(self):
        data = request.json
        new_restaurant = Restaurant(**data)
        db.session.add(new_restaurant)
        db.session.commit()
        return jsonify(RestaurantSchema().dump(new_restaurant)), 201

class RestaurantDetailResource(Resource):
    def delete(self, id):
        restaurant = Restaurant.query.get_or_404(id)
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204

    def patch(self, id):
        restaurant = Restaurant.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(restaurant, key, value)
        db.session.commit()
        return jsonify(RestaurantSchema().dump(restaurant))

api.add_resource(RestaurantResource, '/api/restaurants')
api.add_resource(RestaurantDetailResource, '/api/restaurants/<int:id>')

# Restaurant Session routes
class RestaurantSessionResource(Resource):
    def get(self):
        sessions = RestaurantSession.query.all()
        return jsonify(RestaurantSessionSchema(many=True).dump(sessions))

    def post(self):
        data = request.json
        new_session = RestaurantSession(**data)
        db.session.add(new_session)
        db.session.commit()
        return jsonify(RestaurantSessionSchema().dump(new_session)), 201

api.add_resource(RestaurantSessionResource, '/api/restaurant_sessions')

# Menu Item routes
class MenuItemResource(Resource):
    def get(self):
        menu_items = MenuItem.query.all()
        return jsonify(MenuItemSchema(many=True).dump(menu_items))

    def post(self):
        data = request.json
        new_menu_item = MenuItem(**data)
        db.session.add(new_menu_item)
        db.session.commit()
        return jsonify(MenuItemSchema().dump(new_menu_item)), 201

class MenuItemDetailResource(Resource):
    def delete(self, id):
        menu_item = MenuItem.query.get_or_404(id)
        db.session.delete(menu_item)
        db.session.commit()
        return '', 204

    def patch(self, id):
        menu_item = MenuItem.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(menu_item, key, value)
        db.session.commit()
        return jsonify(MenuItemSchema().dump(menu_item))

api.add_resource(MenuItemResource, '/api/menu_items')
api.add_resource(MenuItemDetailResource, '/api/menu_items/<int:id>')

# Order routes
class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        return jsonify(OrderSchema(many=True).dump(orders))

    def post(self):
        data = request.json
        new_order = Order(**data)
        db.session.add(new_order)
        db.session.commit()
        return jsonify(OrderSchema().dump(new_order)), 201

class OrderDetailResource(Resource):
    def delete(self, id):
        order = Order.query.get_or_404(id)
        db.session.delete(order)
        db.session.commit()
        return '', 204

    def patch(self, id):
        order = Order.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(order, key, value)
        db.session.commit()
        return jsonify(OrderSchema().dump(order))

api.add_resource(OrderResource, '/api/orders')
api.add_resource(OrderDetailResource, '/api/orders/<int:id>')

# Order Menu Item routes
class OrderMenuItemResource(Resource):
    def get(self):
        order_menu_items = OrderMenuItem.query.all()
        return jsonify(OrderMenuItemSchema(many=True).dump(order_menu_items))

    def post(self):
        data = request.json
        new_order_menu_item = OrderMenuItem(**data)
        db.session.add(new_order_menu_item)
        db.session.commit()
        return jsonify(OrderMenuItemSchema().dump(new_order_menu_item)), 201

api.add_resource(OrderMenuItemResource, '/api/order_menu_items')
