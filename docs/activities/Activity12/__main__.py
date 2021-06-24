# Guillermo José Cervera Cervera

import sys
from Activity12 import activity12

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    application=activity12.Execution()
    application.run()

if __name__=='__main__':
    sys.exit(main())
