from flask import Flask, Blueprint
from flask import request

from testing_.tok import access_token_required, encrypt_

app = Flask(__name__)


@app.route('/testing', methods=['POST'])
@access_token_required
@encrypt_
def decry(user_id, site_id, client_id, user_role_id, isSuperUser, isSystemAdmin, enc):
    f=user_id
    s=site_id
    print(f,s)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=False)