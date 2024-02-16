### This file contains classes with logic or python-specific code useful to all representations. ###
from cadabra2 import *

class ExpressionSaver:
    def __init__(self, file_path):
        self.file_path = file_path
    def save(self, exp, file_name):
        with open(self.file_path + file_name, "w") as file:
            file.write(exp.input_form()+"\n")
    def read(self, file_name):
        with open(self.file_path + file_name, "r") as file:
            exp = Ex(file.readline())
        return exp 

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

                    if self.is_object_a_derivative(object):
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