import ast
from flask import Flask, request, jsonify
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
app = Flask(__name__)


class MyConfig:
    max_any_str_length = 10
    validate_assignment = True
    error_msg_templates = {"type_error.integer": f" should be integer",
                           'value_error.any_str.max_length': 'should not exceeds more than 10 characters'}


@dataclass(config=MyConfig)
class Password(BaseModel):
    password: int
    name :str



def exceptHandler(exc=None):
    # res = ast.literal_eval(exc.json())
    res = eval(exc.json())
    # res_ = dict()
    # print(res)
    # for i in res:
    #     res_[i['loc'][0]] = i['msg']
    # return res_
    return f"{res[0]['loc'][0]} {res[0]['msg']}"


@app.route("/test", methods=["POST"])
def test():
    try:
        a=request.json
        Password(**a)
    except Exception as e:
        res=exceptHandler(exc=e)
        return jsonify({"message": res, "status": "failed"})
    return jsonify({"status":"success"})

if __name__=="__main__":
    app.run()

