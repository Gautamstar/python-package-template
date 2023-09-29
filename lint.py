#lint.py 

import sys 

from pylint import lint  

THRESHOLD = 9  

run = lint.Run(["hello_world.py"], do_exit=False) 

score = run.linter.stats["hello_world"]  

if score < THRESHOLD: 

    print("Linter failed: Score < threshold value") 

    sys.exit(1) 


sys.exit(0) 
