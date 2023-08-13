import subprocess

# Command to build the Ionic application and generate the APK using Ionic Cordova
build_command = "ionic cordova build android --prod"

# Run the build command
subprocess.run(build_command, shell=True, check=True)