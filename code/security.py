from user import User

##users = [
##   User(1,'bob','asdf')
##]

##username_mapping = {u.username: u for u in users}
##userid_mapping = {u.id: u for u in users}


def authenticate(username,password):
    user = User.find_by_username(username)
    if user is not None and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)