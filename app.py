from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_uuid import FlaskUUID
from uuid import uuid4
import os
from datetime import datetime

app = Flask(__name__)
FlaskUUID(app)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

db = SQLAlchemy(app)

# Define the Image model
class Image(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    image_name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Create the database and tables
with app.app_context():
    db.create_all()

# GET API - Paginated list of images
@app.route('/images', methods=['GET'])
def get_images():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    images = Image.query.paginate(page=page, per_page=per_page)
    
    data = []
    for image in images.items:
        data.append({
            'id': image.id,
            'image_name': image.image_name,
            'image_url': url_for('static', filename=image.image_url, _external=True),
            'created_on': image.created_on
        })
    
    return jsonify({
        'total': images.total,
        'pages': images.pages,
        'current_page': images.page,
        'images': data
    })

# POST API - Upload an image
@app.route('/upload', methods=['POST'])
def upload_image():
    image_name = request.form['image_name']
    image_file = request.files['image_file']

    if image_file:
        image_filename = str(uuid4()) + '_' + image_file.filename
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        image_file.save(image_path)

        image = Image(
            image_name=image_name,
            image_url=os.path.join('uploads', image_filename)  # Update the URL path
        )
        db.session.add(image)
        db.session.commit()

        return jsonify({'message': 'Image uploaded successfully', 'image_id': image.id}), 201

    return jsonify({'message': 'Image upload failed'}), 400

# Index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
