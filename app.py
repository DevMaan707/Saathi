from flask import Flask, request,render_template,jsonify
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from flask_socketio import SocketIO, send, emit
classifier = DecisionTreeClassifier()
app=Flask(__name__)
socketio = SocketIO(app)
symptom_dict={}
user_input=""
predicted_disease=""
@app.route("/")
def start():
    return render_template("index.html")

@socketio.on('data_from_client')
def handle_data(data):
    # Process the data
    user_input = data['data']
    print(user_input)   
    solution=work()        
    json_data = {'message': solution}
    socketio.emit('json_response', json_data)

@app.route("/bott.html")
def chat():
               
    return render_template("bott.html")


def work():
    symptoms = [
        ["fever", "cough", "fatigue"],
        ["headache", "runny nose", "sore throat","fever"],
        
        # Add more symptom-disease pairs here
    ]

    diseases = [
        "Common Cold",
        "Flu",
        
        # Add more diseases here
    ]
    print("I am here__")

    # Convert symptoms to numerical data using one-hot encoding.
    
    for i, symptom in enumerate(symptoms):
        for s in symptom:
            if s not in symptom_dict:
                symptom_dict[s] = len(symptom_dict)

    X = []
    for symptom_set in symptoms:
        encoded_symptoms = [0] * len(symptom_dict)
        for symptom in symptom_set:
            encoded_symptoms[symptom_dict[symptom]] = 1
        X.append(encoded_symptoms)

    X = np.array(X)
    y = np.array(diseases)

    # Create a decision tree classifier and train it.
    
    classifier.fit(X, y)
    sol=predict_disease()
    return sol
    # Define a function to predict diseases based on user input.
def predict_disease():
        print("Pred_disease")
        user_symptoms=[]
        user_symptom = user_input.split(",")
        for i in user_symptom:
            user_symptoms.append(i.lower())        
        encoded_symptoms = [0] * len(symptom_dict)
        
        for symptom in user_symptoms:
            if symptom in symptom_dict:
                encoded_symptoms[symptom_dict[symptom]] = 1

        predicted_disease = classifier.predict([encoded_symptoms])[0]
        print(predicted_disease)
        return predicted_disease    

    # Define some example symptoms and corresponding diseases.
    # In a real application, you'd have a much larger dataset.
    

if __name__=="__main__":
    socketio.run(app, debug=True)
    