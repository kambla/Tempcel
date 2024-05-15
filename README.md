# Tempcel app - Fahrenheit to Celsius converter tool
![github-header-image](https://github.com/kambla/Tempcel/assets/44547030/08127915-ceff-4fbc-919c-8c111b696085)

## Description
This Flask application allows you to convert temperatures from Fahrenheit to Celsius. It uses a random application identifier to avoid conflicts in distributed environments.
## Application setup
You can build app from ```Dockerfile.tempcel``` by  ```docker run -p 5000:5000 kambla2662224/tempcel:1.0``` or set it on kubernetes cluster.

Initiate minikube: Invoke the command ```minikube start``` to commence minikube's operation.
Establish a Namespace: Type the command ```kubectl create namespace {name}``` to create a dedicated namespace for your application.
Install Tempcel via Helm: Employ the command ```helm install tempcel-chart/ --generate-name``` to install Tempcel using Helm.
Port Forwarding: Execute the command ```kubectl port-forward service/tempcel-svc 5000:5000``` to establish a connection between your local machine and the Tempcel application.

Now the app is ready. For instance, to convert 100 degrees Fahrenheit, 
enter ```http://localhost:5000/fahrenheit_to_celsius/100.0``` 
You can use aby float number.
The converted Celsius temperature and random identifier will be displayed in json format.
## Locust setup for testing
To evaluate Tempcel's performance under load, follow these meticulous steps:

Install Locust via Helm: ```helm install locust-chart/ --generate-name``` to install the Locust load testing tool.

Port Forwarding: ```port-forward service/locust-svc 8089:8089``` to establish a connection to the Locust interface.

Access the Locust Interface: Navigate your web browser to 
```http://localhost:8089/``` 
to interact with the Locust load testing tool.

## TensorFlow Serving for Temperature Prediction
If you wish to incorporate machine learning-based temperature prediction into your Tempcel setup, you'll need to utilize a separate Dockerfile for TensorFlow Serving. This Dockerfile will package the trained TensorFlow model and configure the serving environment. Once the TensorFlow Serving container is running, you can access it through its respective port and utilize it for temperature predictions.

Use ```docker build -f Dockerfile.model -t model_f2c .``` to build docker image with the model.
To run a container use ```docker run -p 8501:8501 model_f2c```.
### Sending Predictions Requests
In both methods, the response from the server will contain the predicted Celsius temperatures corresponding to the provided Fahrenheit values.
#### Method a: Using JSON data
```curl -d '{"instances": [212.0, 100.0, 5.0]}'   -X POST http://localhost:8501/v1/models/model:predict```
#### Method b: Using a JSON file
```curl -X POST http://localhost:8501/v1/models/model:predict -T ./data.json```

