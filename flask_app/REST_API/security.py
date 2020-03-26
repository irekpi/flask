from user import User

# mimic of DB
users = [
    User(1, 'Jos', 'mypassword'),
    User(2, 'Kat', 'mypassword')
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and password == user.password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)