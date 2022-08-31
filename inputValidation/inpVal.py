from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError, constr, validator
app = Flask(__name__)


class Cred(BaseModel):
    name: str
    pasword: str

    @validator("pasword")
    def password_match(cls, v):
        if not v.isdigit():
            raise ValueError("password is not a string")
        # return v.title()

# def listToDict(lst):
#     op = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return op

@app.route("/test", methods=["POST"])
def test():
    dat = request.json
    try:
        asd = Cred(**dat)
    except Exception as e:
        asf = f"{e}".split("\n")
        asf.pop(0)
        # ssd = listToDict(asf)
        ssd = {asf[i]: asf[i + 1] for i in range(0, len(asf), 2)}
        for i, j in ssd.items():
            ssd[i] = " ".join(list(filter(lambda x: x != "value", j.strip().split())))
        return jsonify({"message": ssd, "status": "failed"})
    return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run()