import sys
import re
from pyparsing import *
import random

ROUND = 2 ## we round results to two decimal places for checking

MATH_PROBLEMS = [{'problem': 'x/y', 'in_vars': {'x': 1.0, 'y': 1.0}, 'output': 1.0, 'derivative': {'x': 1.0, 'y': -1.0}},
 {'problem': 'exp(x) - (y * 2)', 'in_vars': {'x': 2.0, 'y': -2.0},'output': 11.39, 'derivative': {'x': 7.39, 'y': -2.0}},
 {'problem': '(x^2 - 1) * (y+2)', 'in_vars': {'x': 3.0, 'y': 2.0}, 'output': 32.0, 'derivative': {'x': 24.0, 'y': 8.0}},
 {'problem': 'z + sin(x^(2) + (y * exp(z)))', 'in_vars': {'x': 2.0, 'y': -1.0, 'z': 0.0}, 'output': 0.14, 'derivative': {'x': -3.96, 'y': -0.99, 'z': 1.99}}]


class Parser():

    def __init__(self, print_res: bool = False):

        self.print_res = print_res
        self.expr = self.infix_notation_parser()

    def parse(self, math_string: str, in_vars: dict = {}):
        """
        math_string: str describing math equation, e.g. 'z + sin(x^(2) + y * exp(z))'
        in_vars: optional dict of mapping between input variables and numbers
        RETURN: list of infix parsed string, returns dict of input used_vars
        """
        if self.print_res:
            print(f"\nproblem: {math_string} with input {in_vars}")
        in_vars = self.get_input_variables(math_string, in_vars)
        infix_list = self.expr.parseString(math_string).asList()[0]
        return infix_list, in_vars

    def infix_notation_parser(self, ):
        """
        RETURN: expr py_parse object
        """

        ppc = pyparsing_common

        ParserElement.enablePackrat()
        sys.setrecursionlimit(3000)

        integer = ppc.integer
        variable = Word(alphas, exact=1)
        operand = integer | variable

        expop = Literal("^")
        factop = Literal("!")
        ident = Word(alphas, alphanums + "_$")
        signop = oneOf("+ -")
        multop = oneOf("* /")
        plusop = oneOf("+ -")
        #e = CaselessKeyword("E")
        #pi = CaselessKeyword("PI")

        expr = infixNotation(
            operand,
            [
                (ident, 1, opAssoc.RIGHT),
                (factop, 1, opAssoc.LEFT),
                (expop, 2, opAssoc.RIGHT),
                (signop, 1, opAssoc.RIGHT),
                (multop, 2, opAssoc.LEFT),
                (plusop, 2, opAssoc.LEFT),
            ],
        )

        return expr


    def get_input_variables(self, math_string: str, in_vars: dict = {}):
        """
        math_string: str describing math equation, e.g. 'z + sin(x^(2) + y * exp(z))'
        in_vars: optional dict of mapping between input variables and numbers
        RETURN: returns dict of input used_vars
        """

        in_var_list = list(set(re.findall(r'(?i)(?<![a-z])[a-z](?![a-z])', math_string)))
        random_in_vars = {}

        filtered_in_vars = {}
        for in_var in in_var_list:
            if in_var not in in_vars.keys():
                random_in_vars[in_var] = float(random.randint(1, 3)) ## random input
            else:
                filtered_in_vars[in_var] = in_vars[in_var]

        if self.print_res:
            print(f"generated random input {random_in_vars} and kept {filtered_in_vars}")
        return {**filtered_in_vars, **random_in_vars}



def test_backprop(Builder, Executor, math_problems = None):

    if math_problems == None:
        math_problems = MATH_PROBLEMS
    elif isinstance(math_problems, dict):
        math_problems = [math_problems]
    elif isinstance(math_problems, list):
        pass
    else:
        assert "math_problems must be None, dict or list"

    ## set up parser
    parser = Parser()

    ## iterate through math problems
    for i, math_problem in enumerate(math_problems):

        ## Step 1 ________________
        ## the math problem is parsed into infix notation
        infix_str, in_vars = parser.parse(math_problem["problem"], in_vars = math_problem["in_vars"])

        ## Step 2 ________________
        ## take infix_str and in_vars and build a computation graph
        ## it is not required that parallel executions are parallelized
        b = Builder(infix = infix_str, in_vars = in_vars)

        ## Step 3 ________________
        ## execute the edges
        ## your method should set float output: x and dict derivative: {'y': -1.0, 'x': 1.0}
        e = Executor(graph = b.graph, in_vars=in_vars)
        e.forward()
        e.backward()

        ## Step 4 ________________
        ## we are testing our solution
        ## output --> float comparison
        print(f"\n{str(i)}: problem: {math_problem['problem']}, in_vars: {math_problem['in_vars']}")
        if round(e.output,2) == round(math_problem["output"], ROUND):
            print(f"SUCCESS output: {round(e.output, ROUND)}")
        else:
            print(f"FAILURE output: {round(e.output, ROUND)} != {math_problem['output']}")

        ## first derivative --> dict comparison
        true_deriv = {k: round(v, ROUND) for k, v in math_problem["derivative"].items()}
        e.derivative = {k: round(v,ROUND) for k,v in e.derivative.items()}
        if e.derivative == true_deriv:
            print(f"SUCCESS derivative: {e.derivative}")
        else:
            print(f"FAILURE derivative: {e.derivative} != {math_problem['derivative']}")


if __name__ == '__main__':
    pass
