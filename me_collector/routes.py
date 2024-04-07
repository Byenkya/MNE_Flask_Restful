import os
from flask_restful import Api, Resource, reqparse
from flask import request
from flask.views import MethodView
from werkzeug.utils import secure_filename
from me_collector import app, db
from .models import ProjectDetails, PdmAssets, PdmBeneficiaries, PdmEnterprises
import json
import psycopg2

parser = reqparse.RequestParser()
parser.add_argument('images', type=list, location='files', action='append')


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


class Project(Resource):

    def post(self):
        try:
            # Access the project data (assuming it's a JSON string)
            project_data = request.form.get('project')
            project_data = json.loads(project_data)

            # Process the images
            images = request.files.getlist('images')
            # store file names only
            filenames = []

            for image in images:
                if image and allowed_file(image.filename):
                    filename = secure_filename(image.filename)
                    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    filenames.append(filename)

            # Update project data with image filenames
            project_data['memberPhotoPath'] = filenames[0]
            project_data['photoOnePath'] = filenames[1]
            project_data['photoTwoPath'] = filenames[2]
            project_data['photoThreePath'] = filenames[3]
            project_data['photoFourPath'] = filenames[4]
            project_data['milestonePhotoOnePath'] = filenames[5]
            project_data['milestonePhotoTwoPath'] = filenames[6]
            project_data['milestonePhotoThreePath'] = filenames[7]
            project_data['milestonePhotoFourPath'] = filenames[8]

            # Save project data to the database
            project_details = ProjectDetails(**project_data)
            db.session.add(project_details)
            db.session.commit()

            print("Project Data:", project_data)

            return {
                "message": "Project Assessment Saved successfully!"
            }

        except psycopg2.Error:
            return {
                "message": "Error: Record already saved. Duplicate key violation."
            }

        except Exception as e:
            return {
                "message": f"Error: {e}"
            }


class AssetResource(Resource):

    def post(self):
        try:

            # Access the project Asset
            project_asset = request.form.get('asset')
            project_asset = json.loads(project_asset)

            # Process the images
            images = request.files.getlist('images')
            # store file names only
            filenames = []
            for image in images:
                if image and allowed_file(image.filename):
                    filename = secure_filename(image.filename)
                    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    filenames.append(filename)

            # update image path
            project_asset['asset_photo1'] = filenames[0]
            project_asset['asset_photo2'] = filenames[1]

            # Save project data to the database
            project_asset = PdmAssets(**project_asset)
            db.session.add(project_asset)
            db.session.commit()

            print("Project Asset:", project_asset)

            return {
                "message": "Asset saved successfully!!"
            }

        except Exception as e:
            print(">>>>>>>>>>>>>", e)

            return {
                "message": f"Error: {e}"
            }


class BeneficiaryResource(Resource):

    def post(self):
        try:
            # Access the project Asset
            project_beneficiary = request.form.get('beneficiary')
            project_beneficiary = json.loads(project_beneficiary)

            # Save project data to the database
            project_beneficiary = PdmBeneficiaries(**project_beneficiary)
            db.session.add(project_beneficiary)
            db.session.commit()

            print("Project Beneficiary:", project_beneficiary)

            return {
                "message": "Beneficiary saved successfully!!"
            }

        except Exception as e:
            print("**************", e)

            return {
                "message": f"Error: {e}"
            }

class EnterpriseResource(Resource):

    def post(self):
        try:
            # Access the project Asset
            print(request.form)
            project_enterprise = request.form.get('enterprise')
            project_enterprise = json.loads(project_enterprise)

            # Save project data to the database
            project_enterprise = PdmEnterprises(**project_enterprise)
            db.session.add(project_enterprise)
            db.session.commit()

            print("Project Enterprise:", project_enterprise)

            return {
                "message": "Enterprise saved successfully!!"
            }

        except Exception as e:
            print("**************", e)

            return {
                "message": f"Error: {e}"
            }
