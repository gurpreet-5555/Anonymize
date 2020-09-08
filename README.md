# Anonymize
Program to blur &amp; anonymize faces of strangers based on whitelist containing faces of known people.

In some cases, you might want to blur faces of strangers in your videos to protect the privacy of others. This program allows you to select images of known people (whitelist) which you wish to have in the video while everyone else will be anonymized.

<br>

Some of the applications of anonymization are:<br>
<ul>
  <li>Privacy Protection</li>
  <li>News reporting and journalism</li>
  <li>Vlogging in public</li>
</ul>
  
<br>

<h3>How it works ?</h3>
<br>
This program uses a whitelist containing images of people who shouldn't be anonymized. It is recommended to have atleast 2-3 images of a person to have better face recognition. People who are not a part of whitelist are censored and anonymized in the input video stream.
<br><br>
It uses <b>face_recognition</b> library created by <a href="https://github.com/ageitgey">Adam Geitgey</a> which is built on top of <b>dlib</b> library.
<br>
<a href="https://github.com/ageitgey/face_recognition">Link to face_recognition library</a>
<br>

<h2>Features:</h2>
<ul>
  <li>Whitelist to specify known people</li>
  <li>Support for multiple streaming protocols from IP cameras such as rtsp, http. Can also be used with static video file depending on installed codecs (.mp4, .avi etc..)</li>
  <li>Ability to upscale video resolution for better face detection and recognition</li>
  <li>Option to display the output as the video is being rendered</li>
</ul>  

<h2>Result</h2>
![](sample/videoplayback.mp4)

<h2>Requirements:</h2>
<ul>
  <li>Python 3.6</li>
  <li>OpenCV 3.3.1</li>
  <li>Dlib 19.7.0</li>
  <li>face_recognition 1.3.0</li>
</ul>

<h2>How to use?</h2>
<ul>
  <li>Clone Repository</li>
  <pre>git clone https://github.com/gurpreet-5555/Anonymize.git</pre>  </ul>
<ul>  <li>Navigate to main directory</li>
  <pre>cd Anonymize</pre> </ul>
<ul><li>Add images of known people in directory 'Allowed_faces'. <br>Note: Only one person per image with face clearly visible. Add 3-4 images per person for better face recognition.</li></ul>
<ul><li>Execute Program</li>
  <pre>python Anonymize.py --stream http://192.168.1.43:8080/video --upsample 1 --display True --output "F:\Temp"</pre>
<pre>Arguments -
stream : Source of video feed (http, rtsp etc) or video file. (Required)
upsample: Scale to upsample the image for better face detection. Note: Higher upsample size reduces speed. Default value = 1 (Optional)
display: True: Display frames while rendering input video stream. Default value = False (Optional)
output: Path to output directory
</pre></ul>
