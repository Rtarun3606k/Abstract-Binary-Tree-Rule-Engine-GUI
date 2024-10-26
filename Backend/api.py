# api.py

from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule, ast_to_string, deserialize_ast
from ast_node import Node
from flask_sqlalchemy import SQLAlchemy
import ast
from config import app,db
from model import Rule



    
def serialize_ast(ast_node):
    """Convert an AST node to a serializable format."""
    if isinstance(ast_node, ast.Expression):
        return {"type": "Expression", "body": serialize_ast(ast_node.body)}
    elif isinstance(ast_node, ast.BoolOp):
        return {
            "type": "BoolOp",
            "op": type(ast_node.op).__name__,
            "values": [serialize_ast(value) for value in ast_node.values]
        }
    elif isinstance(ast_node, ast.And):
        return {"type": "And"}
    elif isinstance(ast_node, ast.Or):
        return {"type": "Or"}
    elif isinstance(ast_node, ast.Compare):
        return {
            "type": "Compare",
            "left": serialize_ast(ast_node.left),
            "comparators": [serialize_ast(comp) for comp in ast_node.comparators],
            "ops": [type(op).__name__ for op in ast_node.ops]
        }
    elif isinstance(ast_node, ast.Name):
        return {"type": "Name", "id": ast_node.id}
    elif isinstance(ast_node, ast.Constant):
        return {"type": "Constant", "value": ast_node.value}
    elif isinstance(ast_node, ast.BinOp):
        return {
            "type": "BinOp",
            "left": serialize_ast(ast_node.left),
            "right": serialize_ast(ast_node.right),
            "op": type(ast_node.op).__name__
        }
    else:
        return {"type": "Unknown", "node": str(ast_node)}


# Add the deserialize_ast function here

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule_string')
    rule_name = request.json.get('rule_name', 'Unnamed Rule')
    
    try:
        rule_ast = create_rule(rule_string)
        serialized_ast = serialize_ast(rule_ast)
        # serialized_ast  = ast.dump(rule_ast,indent=4)
        print(serialized_ast)

        new_rule = Rule(rule_name=rule_name, rule_ast=str(serialized_ast))
        db.session.add(new_rule)
        db.session.commit()

        return jsonify({"ast": serialized_ast, "message": "Rule saved successfully!"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400





@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json.get('data')
    rule_string = request.json.get('rule_string')

    try:
        # Convert the rule string to an AST node
        rule_ast = ast.parse(rule_string, mode='eval').body  # Parse the rule string

        # Evaluate the rule using the converted AST node
        result = evaluate_rule(rule_ast, data)
        return jsonify({"result": result,"message":"evaluated sucessfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except SyntaxError as e:
        return jsonify({"error": "Invalid rule AST syntax.", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while evaluating the rule", "details": str(e)}), 500




@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.json
    rules = data.get('rules')
    rule_name = data.get('rule_name')

    if not isinstance(rules, list) or not all(isinstance(rule, str) for rule in rules):
        return jsonify({"error": "Invalid input: 'rules' should be a list of strings."}), 400
    
    if not isinstance(rule_name, str) or not rule_name.strip():
        return jsonify({"error": "Invalid input: 'rule_name' must be a non-empty string."}), 400

    try:
        combined_ast = combine_rules(rules)
        combined_ast_str = ast_to_string(combined_ast)

        new_rule = Rule(rule_name=rule_name, rule_ast=combined_ast_str)
        db.session.add(new_rule)
        db.session.commit()

        return jsonify({"combined_ast": combined_ast_str, "message": "Combined rule saved successfully!"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while saving the rule", "details": str(e)}), 500
















if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


