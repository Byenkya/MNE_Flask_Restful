from me_collector import app, db, api
from me_collector.config import Config
from me_collector.routes import Project
from me_collector.models import ProjectDetails

# register routes
api.add_resource(Project, '/project')

if __name__ == '__main__':
    with app.app_context():
        app.config.from_object(Config)
        db.create_all()

    app.run(debug=True, host='0.0.0.0')

