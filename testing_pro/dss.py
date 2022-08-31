import random
import string

import razorpay
from flask import Flask, render_template, request

razor_details = {"key_id": "rzp_test_05V5GVmEduGwSk", "key_secret": "oWIdCVzHvHNOgF5Lw3gKTtAH"}

app = Flask(__name__,template_folder="/home/ashok/PycharmProjects/CodingManiac/testing_pro/templates/")

@app.route('/')
def app_():
    return render_template('home.html')

@app.route('/pay', methods=['GET','POST'])
def payments():
    if request.method == "POST":
        amount = request.form.get("amount")
        currency = request.form.get("currency")
        receipt = f"receipt_{''.join(random.choices(string.ascii_uppercase + string.digits, k=5))}"
        details = {"amount": amount, "currency": currency, "receipt": receipt}
        return pay(details)

def pay(data):
    global payment
    razor_client = razorpay.Client(auth=(razor_details['key_id'], razor_details['key_secret']))
    razorpay_ord = razor_client.order.create(data=data)
    payment = {"razor":razorpay_ord, "dat":data}
    print(payment)
    return render_template('pay.html', payment=payment)

# def resp():
    # res=responce


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)



