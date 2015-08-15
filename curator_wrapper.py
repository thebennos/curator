import argparse
import subprocess
import sys

""" This scripts aims to handle the return codes of the curator tool. It returns
    an exit code 99 when the not indices were found for the specific arguments.
    We should handle this situation.
"""


def curator_executor(args):
    print "Calling curator elasticsearch process..."
    print "Arguments: curator {0}".format(args)

    result = subprocess.Popen(["curator {0}".format(args)], shell=True, stdout=subprocess.PIPE)
    for line in iter(result.stdout.readline, b''):
        if line:
            print line
    result.wait()

    print "Returned exit code {}".format(result.returncode)
    if int(result.returncode) == 99:
        print "WARNING: No indices matched provided args"
    elif int(result.returncode) !=0:
        sys.exit(int(result.returncode))

    print "Elasticsearch Curation COMPLETED!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--curator_args')
    args = parser.parse_args()

    curator_executor(args.curator_args)
