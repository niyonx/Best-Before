"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restx import Resource

from .security import require_auth
from . import api_rest

from .barcode import *
from .expiry import *
import os

"""This module performs the following steps sequentially:
    1. Reads in existing account IDs (if any) from the bank database.
    2. Creates additional accounts with randomly generated IDs. Then, it adds a bit of money to each new account.
    3. Chooses two accounts at random and takes half of the money from the first and deposits it into the second.
"""

import random
from math import floor
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cockroachdb.sqlalchemy import run_transaction

Base = declarative_base()

class Products(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_brand = Column(String)
    expiry_date = Column(String)



# Create an engine to communicate with the database. The
# "cockroachdb://" prefix for the engine URL indicates that we are
# connecting to CockroachDB using the 'cockroachdb' dialect.
# For more information, see
# https://github.com/cockroachdb/sqlalchemy-cockroachdb.

engine = create_engine(
    # For cockroach demo:
    # 'cockroachdb://<username>:<password>@<hostname>:<port>/bank?sslmode=require',
    # For CockroachCloud:
    'cockroachdb://nigel:bZpGIcHVE-yJ3em_@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=/home/niyon/Workspace/ExpireNoMore/certs/cc-ca.crt&options=--cluster=frozen-rhino-524',
    # 'cockroachdb://<username>:<password>@<globalhost>:26257/<cluster_name>.bank?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>',
    echo=True                   # Log SQL queries to stdout
)

# Automatically create the "accounts" table based on the Account class.
Base.metadata.create_all(engine)


# Store the account IDs we create for later use.

seen_account_ids = set()


# The code below generates random IDs for new accounts.

def get_products():

    def method(sess):
        result = []
        for instance in sess.query(Products).all():
            result.append({
                'product_id':instance.id,
                'product_name':instance.product_name,
                'product_brand':instance.product_brand,
                'expiry_date':instance.expiry_date
            }
            )
        
        return result
    
    return run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))

def create_random_products():
    """Create N new accounts with random IDs and random account balances.
    Note that since this is a demo, we don't do any work to ensure the
    new IDs don't collide with existing IDs.
    """

    def method(sess):
        new_products = []
        billion = 1000000000
        new_id = floor(random.random()*billion)
        new_products.append(
            Products(
                id=new_id,
                product_name='Mayonaise',
                product_brand='Hellmanns',
                expiry_date='06-22-2022'
            )
        )

        new_id = floor(random.random()*billion)
        new_products.append(
            Products(
                id=new_id,
                product_name='Ketchup',
                product_brand='Made in moris',
                expiry_date='01-24-2021'
            )
        )
        
        sess.add_all(new_products)
    
    run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))

print(get_products())

# create_random_products()

# run_transaction(sessionmaker(bind=engine),
#                 lambda s: create_random_products(s))


# def get_random_account_id():
#     """ Helper function for getting random existing account IDs.
#     """
#     random_id = random.choice(tuple(seen_account_ids))
#     return random_id


# def transfer_funds_randomly(session):
#     """Transfer money randomly between accounts (during SESSION).
#     Cuts a randomly selected account's balance in half, and gives the
#     other half to some other randomly selected account.
#     """
#     source_id = get_random_account_id()
#     sink_id = get_random_account_id()

#     source = session.query(Account).filter_by(id=source_id).one()
#     amount = floor(source.balance/2)

#     # Check balance of the first account.
#     if source.balance < amount:
#         raise "Insufficient funds"

#     source.balance -= amount
#     session.query(Account).filter_by(id=sink_id).update(
#         {"balance": (Account.balance + amount)}
#     )


# Run the transfer inside a transaction.

# run_transaction(sessionmaker(bind=engine), transfer_funds_randomly)

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}


@api_rest.route('/uploadBarcode')
class UploadBarcode(Resource):
    def post(self):
        if 'file' not in request.files:
            return 'Please upload file', 400

        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400

        root_dir = os.getcwd()
        img = Image.open(file)
        
        barcode_id = read_image_barcode(img)

        product_info = get_product_info(barcode_id)

        return product_info

@api_rest.route('/uploadExpiry')
class UploadExpiry(Resource):
    def post(self):
        if 'file' not in request.files:
            return 'Please upload file', 400

        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400

        root_dir = os.getcwd()
        img = Image.open(file)
        
        expiry_date = find_expiry_date(img)

        return expiry_date

@api_rest.route('/getProducts')
class GetProducts(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self):
        products = get_products()
        return products

