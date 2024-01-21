import os
from flask_restful import Api, Resource, reqparse
from flask import (
    Flask,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    jsonify
)
from flask.views import MethodView
from werkzeug.utils import secure_filename
from me_collector import app, db
from .models import ProjectDetails
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


