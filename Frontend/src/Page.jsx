import React, { useState } from "react";
import SyntaxHighlighter from "react-syntax-highlighter";
import { atomOneDark } from "react-syntax-highlighter/dist/esm/styles/hljs";

const Page = () => {
  const [selectedOption, setSelectedOption] = useState("combineRules");
  // Removed unused state variables
  const [createRuleString, setCreateRuleString] = useState("");
  const [createRuleName, setCreateRuleName] = useState("");
  const [evaluateRule, setEvaluateRule] = useState("");
  const [evaluateDataRule, setEvaluateDataRule] = useState({
    age: 30,
    department: "IT",
    salary: 60000,
    experience: 4,
  });
  const [combineRuleOne, setCombineRuleOne] = useState("");
  const [combineRuleTwo, setCombineRuleTwo] = useState("");
  const [combineRuleName, setCombineRuleName] = useState("");

  const [evaluateDataInput, setEvaluateDataInput] = useState(
    JSON.stringify(evaluateDataRule, null, 2)
  );
  const [answer, setAnswer] = useState({});

  const fetch_data = async (value) => {
    const url = "http://127.0.0.1:5000";
    const Createbody = {
      rule_string: createRuleString,
      rule_name: createRuleName,
    };
    const evaluatebody = {
      rule_string: evaluateRule,
      data: evaluateDataRule,
    };
    const combinebody = {
      rules: [combineRuleOne, combineRuleTwo],
      rule_name: combineRuleName,
    };

    let options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    };

    if (value === "create_rule") {
      options.body = JSON.stringify(Createbody);
    } else if (value === "evaluate_rule") {
      options.body = JSON.stringify(evaluatebody);
    } else if (value === "combine_rules") {
      options.body = JSON.stringify(combinebody);
    }

    const response = await fetch(`${url}/${value}`, options);
    const data = await response.json();
    if (response.ok) {
      // console.log(data);
      setAnswer(data);
    } else {
      // console.log(data);
      setAnswer(data);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Handle form submission based on selectedOption
    if (selectedOption === "createRule") {
      await fetch_data("create_rule");
    } else if (selectedOption === "combineRules") {
      await fetch_data("combine_rules");
    } else if (selectedOption === "evaluateRule") {
      await fetch_data("evaluate_rule");
    }
  };

  const handleEvaluateDataChange = (e) => {
    const inputValue = e.target.value;
    setEvaluateDataInput(inputValue);

    // Try to parse the input value as JSON
    try {
      const parsedData = JSON.parse(inputValue);
      setEvaluateDataRule(parsedData);
    } catch (error) {
      // Handle invalid JSON input
      // console.error("Invalid JSON:", error);
    }
  };

  return (
    <div className="max-w-full max-h-full bg-black">
      <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white px-4">
        <h1 className="text-2xl mb-4">Rule Engine</h1>
        <form
          onSubmit={handleSubmit}
          className="p-8 border border-gray-700 rounded bg-gray-800 text-white mb-8 flex flex-col gap-4 justify-center items-center w-full max-w-lg"
        >
          <div className="mb-4 flex flex-col sm:flex-row">
            <label className="mr-4 mb-2 sm:mb-0">
              <input
                type="radio"
                name="option"
                value="combineRules"
                checked={selectedOption === "combineRules"}
                onChange={() => setSelectedOption("combineRules")}
                className="mr-2"
              />
              Combine Rules
            </label>
            <label className="mr-4 mb-2 sm:mb-0">
              <input
                type="radio"
                name="option"
                value="createRule"
                checked={selectedOption === "createRule"}
                onChange={() => setSelectedOption("createRule")}
                className="mr-2"
              />
              Create Rule
            </label>
            <label>
              <input
                type="radio"
                name="option"
                value="evaluateRule"
                checked={selectedOption === "evaluateRule"}
                onChange={() => setSelectedOption("evaluateRule")}
                className="mr-2"
              />
              Evaluate Rule
            </label>
          </div>
          {selectedOption === "createRule" ? (
            <>
              <input
                type="text"
                className="p-4 border border-gray-700 rounded bg-gray-800 text-white mb-4 w-full"
                placeholder="age > 30 AND salary > 50000"
                value={createRuleString}
                onChange={(e) => setCreateRuleString(e.target.value)}
              />
              <input
                type="text"
                className="p-4 border border-gray-700 rounded bg-gray-800 text-white w-full"
                placeholder="Enter rule name"
                value={createRuleName}
                onChange={(e) => setCreateRuleName(e.target.value)}
              />
            </>
          ) : selectedOption === "combineRules" ? (
            <>
              <input
                type="text"
                className="p-4 border border-gray-700 rounded bg-gray-800 text-white mb-4 w-full"
                placeholder="eg: age > 30 AND salary > 50000"
                value={combineRuleOne}
                onChange={(e) => setCombineRuleOne(e.target.value)}
              />
              <input
                type="text"
                className="p-4 border border-gray-700 rounded bg-gray-800 text-white mb-4 w-full"
                placeholder="eg: age > 30 AND salary > 50000"
                value={combineRuleTwo}
                onChange={(e) => setCombineRuleTwo(e.target.value)}
              />
              <input
                type="text"
                className="p-4 border border-gray-700 rounded bg-gray-800 text-white w-full"
                placeholder="Enter rule name"
                value={combineRuleName}
                onChange={(e) => setCombineRuleName(e.target.value)}
              />
            </>
          ) : selectedOption === "evaluateRule" ? (
            <>
              <input
                type="text"
                className="p-4 border border-gray-700 rounded bg-gray-800 text-white mb-4 w-full"
                placeholder="eg: age == 30 and (department == 'IT' and salary > 50000)"
                value={evaluateRule}
                onChange={(e) => setEvaluateRule(e.target.value)}
              />
              <textarea
                className="p-4 border border-gray-700 rounded bg-gray-800 text-white w-full"
                placeholder='{"data": {"age": 30, "department": "IT", "salary": 60000, "experience": 4}}'
                value={evaluateDataInput}
                onChange={handleEvaluateDataChange}
              />
            </>
          ) : (
            ""
          )}
          <button
            type="submit"
            className="mt-4 p-4 bg-blue-500 rounded w-full sm:w-auto hover:bg-blue-600 transition-all ease-linear duration-150"
          >
            Submit
          </button>
        </form>
        <div className="p-8 border border-gray-700 rounded bg-gray-800 text-white w-full max-w-4xl">
          {answer && (
            <>
              {answer.message && (
                <h2 className="text-xl mb-4 text-green-400 items-center flex justify-center">
                  RESPONSE : {answer.message}
                </h2>
              )}
              {answer.error && (
                <h2 className="text-xl mb-4 text-red-600">
                  ERROR : {answer.error}
                </h2>
              )}
              {answer.combined_ast && (
                <h2 className="text-xl mb-4">
                  Combined AST : {answer.combined_ast}
                </h2>
              )}
              {answer.result && (
                <h2 className="text-xl mb-4">RESULT : {answer.result}</h2>
              )}

              {answer.ast && (
                <SyntaxHighlighter language="json" style={atomOneDark}>
                  {JSON.stringify(answer.ast, null, 2)}
                </SyntaxHighlighter>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default Page;
