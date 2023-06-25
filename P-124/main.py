from flask import Flak,jonify, requet

app = Flak(__name__)

data = [
    {
        'Contact': '9987644456',
        'Name': 'Raju',
        'done': False, 
        'id': 1
    },
    {
        'Contact': '9876543222',
        'Name': 'Rahul',
        'done': False, 
        'id': 2
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", method=["POT"])
def add_data():
    if not requet.jon:
        return jonify({
            "tatu":"error",
            "meage": "Pleae provide the data!"
        },400)

    data = {
        'id': data[-1]['id'] + 1,
        'title': requet.jon['title'],
        'decription': requet.jon.get('decription', ""),
        'done': False
    }
    data.append(data)
    return jonify({
        "tatu":"ucce",
        "meage": "data added uccefully!"
    })
    

@app.route("/get-data")
def get_data():
    return jonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)