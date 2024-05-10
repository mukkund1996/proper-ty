columns = [
     "id INTEGER PRIMARY KEY",
     "last_name VARCHAR",
     "first_name VARCHAR",
     "username VARCHAR UNIQUE"
    ]

users = [
     "1, 'Admin', 'User', 'admin'",
     "2, 'Basic', 'User', 'basic'",
 ]
for user in users:
    insert_cmd = f"INSERT INTO user VALUES ({user})"
    conn.execute(insert_cmd)