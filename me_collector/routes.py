import os
from flask_restful import Api, Resource, reqparse
from flask import request
from flask.views import MethodView
from werkzeug.utils import secure_filename
from me_collector import app, db
from .models import (
    ProjectDetails,
    PdmAssets,
    PdmBeneficiaries,
    PdmEnterprises,
    PdmGroups,
    PdmProjects,
    PdmProjectAssessments
)
import json
import psycopg2
from flask import jsonify

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
                    # Ensure the upload folder exists
                    upload_folder = app.config['UPLOAD_FOLDER']
                    if not os.path.exists(upload_folder):
                        os.makedirs(upload_folder)

                    filename = secure_filename(image.filename)
                    image_path = os.path.join(upload_folder, filename)
                    image.save(image_path)
                    filenames.append(filename)

            # update image path
            project_asset['asset_photo1'] = filenames[0] if len(filenames) > 0 else None
            project_asset['asset_photo2'] = filenames[1] if len(filenames) > 1 else None

            # Save project data to the database
            project_asset_obj = PdmAssets(**project_asset)
            db.session.add(project_asset_obj)
            db.session.commit()

            print("Project Asset:", project_asset_obj)

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
class GroupResource(Resource):

    def post(self):
        try:
            # Access the project Asset
            print(request.form)
            project_group = request.form.get('group')
            project_group = json.loads(project_group)

            # Save project data to the database
            project_group = PdmGroups(**project_group)
            db.session.add(project_group)
            db.session.commit()

            print("Project Group:", project_group)

            return {
                "message": "Group saved successfully!!"
            }

        except Exception as e:
            print("**************", e)

            return {
                "message": f"Error: {e}"
            }

    def get(self):
        try:
            # Query all groups from the database
            groups = PdmGroups.query.all()

            # Convert the list of groups to a list of dictionaries
            groups_list = []
            for group in groups:
                groups_list.append({
                    'id': group.id,
                    'name': group.name,
                    'descr': group.descr
                })

            print(groups_list)

            return groups_list

        except Exception as e:
            print("**************", e)
            return {
                "message": f"Error: {e}"
            }


class ProjectResource(Resource):

    def post(self):

        try:
            # Access the project Asset
            print(request.form)
            project = request.form.get('project')
            project = json.loads(project)

            # Save project data to the database
            project = PdmProjects(**project)
            db.session.add(project)
            db.session.commit()

            print("Project:", project)

            return {
                "message": "Pdm Project saved successfully!!"
            }
        except Exception as e:
            print("**************", e)

            return {
                "message": f"Error: {e}"
            }

class ProjectAssessmentResource(Resource):

    def post(self):
        try:
            # Access the project data (assuming it's a JSON string)
            project_assessment = request.form.get('project_assessment')
            project_assessment = json.loads(project_assessment)

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
            project_assessment['assessed_photo1'] = filenames[0]
            project_assessment['assessed_photo2'] = filenames[1]
            project_assessment['assessed_photo3'] = filenames[2]
            project_assessment['assessed_photo4'] = filenames[3]
            project_assessment['milestone_photo1'] = filenames[4]
            project_assessment['milestone_photo2'] = filenames[5]
            project_assessment['milestone_photo3'] = filenames[6]
            project_assessment['milestone_photo4'] = filenames[7]

            # Save project data to the database
            project_assessment = PdmProjectAssessments(**project_assessment)
            db.session.add(project_assessment)
            db.session.commit()

            print("Project Data:", project_assessment)

            return {
                "message": "Project Assessment Saved successfully!"
            }

        except psycopg2.Error:
            return {
                "message": "Error: Record already saved. Duplicate key violation."
            }

        except Exception as e:
            print(">>", e)
            return {
                "message": f"Error: {e}"
            }
