# test_cases.py

from rule_engine import create_rule, combine_rules, evaluate_rule
import ast

# Test case for rule creation
def test_create_rule():
    rule = "age > 30 AND salary > 50000"
    rule_ast = create_rule(rule)
    print(f"AST for '{rule}':", rule_ast,ast.dump(rule_ast,indent=4))

# Test case for combining rules
def test_combine_rules():
    rule1 = "age > 30 AND department == 'Sales'"
    rule2 = "age < 25 AND department == 'Marketing'"
    combined_ast = combine_rules([rule1, rule2])
    print(f"Combined AST:", combined_ast, ast.dump(combined_ast, indent=4))


def test_evaluate_rule():
    sample_data = {
        "age": 35,
        "department": "Sales",
        "salary": 60000,
        "experience": 3
    }
    rule_string = "age > 30 AND department == 'Sales'"
    rule_ast = create_rule(rule_string)  # Ensure this returns the actual AST node

    # Call evaluate_rule with the actual AST node
    result = evaluate_rule(rule_ast, sample_data)
    print(f"Evaluation result: {result}")

# Call the test function
test_evaluate_rule()



# Run the tests
if __name__ == "__main__":
    test_create_rule()
    test_combine_rules()
    test_evaluate_rule()
