This is a tool script that can make a mobile phone linear motor vibrate and produce sound by extracting audio metadata (similar to bone conduction headphones)
How to use?
  Single file processing
   /python haptic.py music.ogg
  Batch process the current directory
   /python haptic.py --batch
  Specify file output name
   /python haptic.py input.ogg output.ogg
  You need to add(Dependent Libraries)
   / pip install mutagen
  *****NOTICE*****
You must first convert the audio to 48kHz
Then convert it to *. ogg format file, otherwise it will change tone due to Android resampling mechanism!!!

By YuzakiPTeam@2025
This is the first time there is a problem with this program. Please provide feedback and understanding
Thank you all for your support
Not currently supported for Xiaomi devices (missing relevant APIs)
Currently, the OnePlus 13 model that has passed testing and achieved good results
Two audio files are included in the project, where AF is the sample audio with metadata loaded and BF is the sample audio without metadata loaded
I am not responsible for any problems caused by self testing of other models
Please debug the environment, installation, etc. by yourself
Have fun!