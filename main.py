from flask import Flask, jsonify

app = Flask(__name__)

# Модели
class Entity1:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Entity2:
    def __init__(self, id, description):
        self.id = id
        self.description = description

# Контроллеры
@app.route('/entity1/<int:id>')
def get_entity1(id):
    entity1 = Entity1(id=id, name=f"Entity1_{id}")
    return jsonify({"id": entity1.id, "name": entity1.name})

@app.route('/entity2/<int:id>')
def get_entity2(id):
    entity2 = Entity2(id=id, description=f"Description for Entity2_{id}")
    return jsonify({"id": entity2.id, "description": entity2.description})

@app.route('/health')
def health_check():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(debug=True)
