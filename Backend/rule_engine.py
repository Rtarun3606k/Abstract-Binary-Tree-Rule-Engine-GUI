# rule_engine.py

import ast
import operator
from ast_node import Node
from functools import reduce

# Supported comparison and logical functions
operators = {
    ast.Gt: operator.gt,
    ast.Lt: operator.lt,
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.And: operator.and_,
    ast.Or: operator.or_,
}

def create_rule(rule_string):
    """Convert the rule string to a Python AST."""
    # Replace logical operators to match Python syntax
    rule_string = rule_string.replace(' AND ', ' and ').replace(' OR ', ' or ')
    
    try:
        tree = ast.parse(rule_string, mode='eval')
        return tree
    except Exception as e:
        raise ValueError(f"Invalid rule syntax: {str(e)}")
    

def deserialize_ast(ast_json):
    """Convert a JSON representation of the AST back to an AST node."""
    node_type = ast_json.get("type")
    
    if node_type == "Expression":
        return ast.Expression(body=deserialize_ast(ast_json["body"]))
    elif node_type == "Compare":
        left = deserialize_ast(ast_json["left"])
        comparators = [deserialize_ast(comp) for comp in ast_json["comparators"]]
        ops = [getattr(ast, op)() for op in ast_json["ops"]]
        return ast.Compare(left=left, ops=ops, comparators=comparators)
    elif node_type == "Name":
        return ast.Name(id=ast_json["id"], ctx=ast.Load())
    elif node_type == "Constant":
        return ast.Constant(value=ast_json["value"])
    elif node_type == "BoolOp":
        values = [deserialize_ast(value) for value in ast_json["values"]]
        op = getattr(ast, ast_json["op"])()
        return ast.BoolOp(op=op, values=values)
    # Add other AST node types as needed
    raise ValueError(f"Unsupported AST Node type: {node_type}")

def evaluate_rule(rule_ast, data):
    """Evaluate the rule AST against the provided data."""
    # The rule_ast is already an AST node; no need to deserialize
    def eval_node(node):
        if isinstance(node, ast.Expression):
            return eval_node(node.body)
        elif isinstance(node, ast.BoolOp):
            if isinstance(node.op, ast.And):
                return all(eval_node(value) for value in node.values)
            elif isinstance(node.op, ast.Or):
                return any(eval_node(value) for value in node.values)
        elif isinstance(node, ast.Compare):
            left = eval_node(node.left)
            for comp, op in zip(node.comparators, node.ops):
                right = eval_node(comp)
                if isinstance(op, ast.Gt):
                    return left > right
                elif isinstance(op, ast.Lt):
                    return left < right
                elif isinstance(op, ast.Eq):
                    return left == right
                elif isinstance(op, ast.GtE):
                    return left >= right
                elif isinstance(op, ast.LtE):
                    return left <= right
                elif isinstance(op, ast.NotEq):
                    return left != right
        elif isinstance(node, ast.Name):
            return data.get(node.id)
        elif isinstance(node, ast.Constant):
            return node.value
        else:
            raise ValueError(f"Unsupported AST Node: {type(node)}")

    return eval_node(rule_ast)




import ast

def combine_rules(rules):
    combined_expr = None
    for rule in rules:
        # Replace 'AND' with 'and' for Python compatibility
        rule = rule.replace(' AND ', ' and ')

        try:
            # Parse the rule string into an AST
            rule_ast = ast.parse(rule, mode='eval').body
            
            # Combine the expressions using logical AND
            if combined_expr is None:
                combined_expr = rule_ast
            else:
                combined_expr = ast.BoolOp(op=ast.And(), values=[combined_expr, rule_ast])
        except SyntaxError as e:
            raise ValueError(f"Invalid rule syntax: {e}")

    return combined_expr

def ast_to_string(node):
    if isinstance(node, ast.BoolOp):
        op = ' AND ' if isinstance(node.op, ast.And) else ' OR '
        return op.join(ast_to_string(v) for v in node.values)
    elif isinstance(node, ast.Compare):
        # Convert comparison node to string
        left = ast_to_string(node.left)
        right = ast_to_string(node.comparators[0])
        op = {ast.Eq: '==', ast.NotEq: '!=', ast.Lt: '<', ast.LtE: '<=', ast.Gt: '>', ast.GtE: '>='}
        return f"{left} {op[type(node.ops[0])]} {right}"
    elif isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Constant):
        return repr(node.value)
    else:
        raise ValueError(f"Unsupported AST Node: {type(node)}")


