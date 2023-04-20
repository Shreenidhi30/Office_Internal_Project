from flask import Flask

def create_app():
    app=Flask(__name__)
    from website.routes import webs



    app.register_blueprint(webs)

    
    return app


