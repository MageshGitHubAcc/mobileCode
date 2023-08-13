import subprocess
import os
import shutil
# import requests
import json
import sys
import os.path
# from requests.exceptions import ConnectionError
with open('build.json', 'r') as f:
    config = json.load(f)
choice = sys.argv[1]
print("You choosed : %s" % choice)
tspath = config['paths'][choice]['tspath']
xmlpath = config['paths'][choice]['xmlpath']
jsonpath = config['paths'][choice]['jsonpath']
apkpath = config['paths'][choice]['apkpath']
shutil.copy2(xmlpath, "config.xml")
shutil.copy2(tspath, "src/app/config.ts")
shutil.copy2(jsonpath, "google-services.json")
print("Configuration changed successfully for %s" % choice)
# if !os.path.isdir("node_modules"):
#     cmd = "npm i"
#     p = subprocess.Popen(cmd, shell=True)
#     out, err = p.communicate()
#     print("node modules updated")
# try:
#     shutil.copy2('build/node_modules/angular2-signaturepad/signature-pad.js',
#                  'node_modules/angular2-signaturepad/signature-pad.js')
#     shutil.copy2('build/node_modules/signature_pad/dist/signature_pad.mjs',
#                  'node_modules/signature_pad/dist/signature_pad.mjs')
#     print("Image Annotation files updated")
#     # Directories are the same
# except shutil.Error as e:
#     print('Directory not copied. Error: %s' % e)
#     # Any error saying that the directory doesn't exist
# except OSError as e:
#     print('Directory not copied. Error: %s' % e)
# cmd = "ionic serve"
# p = subprocess.Popen(cmd, shell=True)
# out, err = p.communicate()

