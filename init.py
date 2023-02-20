from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    # Obtener la pregunta del usuario desde la solicitud POST
    user_input = request.json['input']
    
    # Realizar una respuesta según el input del usuario
    chatbot_response = "Esta es una respuesta del chatbot"
    
    # Devolver la respuesta del chatbot como un JSON
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
