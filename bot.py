from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Define some example symptoms and corresponding diseases.
# In a real application, you'd have a much larger dataset.
symptoms = [
    ["fever", "cough", "fatigue"],
    ["headache", "runny nose", "sore throat"],
    ["fever", "shortness of breath", "chest pain"],
    # Add more symptom-disease pairs here
]

diseases = [
    "Common Cold",
    "Flu",
    "COVID-19",
    # Add more diseases here
]

# Convert symptoms to numerical data using one-hot encoding.
symptom_dict = {}
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
classifier = DecisionTreeClassifier()
classifier.fit(X, y)

# Define a function to predict diseases based on user input.

def predict_disease(user_input):
    user_symptoms=[]
    user_symptom = user_input.split(",")
    for i in user_symptom:
        user_symptoms.append(i.lower())        
    encoded_symptoms = [0] * len(symptom_dict)
    
    for symptom in user_symptoms:
        if symptom in symptom_dict:
            encoded_symptoms[symptom_dict[symptom]] = 1

    predicted_disease=classifier.predict([encoded_symptoms])[0]
    return predicted_disease
    
    #return predicted_disease

# Chat with the user.
print("Welcome to the Disease Prediction Chatbot!")
while True:
    user_input = input("Enter your symptoms (comma-separated) or 'exit' to quit: ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    disease = predict_disease(user_input)
    print(f"Based on your symptoms, you may have: {disease}")