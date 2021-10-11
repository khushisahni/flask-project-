from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        "data": [
            {
                "Contact": "9987644456",
                "Name": "Raju",
                "done": false,
                "id": 1
            },
            {
                "Contact": "9876543222",
                "Name": "Rahul",
                "done": false,
                "id": 2
            }


        ]

   }
]

@app.route("/add-data", methods=["POST"])

def add_task() :
    
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)