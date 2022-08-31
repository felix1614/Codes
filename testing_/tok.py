from functools import wraps
from flask import request, jsonify
from flask import Flask
import jwt

app = Flask(__name__)

app.config['SECRET_KEY'] = '8fNGJMqrQwIMV3AdlYEiQbSAa_VETe2JlOMbtPE7Zs'


def access_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if 'Access_Token' in request.headers:
                token = request.headers['Access_Token']
            else:
                raise Exception
        except Exception as e:
            return jsonify({'message': f'{e}-Access-Token is missing!'}), 401

        try:
            # data = jwt.decode(token, app.config['SECRET_KEY'])/
            client_id = "as"
            user_id = "as"
            isSystemAdmin = "we"
            user_role_id = "rt"
            site_id = "rt"
            isSuperUser = "rt"

            return f(user_id, site_id, client_id, user_role_id, isSuperUser, isSystemAdmin, *args, **kwargs)

        except (jwt.InvalidSignatureError, jwt.ExpiredSignatureError, jwt.InvalidTokenError) as error:
            return jsonify({'message': f'{error}.'}), 401

    return decorated


def encrypt_(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        client_id = "as"
        user_id = "as"
        isSystemAdmin = "we"
        user_role_id = "rt"
        site_id = "rt"
        isSuperUser = "rt"
        enc= "enc "
        print(*args, **kwargs)
        return f(user_id, site_id, client_id, user_role_id, isSuperUser, isSystemAdmin, enc)

    return decorated

