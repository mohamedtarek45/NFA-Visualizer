import pygraphviz as pgv
from parser_1 import parsing
import re

class NFA:
    def __init__(self, regex, input_string):
        self.regex = regex
        self.input_string = input_string
        self.nfa_agraph = pgv.AGraph(directed=True, landscape='true')
        self.nfa_agraph.node_attr['rotate'] = 90
        self.state_id = 0
        self.states = []
        self.incomplete_or = []
        self.incomplete_closure = []

        self.nfa_agraph.add_node(str(self.state_id), shape="circle")
        self.states.append(self.state_id)
        self.state_id += 1
        self.plot_nfa_graph()
    def validate(self):
        try:
            re.compile(self.regex)
            return True
        except re.error:
            return False
        
    def check(self):
        return re.fullmatch(self.regex, self.input_string) != None
    
    
    def r1_or_r2(self, r1, r2):
        if len(r1) == 1 and len(r2) == 1:
            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")

            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label=str(r1))

            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-4]), str(self.states[-1]), label="ε")

            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label=str(r2))

            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-4]), str(self.states[-1]), label="ε")
            self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")

        else:
            if len(r1) == 1:
                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")

                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.incomplete_or.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label=str(r1))
                
                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-4]), str(self.states[-1]), label="ε")

                self.sub_plot(r2)

                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.incomplete_or.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")

            elif len(r2) == 1:
                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")

                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.incomplete_or.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label=str(r2))
                
                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-4]), str(self.states[-1]), label="ε")

                self.sub_plot(r1)

                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.incomplete_or.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")

            else:
                pinned_state = self.states[-1]
                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")

                self.sub_plot(r1)

                pinned_state_2 = self.states[-1]

                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(pinned_state), str(self.states[-1]), label="ε")

                self.sub_plot(r2)

                self.nfa_agraph.add_node(str(self.state_id), shape="circle")
                self.states.append(self.state_id)
                self.state_id += 1

                self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")
                self.nfa_agraph.add_edge(str(pinned_state_2), str(self.states[-1]), label="ε")


    def sequance(self, r):
        self.nfa_agraph.add_node(str(self.state_id), shape="circle")
        self.states.append(self.state_id)
        self.state_id += 1

        self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label=str(r))

    def r_closure(self, r):
        if len(r) == 1:
            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")

            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-1]), str(self.states[-2]), label="ε")
            self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label=str(r))

            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")
            self.nfa_agraph.add_edge(str(self.states[-4]), str(self.states[-1]), label="ε")

        else:
            self.incomplete_closure.append(self.states[-1])
            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")
            pinned_state = self.states[-1]
            self.sub_plot(r)

            self.nfa_agraph.add_edge(str(self.states[-1]), str(pinned_state), label="ε")
            
            self.nfa_agraph.add_node(str(self.state_id), shape="circle")
            self.states.append(self.state_id)
            self.state_id += 1

            self.nfa_agraph.add_edge(str(self.states[-2]), str(self.states[-1]), label="ε")

            self.incomplete_closure.append(self.states[-1])

    def sub_plot(self, regex):
        tokens = parsing(regex)
        if '|' in tokens:
            index = tokens.index('|')
            r1 = tokens[index-1]
            r2 = tokens[index+1]
            self.r1_or_r2(r1, r2)

        else:
            for token in tokens:
                if len(token)==1:
                    self.sequance(token)
                else:
                    if token[-1] == '*':
                        self.r_closure(token[:-1])
                    if token[0] == '(' and token[-1] == ')':
                        self.sub_plot(token[1:-1])

    def plot_nfa_graph(self):
        
        self.sub_plot(self.regex)

        self.nfa_agraph.add_node(str(self.states[-1]), shape="doublecircle")

        if self.incomplete_or:
            for i in range(len(self.incomplete_or)//2):
                self.nfa_agraph.add_edge(self.incomplete_or[i],self.incomplete_or[-1-i], label="ε")
        
        if self.incomplete_closure:
            for i in range(len(self.incomplete_closure)//2):
                self.nfa_agraph.add_edge(self.incomplete_closure[i],self.incomplete_closure[-1-i], label="ε")

        output_path = "images/nfa_graph.png"
        self.nfa_agraph.draw(output_path, format="png", prog="dot")