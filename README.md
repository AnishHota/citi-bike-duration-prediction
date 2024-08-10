# CITI BIKE DURATION PREDICTION
This project aims to predict the duration of the citi bike trips in New York City. The dataset used for this project is the Citi Bike trip history data from January 2024 to March 2024. The project involves data cleaning, exploratory data analysis, feature engineering, model building, and evaluation. The goal is to build a predictive model that can accurately estimate the duration of a bike trip based on various features such as start time, end time, start station, end station. The project uses machine learning algorithms such as linear regression, decision trees, random forests, and gradient boosting to build the predictive model. The performance of the model is evaluated using root mean squared error. The project will also includes a user-friendly interface that will allow users to input the features of a bike trip and get a predicted duration.

**Data Source:** The data used for this project is the Citi Bike trip history data from January 2024 to March 2024, which can be downloaded from the following link: https://s3.amazonaws.com/tripdata/index.html. The data is in ZIP format and can be extracted to get the CSV files. It contains information about each bike trip such as start time, end time, start station, end station, user type, and gender. The data is publicly available and can be used for research and analysis purposes.
For the purpose of this project, the data is downloaded and is available in the training folder inside the data folder.

## Training Pipeline:
The training pipeline is fully orchestrated through a mage pipeline and containerized using docker. Models are tracked and regiested using MLflow. The pipeline is as follows:

To start the training pipeline:
1. Clone the github repository.
2. Navigate to the project directory.
3. Start Docker desktop.
4. Run the command: docker compose up
5. Once the containers are up and running, navigate to http://localhost:6789/ to view the mage training pipeline.
6. Click on the "Run Pipeline" button to start the training pipeline.
