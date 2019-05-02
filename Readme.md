This is the simple ToDo list app.
![App](https://github.com/juldepol/todo-flask/blob/master/sreenshots/app.png)
Run frontend
------------
### Set up
    cd frontend 
    npm install
### Run
    npm start
    Visit http://localhost:3000/
## Tests
    npm test

Run backend
-----------
## Flask
### Set up
    cd server
    pip install virtualenv
    virtualenv venv
    venv\scripts\activate (on Windows)
    venv/bin/activate (on Linux)
    pip install --user --requirement requirements.txt
### Run
    python server.py
#### Tests              
    python tests.py