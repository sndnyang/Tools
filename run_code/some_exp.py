import argparse
import configparser

parser = argparse.ArgumentParser(description='parameters combinations',
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--file', default='para.ini', type=str, help='config file (default: para.ini)')

args = parser.parse_args()
file_name = args.file

config = configparser.ConfigParser()

config.read(file_name)

# d = {"w": config.get('default', 'w', fallback='1'), "lmbd": config.get('default', 'lmbd', fallback='1'),
#      "c": config.get('default', 'c', fallback='1'),
#      "u": config.get('default', 'u', fallback='1'),
#      "index-i": config.get('default', 'index-i', fallback='1'),
#      }
options = config.options(config.sections()[0])


def iterates(lists, level, prod):
    if level == len(lists):
        param_str = ""
        for e in range(level):
            if prod[e] not in ['true', 'false']:
                param_str += "--%s=%s " % (lists[e], prod[e])
            elif prod[e] == 'true':
                param_str += "--%s " % lists[e]

        print(param_str)
        return
    for e in config.get('default', lists[level]).split(","):
        iterates(lists, level+1, prod + [e.strip()])


iterates(options, 0, [])
