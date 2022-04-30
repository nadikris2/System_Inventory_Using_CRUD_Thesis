from sqlalchemy.sql.expression import true
from . import db
from flask_login import UserMixin,current_user
from functools import wraps
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import event
from werkzeug.security import generate_password_hash

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    barang = db.Column(db.string, nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    stocks = db.Column(db.Integer, nullable=False)
    tnglbarangmasuk = db.Column(db.DateTime, nullable=False)
    tnglbarangkeluar= db.Column(db.DateTime, nullable= False)
    jmlhbarangkeluar= db.Column(db.DateTime, nullable= False)
    jmlhbarangmasuk = db.Column(db.DateTime, nullable= False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    create_on = db.Column(db.DateTime, nullable= False)

class TransactionProducts(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    transaction_id = db.Column(db.Integer, db.ForeignKey("transaction.id"), nullalble =False)
    jmlhbarangmasuk_id=db.Column(db.Integer,db.ForeignKey("products.jmlhbarangmasuk"),nullable= False)
    jmlhbarangkeluar_id=db.Column(db.Integer,db.ForeignKey("products.jmlhbarangmasuk"),nullable= False)
    product_qty = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    product = relationship("Products", backref="transaction_products")

@event.listens_for(db.session,"before_flush")
def reduce_stock_product(*args):
	sess = args[0]
	for obj in sess.new:
		if not isinstance(obj, TransactionProducts):
			continue
		product = Products.query.filter_by(id=obj.product_id).first()

		product.stocks = product.stocks + obj.jmlhbarangmasuk_id
		db.session.add(product)

@event.listens_for(db.session,"before_flush")
def reduce_stock_product(*args):
	sess = args[0]
	for obj in sess.new:
		if not isinstance(obj, TransactionProducts):
			continue
		product = Products.query.filter_by(id=obj.product_id).first()

		product.stocks = product.stocks - obj.jmlhbarangkeluar_id
		db.session.delete(product)



def __init__(self):
		self.create_on = datetime.now()