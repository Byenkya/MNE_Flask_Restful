from me_collector import app, db, api
from me_collector.config import Config
from me_collector.routes import Project, AssetResource, BeneficiaryResource, EnterpriseResource, GroupResource
from me_collector.models import ProjectDetails

# register routes
api.add_resource(Project, '/project')
api.add_resource(AssetResource, '/saveAsset')
api.add_resource(BeneficiaryResource, '/saveBeneficiary')
api.add_resource(EnterpriseResource, '/saveEnterprise')
api.add_resource(GroupResource, '/saveGroup')


if __name__ == '__main__':
    with app.app_context():
        app.config.from_object(Config)
        db.create_all()

    app.run(debug=True, host='0.0.0.0')

