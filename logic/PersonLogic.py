from flask import jsonify
from dataacces.PersonDA import PersonDA


class PersonLogic:

    @staticmethod
    def createPerson(body):
        try:
            if body["name"] is None or body["name"] == "":
                return jsonify({"error": "Name is empty."}), 400
            
            if body["lastname"] is None or body["lastname"] == "":
                return jsonify({"error": "lastname is empty."}), 400
            
            if body["age"] is None or body["age"] < 0:
                return jsonify({"error": "age is empty."}), 400

            return PersonDA.createPerson(body)
        except Exception as e:
            print("Error: ", e)
            return jsonify({"message": "Error an encountered."}), 500

    @staticmethod
    def listPerson():
        try:
            return PersonDA.listPerson()
        except Exception as e:
            print("Error: ", e)
            return jsonify({"message": "Error list person logic."}), 500

    @staticmethod
    def getPersonById(person_id):
        try:
            return PersonDA.getPersonById(person_id)
        except Exception as e:
            print("Error: ", e)
            return jsonify({"message": "Error detail person logic."}), 500
    

    @staticmethod
    def updatePersonById(person_id, body):
        try:
            if body["name"] is None or body["name"] == "":
                return jsonify({"error": "Name is empty."}), 400
            
            if body["lastname"] is None or body["lastname"] == "":
                return jsonify({"error": "lastname is empty."}), 400
            
            if body["age"] is None or body["age"] < 0:
                return jsonify({"error": "age is empty."}), 400

            return PersonDA.updatePersonById(person_id, body)
        except Exception as e:
            print("Error: ", e)
            return jsonify({"message": "Error update persona logic."}), 500