from flask import Flask
from flask_restful import Api
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from resource.user import Users

app = Flask(__name__)
api = Api(app)

app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="Awesome Projectdfdfssdd",
            version="v1",
            plugins=[MarshmallowPlugin()],
            openapi_version="2.0.0",
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",  # URI to access API Doc JSON
        "APISPEC_SWAGGER_UI_URL": "/swagger-ui/",  # URI to access UI of API Doc
        "SERVER_NAME": "fbvsig.serveirc.com:10009", # https://[每次不同].ngrok-free.app/swagger-ui/
    }
)

docs = FlaskApiSpec(app)

api.add_resource(Users, "/users")
docs.register(Users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888", debug=True, use_reloader=True)