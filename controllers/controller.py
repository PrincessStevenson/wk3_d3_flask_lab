from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route('/orders/<index>')
def order(index):
    order_to_sendback=orders[int(index)]    
    return render_template('order.html', title='Order', order=order_to_sendback)
    
    
    
    