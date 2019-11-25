from flask import Flask
from views import ArticleView

app = Flask(__name__)

app.add_url_rule(
    '/articles',
    view_func=ArticleView.as_view('article-view'),
    methods=['GET', 'POST']
)

if __name__ == '__main__':
    app.run()
