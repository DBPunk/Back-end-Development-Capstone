from flask import Flask, request, jsonify
app = Flask(__name__)
cartoons = []
id_counter = 1
@app.route('/cartoons', methods=['GET'])
def get_cartoons():
    return jsonify(cartoons)
@app.route('/cartoons', methods=['POST'])
def post_cartoons():
    global id_counter
    data = request.get_json()
    new_c = {'id': id_counter, 'title': data['title']}
    cartoons.append(new_c)
    id_counter += 1
    return jsonify(new_c), 201
@app.route('/cartoons/<int:id>', methods=['DELETE'])
def delete_cartoon(id):
    global cartoons
    cartoons = [c for c in cartoons if c['id'] != id]
    return jsonify({'message':'Deleted'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
