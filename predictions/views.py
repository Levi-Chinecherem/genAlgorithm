import os
import pandas as pd
import pickle
from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

# Load the trained model
with open(os.path.join(settings.BASE_DIR, 'best_model.pkl'), 'rb') as f:
    model = pickle.load(f)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            # Read the uploaded file
            df = pd.read_csv(file)

            # Extract features for prediction
            features = ['Attendance', 'Previous_Grade', 'Study_Hours', 'Assignment_Score', 'Extracurricular']
            X_test = df[features]

            # Predict using the trained model
            df['Predicted_Final_Grade'] = model.predict(X_test)
            df['Performance'] = ['Doing Well' if grade >= 60 else 'Needs Improvement' for grade in df['Predicted_Final_Grade']]
            performance_counts = df['Performance'].value_counts()

            # Plot the predicted final grades with KDE line
            plt.figure(figsize=(10, 6))
            sns.histplot(df['Predicted_Final_Grade'], kde=True, color='blue')
            plt.title('Distribution of Predicted Final Grades')
            plt.xlabel('Predicted Final Grade')
            plt.ylabel('Frequency')
            plt.tight_layout()
            hist_img = get_image_from_plot(plt)

            # Plot the performance categories using Plotly
            plt.figure(figsize=(8, 6))
            sns.barplot(x=performance_counts.index, y=performance_counts.values, palette='viridis')
            plt.title('Student Performance Categories')
            plt.xlabel('Performance')
            plt.ylabel('Number of Students')
            plt.tight_layout()
            bar_img = get_image_from_plot(plt)

            context = {
                'dataframe': df.to_html(classes='table-auto w-full text-left border-collapse'),
                'hist_img': hist_img,
                'bar_img': bar_img
            }
            return render(request, 'results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def get_image_from_plot(plt):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    string = base64.b64encode(buf.read())
    return 'data:image/png;base64,' + string.decode('utf-8')
