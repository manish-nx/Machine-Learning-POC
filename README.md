# Machine-Learning-POC

## Requirements

Python 3.6
```
sudo apt-get install python3.6
```
PIP3
```
sudo apt-get install python3-pip

```

## Installation
This will install all the required packages
```
pip3 install -r requirements.txt
```

## Usage

Train & Prepare Model
```
python3 model.py
```
Run Local Server
```
python3 server.py
```
Prediction - API Call
```
URL: http://localhost:5000/predict
Headers: { Content-Type: application/json }
Body: { "celsius": <value> }
```