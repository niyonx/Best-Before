
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
    """The Products class corresponds to the "products" database table.
    """
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    product_name = Column(String)
    product_brand = Column(String)
    expiry_date = Column(String)

class UserAccounts(Base):
    """The User class corresponds to the "user" database table.
    """
    __tablename__ = 'user_accounts'
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    phone = Column(String)

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

def create_init_users():
  
    def method(sess):
        new_users = []
        
        new_users.append(
            UserAccounts(
                user_id = 11,
                username = 'niyonx',
                password = 'password',
                phone = '4382233900'
            )
        )

        new_users.append(
            UserAccounts(
                user_id = 18,
                username = 'cnmk',
                password = 'password',
                phone = '5145690119'
            )
        )
        
        sess.add_all(new_users)
    
    return run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))

def create_init_products():
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
                user_id=11,
                product_id=new_id,
                product_name='Mayonaise',
                product_brand='Hellmanns',
                expiry_date='06-22-2022'
            )
        )

        new_id = floor(random.random()*billion)
        new_products.append(
            Products(
                user_id=11,
                product_id=new_id,
                product_name='Ketchup',
                product_brand='Made in moris',
                expiry_date='01-24-2021'
            )
        )

        new_id = floor(random.random()*billion)
        new_products.append(
            Products(
                user_id=18,
                product_id=new_id,
                product_name='Mayonaise',
                product_brand='Hellmanns',
                expiry_date='06-22-2022'
            )
        )

        new_id = floor(random.random()*billion)
        new_products.append(
            Products(
                user_id=18,
                product_id=new_id,
                product_name='Ketchup',
                product_brand='Made in moris',
                expiry_date='01-24-2021'
            )
        )
        
        sess.add_all(new_products)
    
    run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))

def get_products():
  
    def method(sess):
        result = []
        for instance in sess.query(Products).all():
            result.append({
                'product_id':instance.product_id,
                'product_name':instance.product_name,
                'product_brand':instance.product_brand,
                'expiry_date':instance.expiry_date
            }
          )
        
        return result
    
    return run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))

def create_product(product_name, product_brand, expiry_date, user_id):

    def method(sess):
        new_products = []
        billion = 1000000000
        new_id = floor(random.random()*billion)
        new_products.append(
            Products(
                user_id=user_id,
                product_id=new_id,
                product_name=product_name,
                product_brand=product_brand,
                expiry_date=expiry_date
            )
        )
        
        sess.add_all(new_products)
    
    run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))

def create_user(username, password, phone):
  
    def method(sess):
        new_user = []
        
        billion = 1000000000
        new_id = floor(random.random()*billion)
        new_user.append(
            UserAccounts(
                user_id = new_id,
                username = username,
                password = password,
                phone = phone
            )
        )
        
        sess.add_all(new_user)
    
    run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))

def check_user(username, password):

  def method(sess):
        user = sess.query(UserAccounts).filter_by(username=username).first()

        if(user and user.password == password):
            return True
        return False
    
  return run_transaction(sessionmaker(bind=engine),lambda s: method(s))

# print(get_products())

# create_init_products()

# create_init_users()

print(check_user('niyonx', 'password'))

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