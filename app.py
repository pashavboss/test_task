from flask import Flask
from views import ArticleView

app = Flask(__name__)


if __name__ == '__main__':
    app.run()


app.add_url_rule(
    '/articles',
    view_func=ArticleView.as_view(),
    methods=['GET', 'POST']
)
