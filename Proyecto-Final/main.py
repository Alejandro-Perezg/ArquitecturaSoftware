import flask
from controller.item_controller import ItemController
from repository.item_repository import ItemRepository
import psycopg2
from flask import render_template, request, redirect, jsonify

def create_app():
    app = flask.Flask(__name__)
    connection = psycopg2.connect("host=localhost dbname=my_database user=jvnko password=1234")
    item_repository = ItemRepository(connection)
    item_controller = ItemController(item_repository)

    @app.route('/', methods=['GET'])
    def show_items():
        items = item_repository.get_items()
        return render_template('index.html', items=items)

    @app.route('/item/<sku>/convert', methods=['GET'])
    def convert_currency(sku):
        currency = request.args.get('currency')
        return item_controller.changeCurrency(sku, currency)

    @app.route('/item', methods=['GET'])
    def get_items():
        return item_controller.getItems()

    @app.route('/item', methods=['POST'])
    def add_item():
        item_data = request.get_json()
        return item_controller.add_item(item_data)

    @app.route('/item/<sku>', methods=['DELETE'])
    def delete_item(sku):
        item_controller.deleteItem(sku)
        return redirect('/')

    @app.route('/item/add', methods=['GET'])
    def add_item_view():
        return render_template('add.html')

    @app.route('/item/<sku>/edit', methods=['GET'])
    def edit_item_view(sku):
        item = item_repository.get_item(sku)
        if item:
            return render_template('edit.html', item=item)
        else:
            return 'item not present'

    @app.route('/item/<sku>/delete', methods=['GET'])
    def delete_item_view(sku):
        item = item_repository.get_item(sku)
        if item:
            return render_template('delete.html', item=item)
        else:
            return 'item is not present'

    return app

if __name__ == '__main__':
    create_app().run(debug=True, port=5050)
