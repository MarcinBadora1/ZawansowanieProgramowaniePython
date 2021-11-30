from flask import Flask
from flask_restful import Resource, Api
from services.repository import get_movies

app = Flask(__name__)
api = Api(app)


# class HelloWorld(Resource):
#     def get(self):
#         return get_movies()


class ShowMovies(Resource):
    def get(self):
        return get_movies_data()


class ShowTags(Resource):
    def get(self):
        return get_tags_data()


class ShowRatings(Resource):
    def get(self):
        return get_ratings_data()


class ShowLinks(Resource):
    def get(self):
        return get_links_data()


api.add_resource(ShowMovies, '/movie')
api.add_resource(ShowTags, '/tags')
api.add_resource(ShowRatings, '/ratings')
api.add_resource(ShowLinks, '/links')
# api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
## tyle endpointów ile plików na cs