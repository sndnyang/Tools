# run and tune parameters

example:

    [default]
    lmbd=0.1,1,10
    c=1,10,20
    w=1,5,10
    u=0,1,10
    index-i=1,2

Use some_exp.py to get and check the parameters list.

The run_c|gpu.sh will call some_exp.py and run your code/experiments of different parameters when your gpu/cpu usage is fine. 

## What you need to edit

1. run_c|gpu.sh  
    1. your python intepreter path
    2. your main python script
    3. (for gpu) the gpu id list you can use. The list is controled by "head -n" and "c=0". If you want to use GPU 2 3 4 5, you need to change to "tail -n " and "c=2".
2. para.ini, the parameters and their options
    

