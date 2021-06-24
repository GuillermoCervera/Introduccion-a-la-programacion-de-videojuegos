# Guillermo José Cervera Cervera

import sys
from Activity11 import activity11

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    application=activity11.Execution()
    application.run()

if __name__=='__main__':
    sys.exit(main())
