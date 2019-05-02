from flask import Flask, request, Response
from flask_api import status
import sqlite3
from sqlite3 import Error
import json
from flask_cors import CORS
from task import Task

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db_file = "database.db"


def connect_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


@app.route('/list', methods=['GET'])
def itemList():
    with connect_db(db_file) as conn:
        results = Task(conn).list()
        return Response(
                response=json.dumps(results), 
                status=status.HTTP_200_OK,
                mimetype='application/json')


@app.route('/add', methods=['POST'])
def addItem():
    try:    
        task_name = json.loads(request.data)["task"] 
    except:
        return internal_error("empty POST")   
    with connect_db(db_file) as conn:
        Task(conn).add(task_name)
        return Response( 
                status=status.HTTP_201_CREATED,
                mimetype='application/json')


@app.route('/delete', methods=['DELETE'])
def deleteItem():
    id = request.args.get('id')
    with connect_db(db_file) as conn:
        Task(conn).delete(id)
        return Response( 
                status=status.HTTP_200_OK,
                mimetype='application/json')


@app.route('/complete', methods=['PUT'])
def completeItem():
    id = request.args.get('id')
    with connect_db(db_file) as conn:
        Task(conn).complete(id)
        return Response( 
                status=status.HTTP_200_OK,
                mimetype='application/json')
 

@app.errorhandler(404)
def not_found_error(error):
    return Response( 
        status=status.HTTP_404_NOT_FOUND,
        mimetype='application/json')    


@app.errorhandler(500)
def internal_error(error):
    return Response(
        response=error, 
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        mimetype='application/json')    


if __name__ == '__main__':
    app.run()