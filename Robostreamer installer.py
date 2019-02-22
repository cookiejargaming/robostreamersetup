import os
import urllib.request
import subprocess 
import zipfile

menu = input("1. Install\n>")
if menu == "1":
    #Virtual Cam Install
    print("Downloading VirtualCam, Once Downloaded Promt to install will happen Click all of the next and install buttons to continue")

    urllib.request.urlretrieve("https://github.com/CatxFish/obs-virtual-cam/releases/download/2.0.3/OBS-VirtualCam2.0.3-Installer.exe", "virtualcam.exe")

    subprocess.Popen([r"virtualcam.exe"]) 

    print("Downloading More Pythonfile for Robostreamer")

    urllib.request.urlretrieve("https://github.com/robotstreamer/robotstreamer_win_obs/archive/master.zip", "robostreamer.zip")
    with zipfile.ZipFile("robostreamer.zip","r") as zip_ref:
        zip_ref.extractall()
    os.rename("robotstreamer_win_obs-master", "robostreamer")

    print("Downloading ESpeak, For TTS")
    urllib.request.urlretrieve("https://github.com/cookiejargaming/robotstreamerinstall/blob/master/espeak.exe?raw=true", "robostreamer/espeak.exe")

    print("Download FFMeg Shit")
    urllib.request.urlretrieve("https://www35.zippyshare.com/d/UJe8EBIl/2000379/ffmpeg.exe", "robostreamer/ffmpeg.exe")
    urllib.request.urlretrieve("https://www38.zippyshare.com/d/zlupXGit/2352640/ffplay.exe", "robostreamer/ffplay.exe")

    print("Everything has been downloaded, Time for customising your Run.bat so you can stream straight away")

    streamkey = input("Please enter your streamkey\n>")
    robotid = input("Please Enter Your RobotID\n>")
    cameraid = input("Please enter your cameraid\n>")
    f = open("robostreamer/start.bat",'r')
    filedata = f.read()
    f.close()

    bannacheesecake = filedata.replace("CAMERA_ID_GOES_HERE", cameraid)
    controlkey = bannacheesecake.replace("STREAM_KEY_GOES_HERE", streamkey)
    robotidreplace = controlkey.replace("ROBOT_ID_GOES_HERE", robotid)
    newdata = robotidreplace.replace("CONTROL_KEY_GOES_HERE", streamkey)

    f = open("robostreamer/start.bat",'w')
    f.write(newdata)
    f.close()
    os.remove("robostreamer.zip")
    print("Goodbye, Made by TeddyTR")
    os.system("pause")

   
