from flask import Flask, request, render_template, jsonify, redirect
import repository

app = Flask(__name__)
repository = repository.data

@app.route('/item', methods = ['GET'])
def getItems():
    return render_template('controller.html', myList = repository )

@app.route('/item', methods = ['POST'])
def postItem():
    new_item = {
        'SKU': request.form['sku'],
        'name': request.form['name'],
        'description': request.form['description'],
        'price': request.form['price'],
        'quantity': request.form['quantity'],
        'expdate': request.form['expdate']
    }
    
    repository.append(new_item)
    return render_template('controller.html', myList = repository )
    # sku = request.form['sku']
    # name = request.form['name']
    # description = request.form['description']
    # price = request.form['price']
    # quantity = request.form['quantity']
    # expdate = request.form['expdate']

    # newItem={'SKU':sku, 'Name':name, 'Description': description, 'Price': price,'Quantity': quantity, 'Expiration Date':expdate}

@app.route('/item', methods = ['DELETE'])
def deletItem():
    deletedItem = request.form['toDelete']
    deletedItem =  str(deletedItem)
    for items in repository:
        if items['SKU'] == deletedItem:
            del items

    return render_template('controller.html', myList = repository )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)