import sys
import argparse
import configparser

# abc=0,1,hello
# x:y=5:1,10:2

parser = argparse.ArgumentParser(description='parameters combinations',
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--file', default='para.ini', type=str, help='config file (default: para.ini)')

args = parser.parse_args()
file_name = args.file

config = configparser.ConfigParser()

config.read(file_name)

options = config.options(config.sections()[0])


def iterates(lists, level, prod):
    if level == len(lists):
        param_str = ""
        for e in range(level):
            # deal with options containing :, like x:y
            option_map = lists[e].split(".")

            values_pair = prod[e].split(":")

            if len(option_map) != len(values_pair):
                print("%s and %s don't match" % (lists[e], prod[e]))
                sys.exit(-1)

            for i in range(len(values_pair)):
                if values_pair[i] not in ['true', 'false']:
                    param_str += "--%s=%s " % (option_map[i], values_pair[i])
                elif values_pair[i] == 'true':
                    param_str += "--%s " % option_map[i]

        print(param_str)
        return
    for e in config.get('default', lists[level]).split(","):
        iterates(lists, level+1, prod + [e.strip()])


iterates(options, 0, [])
