import os
import pandas as pd
# from flask import Flask, render_template, request, redirect, url_for, send_file
from flask import Flask, render_template, request, redirect, url_for, flash, send_file

def catFunction(p):
    return True

def cat1Page():
    if request.method == 'POST':
        # Process uploaded files for Category 1
        file1 = request.files['file1']
        file2 = request.files['file2']

        if file1 and file2:
            # Save the uploaded files
            file1.save(os.path.join('uploads', 'cat1_file1.xlsx'))
            file2.save(os.path.join('uploads', 'cat1_file2.xlsx'))

            # Process and merge the files using pandas (example: concatenating dataframes)
            df1 = pd.read_excel(os.path.join('uploads', 'cat1_file1.xlsx'))
            df2 = pd.read_excel(os.path.join('uploads', 'cat1_file2.xlsx'))
            result_df = pd.concat([df1, df2], ignore_index=True)

            # Save the processed dataframe to a new Excel file
            result_df.to_excel(os.path.join('uploads', 'cat1_result.xlsx'), index=False)

            flash('Files uploaded and processed successfully!', 'success')
            return redirect(url_for('home'))

    return render_template('cat1.html')