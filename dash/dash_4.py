import json
from itertools import islice

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template("temp.html")


@app.route("/test", methods=['GET', 'POST'])
def tes():
    # df = request
    f = request.files.get('file')
    data = f.read().decode().split("END")
    splitData = [i.replace("\r\n", "") for i in data if "\r" or "\n" in i]
    finalOut, loadVal, eventData, instantData, scalar = dict(), dict(), dict(), dict(), dict()
    tuple(map(lambda x: finalOut.update({x.split(",")[0].lower(): x.split(",")[1:-1] if splitData.index(x) != len(
        splitData) - 1 else x.split(",")[1:]}), splitData))

    def splitter(arr, size):
        arr = iter(arr)
        return iter(lambda: tuple(islice(arr, size)), ())

    for key in finalOut.copy().keys():
        notMap = ["RS485-Device_Address value".lower(), 'billing data value', 'instant data value',
                  'block load data value', 'daily load data value', 'billing load data value']

        if "value" in key and "event" not in key and key not in notMap and "scalar" not in key:
            OBIS = finalOut[key.replace("value", "obis")]
            keyVal = finalOut[key]
            finalOut[key] = dict(zip(OBIS, keyVal))
            del finalOut[key.replace("value", "obis")]

        elif "event" in key and "obis" not in key and "scalar" not in key:
            data_ = list(splitter(finalOut[key], len(finalOut[key.replace("value", "obis")])))
            eventData[key] = list(map(lambda x: {"obis": finalOut[key.replace("value", "obis")], "val": x}, data_))
            del finalOut[key.replace("value", "obis")], finalOut[key]

        elif key in ['billing data value', 'daily load data value', 'block load data value']:
            load = list(splitter(finalOut[key], len(finalOut[key.replace("value", "obis")])))
            loadVal[key] = list(map(lambda x: {"obis": finalOut[key.replace("value", "obis")], "val": x}, load))
            del finalOut[key.replace("value", "obis")], finalOut[key]

        elif key in ['instant data value']:
            load = list(splitter(finalOut[key], len(finalOut[key.replace("value", "obis")])))
            instantData[key] = {"obis": finalOut[key.replace("value", "obis")], "val": finalOut[key]}
            del finalOut[key.replace("value", "obis")], finalOut[key]

        elif "scalar" in key and "obis" in key:
            OBIS = finalOut[key]
            keyVal = finalOut[key.replace("obis", "value")]
            scalar[key] = dict(zip(OBIS, keyVal))
            del finalOut[key.replace("obis", "value")], finalOut[key]

    mainDict = {"GENERAL": finalOut, "EVENT": eventData, "LOAD": loadVal, "INSTANT": instantData, "SCALAR": scalar}
    del eventData, loadVal, finalOut, instantData, scalar
    TEMP = json.dumps(mainDict)
    print(TEMP)
    return TEMP


if __name__ == "__main__":
    app.run(debug=True)