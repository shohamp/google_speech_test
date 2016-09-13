import os
import sys
import subprocess

TOKEN = sys.argv[1]
HERE = os.path.dirname(__file__)
json_path = os.path.join(HERE, "sync-request.json")

success = 0
for i in xrange(100):
    print "Running attempt %d   \r" % (i + 1),
    sys.stdout.flush()
    result = subprocess.check_output('curl -s -k -H "Content-Type: application/json" '
                                     '-H "Authorization: Bearer %s" https://speech.googleapis.'
                                     'com/v1beta1/speech:syncrecognize -d @%s'
                                     % (TOKEN, json_path), shell=True)
    if 'the time' in result.lower():
        success += 1
    else:
        print
        print result

print
print "Succeeded %d times out of 100" % success
