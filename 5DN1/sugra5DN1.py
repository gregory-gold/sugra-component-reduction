## This file simplies imports of appropriate modules (and definitions of paths) ##
import sys
current_path = str(sys.path[0])
repo_name  = 'sugra-component-reduction'
repo_path = current_path.split(repo_name)[0] + repo_name
module_path = repo_path + '/5DN1/modules/'
py_path = repo_path + '/py/'
sys.path.append(module_path)
sys.path.append(py_path)

from shared import *
from latex_macros5D import *                                                  
from properties5D import *
from substitutions5D import *
from methods5D import *
from objects5D import *