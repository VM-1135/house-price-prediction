# House Price Predictor

This is a Flask-based web application that predicts house prices based on features like location, total rooms, bedrooms, population, and number of households. It uses a trained **Linear Regression** model with **scikit-learn** and serves predictions via a simple web interface.


## Features

Input features via a web form
Real-time price prediction using a trained ML model
Scaled inputs using StandardScaler
Clean Bootstrap-based UI
Handles invalid or negative predictions gracefully

## Project Structure

House-price-predictor/

─ app.py             # Flask web app
─ train.py           # ML training script
─ housing.csv        # Dataset used for training
─ model.pkl          # Trained linear regression model
─ scaler.pkl         # Fitted StandardScaler object
─ README.md          # Documentation of the project

─ templates/
   ─ index.html      # HTML form and result display


##  Technologies Used

 Python 3.13
 Flask
 scikit-learn
 Pandas
 NumPy
 Bootstrap 5 (for UI)
 Joblib (for model serialization)

##  ML Model Info

 **Model**: Linear Regression
 **Features used**:
   Longitude
   Latitude
   Total Rooms
   Total Bedrooms
   Population
   Households
 **Preprocessing**: Feature scaling with `StandardScaler`



#  Demo Screenshots

# Input Form Page
[Input Form] -> index.png

#  Prediction Result Page
[Prediction Result] -> predicted.png

# Command Line Running the App
[Command Prompt] -> cmdprompt.png


# How to Run Locally

1. **Clone the repository**:

   bash
   git clone https://github.com/yourusername/house-price-predictor.git
   cd house-price-predictor

   Install dependencies:
pip install -r requirements.txt

or **manually** install:

**pip install flask scikit-learn pandas numpy**

Train the model:
python train.py

Run the Flask app:
python app.py

Visit in browser:
Open http://127.0.0.1:5000 in your browser.



**!!Important Note!!**

 **Input Guidelines for California Housing Price Prediction**
Please follow the below input value ranges while using the prediction form to ensure accurate results:

Feature	Description	Recommended Range
longitude:	Geographic coordinate (west-east), negative values	-124 to -114
latitude:	Geographic coordinate (south-north)	32 to 42
total_rooms:	Total number of rooms in the area	100 to 10,000+
total_bedrooms:	Total number of bedrooms in the area	50 to 4,000
population:	Total population of the block/group	200 to 60,000+
households:	Total number of households in the area	50 to 20,000

 Notes:
Ensure total_bedrooms is less than or equal to total_rooms.

Very high values beyond these ranges may lead to inaccurate or $0 predictions due to model limitations.

For best results, use values within realistic California housing data.

Please ensure that:

You enter longitude as a negative number (e.g., -122), since California lies in the Western Hemisphere.

Incorrect input (e.g., positive longitude like 122) may lead to inaccurate or zero predictions due to the model being trained on a specific geographical region.



**Acknowledgements**
Dataset: California Housing Dataset - Scikit-Learn
Built with: Python, Flask, Scikit-Learn, Bootstrap
