# Anonymize
Program to blur &amp; anonymize faces of strangers based on whitelist containing faces of known people.

In some cases, you might want to blur faces of strangers in your videos to protect the privacy of others. This program allows you to select images of known people (whitelist) which you wish to have in the video while everyone else will be anonymized.

<br><br>

Some of the applications of anonymization are:<br>
<ul>
  <li>Privacy Protection</li>
  <li>News reporting and journalism</li>
  <li>Vlogging in public</li>
</ul>
  
<br><br>

<h3>How it works ?</h3>
<br>
This program uses a whitelist containing images of people who shouldn't be anonymized. It is recommended to have atleast 2-3 images of a person to have better face recognition. People who are not a part of whitelist are censored and anonymized in the input video stream.
<br>
It uses <b>face_recognition</b> library created by <a href="https://github.com/ageitgey">Adam Geitgey</a> which is built on top of <b>dlib</b> library.
<br>
<a href="https://github.com/ageitgey/face_recognition">Link to face_recognition library</a>
<br>

<h2>Features:</h2>
<ul>
  <li>Whitelist to specify known people</li>
  <li>Support for multiple streaming protocols from IP cameras such as rtsp, http. Can also be used with static video file depending on installed codecs(.mp4, .avi etc..)</li>
  <li>Ability to upscale video resolution for better face detection and recognition</li>
  <li>Option to display the output as the video is being rendered</li>
</ul>  

<h2>Result</h2>
