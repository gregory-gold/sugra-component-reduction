file_path = "/Users/uqggold/Dropbox/2021_Honours_Project_Material/cadabra/cadabra_gitrepo/5d_N1/Greg/expressions"

def save_expression(exp, file_name, path = file_path):
    with open(path + "/" + file_name, "w") as file:
        file.write(exp.input_form()+"\n")

def read_expression(file_name, path = file_path):
    with open(path + "/" + file_name, "r") as file:
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

    def print_time(self,precision = 2):
        print(str(round(self.end_time - self.start_time, precision)) + 's') 

