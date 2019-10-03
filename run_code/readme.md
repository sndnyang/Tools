# run and tune parameters

Usage:

    ./run_gpu.sh any_script_file_support_command_line_parameters  the_parameter_file

An example of the parameter file(usually .ini file):

    [default]
    lmbd=0.1,1,10
    c=1,10,20
    w=1,5,10
    u=0,1,10
    index-i=1,2

Make sure your script use parameters with '--' prefix.  --dir --data --lambda.  Don't support sinle '-', such as -t -port.

Use some_exp.py to get and check the parameters list.

## requirements

1. termcolor
2. GPUtil

## What you need to edit

1. para.ini, the parameters and their options
2. from Line 70, change the values.

