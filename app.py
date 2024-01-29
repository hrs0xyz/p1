from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import pandas as pd
from werkzeug.utils import secure_filename
import cat1.cat1 as category1

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_type = request.form.get('type')
        uploaded_files = request.files.getlist('file')

        # Check if the type and number of files match
        if selected_type == 'type1' and len(uploaded_files) != 3:
            return "Please upload 3 files for type1."
        elif selected_type == 'type2' and len(uploaded_files) != 4:
            return "Please upload 4 files for type2."

        # Create a folder for each user to store their files
        user_folder = os.path.join(app.config['UPLOAD_FOLDER'], selected_type)
        os.makedirs(user_folder, exist_ok=True)

        # Upload files
        for file in uploaded_files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(user_folder, filename))

        # Process files (For demonstration, simply concatenate Excel files)
        output_file_path = os.path.join(user_folder, 'output.xlsx')
        dfs = [pd.read_excel(os.path.join(user_folder, file)) for file in os.listdir(user_folder)]
        result_df = pd.concat(dfs, axis=1)
        result_df.to_excel(output_file_path, index=False)

        # Provide the file for download
        return send_file(output_file_path, as_attachment=True)

    return render_template('index2.html')

@app.route('/cat1', methods=['GET', 'POST'])
def cat1():
    return category1.cat1Page()

if __name__ == '__main__':
    app.run(debug=False)
