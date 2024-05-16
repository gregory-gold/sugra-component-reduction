### This file contains classes with logic or python-specific code useful to all representations. ###
class ExpressionSaver:
    def __init__(self, file_path):
        self.file_path = file_path
    def save(self, exp, file_name):
        with open(self.file_path + file_name, "w") as file:
            file.write(exp.input_form()+"\n")
    def read(self, file_name):
        with open(self.file_path + file_name, "r") as file:
            exp_string = file.readline()
        return exp_string 

import time

class StopWatch:
    def __init__(self):
        self.restart_time()
	
    def pause(self, n):
        time.sleep(n)

    def check_time(self, precision = 2):
        self.end_time = time.time()
        self.print_time(precision)
	
    def restart_time(self):
        self.start_time = time.time()
        self.end_time =  time.time()

    def print_time(self, precision = 2):
        print(str(round(self.end_time - self.start_time, precision)) + 's') 

import re
from cadabra2 import *

class Sort:
    def __init__(self, sort_order, anti_commute):
        self.sort_order_map = {k: v for v, k in enumerate(sort_order)}
        self.anti_commute = anti_commute
    
    def is_object_a_derivative(self, object):
        is_der = False
        for arg in object.args():
            is_der = True
            break
        return is_der

    def sort(self, ex):
        
        for term in ex.top().terms():
            
            # Create convenient list of useful charteristics of each object in term. These are [<entire_object>, <number_of_derivatives>, <fermionic>, <object/nested_object name>, <index1>, ..., <indexN>]
            term_sort = []
            term_exps = []
            if term.name == '\\prod': # Only sort if term is a product of objects.
                for object in term.children():
                    fermionic = False
                    final_object = object
                    der_num = 0
                    for child in object.children():
                        fermionic = not fermionic if re.sub('\d\d|\d','#', child.name) in self.anti_commute else fermionic
                    if object.name == '\\pow':
                        final_object = next(object.children())                                
                    elif self.is_object_a_derivative(object):
                        inside = False
                        current_object = object
                        der_num = 0
                        while not inside:
                            der_num += 1
                            inside = True
                            for arg in current_object.args():
                            
                                for child in arg.children():
                                    fermionic = not fermionic if re.sub('\d\d|\d','#', child.name) in self.anti_commute else fermionic
                                
                                if not self.is_object_a_derivative(arg):
                                    final_object = arg
                                else:
                                    inside = False
                                    current_object = arg
                    term_sort.append([der_num, fermionic, final_object.name] + [index.name for index in final_object.indices()])
                    term_exps.append(object.ex())
                    
                #print(term_sort)		
                # Sort List and check anticommutation if switch field order
                sorting = True
                new_term = Ex(str(term.multiplier))
                debug = 0
                while sorting:
                    debug += 1
                    sorting = False

                    for i in range(1, len(term_sort)):
                        objectL = term_sort[i - 1]
                        objectR = term_sort[i]
                    # Swap Conditions, in order of priority, (letters are equal priority)
                    #1: higher derivative number goes right always
                    #2: if equal derivatives (including zero)
                    #2a: switch if sort_order dictates
                    #2b: if sort_order dictates just one, move that one left
                    #2c: if sort_order dictates neither
                    #2cA: sort lexographic by field name
                    #2cB: if same field, sort lexographic by field+index list
                
                        ### This is poorly optimized. We should only check next condition if previous one doesn't fire.
                        swap_condition_one = (objectL[0] > objectR[0])
                        swap_condition_two_a = (objectL[0] == objectR[0]) and ((objectR[2] in self.sort_order_map) and (objectL[2] in self.sort_order_map)) and (self.sort_order_map[objectL[2]] > self.sort_order_map[objectR[2]])
                        swap_condition_two_b = (objectL[0] == objectR[0]) and ((objectR[2] in self.sort_order_map) and (objectL[2] not in self.sort_order_map))
                        swap_condition_two_cA = (objectL[0] == objectR[0]) and (objectR[2] not in self.sort_order_map) and (objectL[2] not in self.sort_order_map) and objectL[2] > objectR[2]
                        swap_condition_two_cB = (objectL[0] == objectR[0]) and (objectL[2] == objectR[2]) and (objectL[2:] > objectR[2:])
                        
                        if swap_condition_one or swap_condition_two_a or swap_condition_two_b or swap_condition_two_cA or swap_condition_two_cB:				
                            #print('swapping objects ' + str(i) + ' and ' + str(i-1))
                            sorting = True
                            term_sort[i] = objectL
                            term_sort[i - 1] = objectR
                            next(x for j, x in enumerate(term.children()) if j==i).replace(term_exps[i-1])
                            next(x for j, x in enumerate(term.children()) if j==i-1).replace(term_exps[i])
                            placeholder = term_exps[i]
                            term_exps[i] = term_exps[i - 1]
                            term_exps[i - 1] = placeholder
                            if objectL[1] and objectR[1]:
                                term.replace(term.ex() * Ex(-1))
                            #print(term_sort)
        
                # Convert sorted list to expression (signs and multipler already handled)
                # for object in term_sort:
                #	new_term *= Ex(object[0])

                #term.replace(new_term)
        
        return ex
    

class CleanUp:

    def __init__(self, dummy_object = '\\Gamma', dummy_index_positions = [sub, super], epsilon_object = '\\e'):
        self.dummy_object = dummy_object
        self.dummy_index_positions = dummy_index_positions
        self.epsilon_object = epsilon_object

    ### Dummy derivative contraction algorithm ###
    def contract_dummy_auto(self, ex, der_object='\\vD'):

        for term in ex.top().terms():
            for dummy in term[self.dummy_object]:

                index_list = [str(index) for index in dummy.indices()]
                
                for vD in term[der_object]:
            
                    indexIter = next(vD.indices())
                    if index_list[2] == str(indexIter):
                        indexIter.name = index_list[0]
                        indexIter.parent_rel = self.dummy_index_positions[0]
                        next(indexIter).name = index_list[1]
                        indexIter.parent_rel = self.dummy_index_positions[1]
                        term[dummy] = Ex(1)
                        break
        
        return(ex)
    
    ### Epsilon Metric Contraction Algorithm ###
    def contract_epsilon_auto(self, ex):
        # For each term, loop through epsilon metrics and save their indices.
        for term in ex.top().terms():
            for eps in term[self.epsilon_object]:
                index_tuple = tuple(str(index) for index in eps.indices())
                contraction = False

                # Loop through other objects in term to check for contractions.
                for child in term.children():
                    if child.name != self.epsilon_object and child.name != "1" and not contraction:
                        
                        for index in child.indices():

                            if str(index) == index_tuple[1]:
                                contraction = True
                                index.name = index_tuple[0]
                                break
                            elif str(index) == index_tuple[0]:
                                contraction = True
                                index.name = index_tuple[1]
                                child.multiplier = -1
                                break

                        if contraction:
                            if index.parent_rel == sub:
                                index.parent_rel = super
                            else:
                                index.parent_rel = sub
                            eps.name = '1'

        # This removes redundant ones.
        collect_factors(ex)
        return ex