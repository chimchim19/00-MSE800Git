"""
Develop a code, record the processing time, and share the results. Provide the GitHub link for reference. 
Hint: You may adjust the queries to align with your database structure.
"""

import sqlite3
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
    
    # Check if users already exist
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        init_users = [
            (1, 'Alice', 'alice123@email.com'),
            (2, 'Bob', 'bob123@email.com'),
            (3, 'Charlie', 'charliemail@email.com'),
            (4, 'David', 'davidtest@email.com')
        ]
        cursor.executemany("INSERT INTO users (id, name, email) VALUES (?, ?, ?)", init_users)
    
    # Check if orders already exist
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


if __name__ == "__main__":

    create_tables()

    user_service = UserService()
    order_service = OrderService()
    
    user_id = 1

    start_time = time.perf_counter()
    user = user_service.get_user(user_id)
    end_time = time.perf_counter()
    print(f"Time taken to fetch user: {end_time - start_time:.6f} seconds")

    start_time = time.perf_counter()
    orders = order_service.get_orders_by_user(user_id)
    end_time = time.perf_counter()
    print(f"Time taken to fetch orders: {end_time - start_time:.6f} seconds")
    
    #print(f"User: {user}")
    #print(f"Orders: {orders}")