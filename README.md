# Boston House Pricing Prediction
This is a full-stack Machine Learning web application that predicts housing prices in Boston based on various socio-economic and geographic features. The project covers the entire pipeline—from data analysis and model training to deploying a web interface using Flask.

## 🚀 Project Features
Regression Modeling: Implements regression algorithms to predict continuous housing values.

Web Interface: A user-friendly web app built with Flask to allow users to input data and receive real-time predictions.

Deployment Ready: Includes configuration files (Procfile, requirements.txt) for deployment on platforms like Heroku or AWS.

Production Standards: Uses a modular Python structure and virtual environments for clean dependency management.

## 🛠️ Tech Stack
Machine Learning: Python, Scikit-learn, Pandas, NumPy

Web Framework: Flask

Environment: Conda / Python 3.7

IDE: VS Code

## 📂 Repository Structure
app.py: The Flask application script that handles routing and model inference.

requirements.txt: List of all Python libraries required to run the project.

.gitignore: Ensures environment files and temporary logs are not tracked.

LICENSE: Apache-2.0 License.

## ⚙️ Setup and Installation
1. Environment Setup
It is recommended to use a virtual environment to avoid dependency conflicts:

Bash
conda create -p venv python==3.7 -y
conda activate venv/
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Run the Application
Bash
python app.py
After running, open your browser and navigate to http://127.0.0.1:5000/.

## 📊 Methodology
Data Analysis: Explored the Boston Housing dataset to understand feature correlations.

Model Training: Trained a regression model (e.g., Linear Regression or Random Forest) to minimize prediction error.

Serialization: Saved the trained model (typically as a .pkl file) for use in the web app.

Integration: Connected the model to a Flask backend to serve predictions via a frontend UI.

👤 Author
Ayushi Jain GitHub Profile | LinkedIn
