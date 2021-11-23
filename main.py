from flask import Flask
from flask_restful import Resource, Api
from services.repository import get_movies

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return get_movies()


api.add_resources(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
## tyle endpointów ile plików na cs