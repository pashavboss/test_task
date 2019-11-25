from flask import jsonify
from flask.views import MethodView

from models import Article


class ArticleView(MethodView):

    def get(self, request):
        articles = Article.get_all()
        return jsonify({
            'data': [article.serialize() for article in articles]
        })

    def post(self, request):
        # ToDO: create article
        pass
