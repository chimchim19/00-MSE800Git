"""
Compare the coding outcomes and processing time when using the Singleton design pattern in OOP (Week 7 – Activity 1) 
within your coding style. Share the GitHub link and add a short comment explaining it.
"""

import sqlite3
import threading
import time

class UserService:
    def __init__(self):
        pass

    def get_user(self, user_id):
        conn = sqlite3.connect('Week7/week7_sample.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user
    
class OrderService:
    def __init__(self):
        pass

    def get_orders_by_user(self, user_id):
        conn = sqlite3.connect('Week7/week7_sample.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        orders = cursor.fetchall()
        conn.close()
        return orders

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._connection = None
        return cls._instance

    def get_connection(self):
        if self._connection is None:
            self._connection = sqlite3.connect('Week7/week7_sample.db', check_same_thread=False)
        return self._connection
    
    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None
    
class UserService2:
    def __init__(self, database):
        self.__db = database

    def get_user(self, user_id):
        conn = self.__db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        ## conn.close()
        return user
    
class OrderService2:
    def __init__(self, database):
        self.__db = database

    def get_orders_by_user(self, user_id):
        conn = self.__db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        orders = cursor.fetchall()
        return orders
    

def create_tables():
    conn = sqlite3.connect('Week7/week7_sample.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product TEXT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')

    # Check if table users has entries, insert initial data if empty
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        init_users = [
            (1, 'Alice', 'alice123@email.com'),
            (2, 'Bob', 'bob123@email.com'),
            (3, 'Charlie', 'charliemail@email.com'),
            (4, 'David', 'davidtest@email.com')
        ]

        cursor.executemany("INSERT INTO users (id, name, email) VALUES (?, ?, ?)", init_users)
    

    # Check if table orders has entries, insert initial data if empty
    cursor.execute("SELECT COUNT(*) FROM orders")
    if cursor.fetchone()[0] == 0:
        init_orders = [
            (1, 1, 'Laptop', 999.99),
            (2, 1, 'Mouse', 25.50),
            (3, 2, 'Keyboard', 45.00),
            (4, 3, 'Monitor', 150.75),
            (5, 4, 'Printer', 85.20)
        ]

        cursor.executemany("INSERT INTO orders (id, user_id, product, amount) VALUES (?, ?, ?, ?)", init_orders)
    
    conn.commit()
    conn.close()

def run():
    create_tables()  # initialize database and tables

    # instantiate for non-singleton
    user_service = UserService()
    order_service = OrderService()

    # instantiate for singleton
    db = DatabaseConnection()   # singleton global instance
    user_service2 = UserService2(db)
    order_service2 = OrderService2(db)

    user_id = 1

    print("\nWithout Singleton Pattern:\n")
    start_time = time.perf_counter()
    user = user_service.get_user(user_id)
    end_time = time.perf_counter()
    print(f"Time taken to fetch user: {end_time - start_time:.6f} seconds")

    start_time = time.perf_counter()
    orders = order_service.get_orders_by_user(user_id)
    end_time = time.perf_counter()
    print(f"Time taken to fetch orders: {end_time - start_time:.6f} seconds")
    
    print("\nUsing Singleton Pattern:\n")
    start_time = time.perf_counter()
    user = user_service2.get_user(user_id)
    end_time = time.perf_counter()
    print(f"Time taken to fetch user: {end_time - start_time:.6f} seconds")

    start_time = time.perf_counter()
    orders = order_service2.get_orders_by_user(user_id)
    end_time = time.perf_counter()
    print(f"Time taken to fetch orders: {end_time - start_time:.6f} seconds")
    
    print(f"User: {user}")
    print(f"Orders: {orders}")

    db.close_connection()

if __name__ == "__main__":
    run()
