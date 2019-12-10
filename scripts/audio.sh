#!/bin/bash
export ROUTE=$PWD
if grep -s -q "MX8MQ" /sys/firmware/devicetree/base/model; then
	echo "installing auto code on Coral"
  crontab -r
  line="@reboot python3 $ROUTE/Audio/audio_loop.py"
  (crontab -u "mendel" -l; echo "$line" ) | crontab -u "mendel" -
  line="@reboot $ROUTE/Audio/test.sh "
  (crontab -u "mendel" -l; echo "$line" ) | crontab -u "mendel" -
  line="@reboot sudo python3 $ROUTE/RobotCode.py"
  (crontab -u "mendel" -l; echo "$line" ) | crontab -u "mendel" -

else
  # Install gstreamer
  #sudo apt-get install -y gstreamer1.0-plugins-bad gstreamer1.0-plugins-good py$

  if grep -s -q "Raspberry Pi" /sys/firmware/devicetree/base/model; then
	echo "installing auto code on pi"
  
	line="@reboot python3 $ROUTE/Audio/audio_loop.py"
  (crontab -u "pi" -l; echo "$line" ) | crontab -u "pi" -
  line="@reboot $ROUTE/Audio/test.sh "
  (crontab -u "pi" -l; echo "$line" ) | crontab -u "pi" -
  line="@reboot sudo python3 $ROUTE/RobotCode.py"
  (crontab -u "pi" -l; echo "$line" ) | crontab -u "pi" 
  


  fi
fi
