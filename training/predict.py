import pickle
import time
from flask import Flask
from flask import request
from flask import jsonify
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("citi-bike")

app = Flask('duration-prediction')

def model_exists(model_name):
    client = MlflowClient()
    try:
        latest_version = client.get_latest_versions(model_name)
        return bool(latest_version)
    except mlflow.exceptions.RestException:
        return False

def wait_for_model():
    model_name = "citi-bike"  # Replace with your model name
    while not model_exists(model_name):
        print(f"Waiting for model {model_name} to be registered in MLflow...")
        time.sleep(30)
    print(f"Model {model_name} found, ready to serve requests.")
    return True

def load_model():
    client = MlflowClient(tracking_uri="http://mlflow:5000")

    # logged_model = 'runs:/09ea924d01d943d090abc307b04dcb0e/model'
    model_name = "citi-bike-model"
    # Use model version
    latest_version_info = max(client.get_latest_versions(model_name), key=lambda x: int(x.version))
    print(latest_version_info)
    latest_version = latest_version_info.version
    run_id = latest_version_info.run_id
    print(latest_version, run_id)

    # Load model as a PyFuncModel.
    model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{latest_version}")
    print(f'The model is loaded')
    # model = mlflow.pyfunc.load_model(registered_model)

    dv_path = client.download_artifacts(run_id=run_id, path="preprocessor/preprocessor.b")

    print(f"Downloading the dict vectorizer to {dv_path}")

    with open(dv_path,'rb') as f_in:
        dv = pickle.load(f_in)
    
    return model, dv


def prepare_features(ride):
    features = {
        'start_end_id': '%s_%s' % (ride["start_station_id"], ride["end_station_id"]),
    }
    return features

def predict(features):
    model, dv = load_model()
    X = dv.transform([features])
    preds = model.predict(X)
    return float(preds[0])



@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()
    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred
    }

    return jsonify(result)

if __name__=="__main__":
    while not wait_for_model():
        time.sleep(30)
    app.run(debug=True, host='0.0.0.0', port=9696)