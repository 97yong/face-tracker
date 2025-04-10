<h1 align="center">🧑‍💻 Face Tracking with MTCNN + BoxMot</h1>

<p align="center">
  This project performs <strong>multi-face tracking</strong> using 
  <a href="https://github.com/timesler/facenet-pytorch" target="_blank">MTCNN</a> for face detection and 
  <a href="https://github.com/mikel-brostrom/boxmot" target="_blank">BoxMot</a> for tracking.
</p>

<hr>

<h2>📽️ Demo</h2>
<ul>
  <li>Test Video: <a href="https://motchallenge.net/vis/MOT16-08" target="_blank"><strong>MOT16-08</strong></a> from the MOTChallenge benchmark</li>
  <li>Trackers tested: <code>BoT-SORT</code>, <code>ByteTrack</code>, <code>OCSORT</code> (via BoxMot)</li>
</ul>

<h2>🛠️ Features</h2>
<ul>
  <li>✅ Face detection with <strong>MTCNN</strong></li>
  <li>✅ Tracker selection: BoT-SORT / ByteTrack / OCSORT</li>
  <li>✅ Confidence-based face filtering</li>
  <li>✅ Real-time thumbnail gallery for tracked faces</li>
  <li>✅ Modular Python codebase</li>
</ul>

<h2>🗂️ Project Structure</h2>

<pre><code>face_tracking_project/
├── main.py                    # Entry point
├── arguments.py               # CLI options
├── face_tracking/
│   ├── tracking_runner.py     # Main tracking logic
│   ├── select_tracker.py      # Tracker selection
│   └── gallery_drawer.py      # Draw face thumbnails
</code></pre>

<h2>🚀 How to Run</h2>

<ol>
  <li><strong>Install dependencies</strong></li>
  <pre><code>pip install facenet-pytorch boxmot opencv-python</code></pre>

  <li><strong>Run the tracker</strong></li>
  <pre><code>python main.py \
  --video_path ./assets/source_lab.mp4 \
  --tracker botsort \
  --reid_weights mobilenetv2_x1_4_market1501.pt \
  --output_path output_custom_draw.mp4
</code></pre>
</ol>

<h2>⚙️ CLI Options</h2>

<table>
  <tr><th>Argument</th><th>Description</th><th>Default</th></tr>
  <tr><td><code>--video_path</code></td><td>Path to input video</td><td><code>./data/MOT16-08-raw.webm</code></td></tr>
  <tr><td><code>--output_path</code></td><td>Path to save result video</td><td><code>output_custom_draw.mp4</code></td></tr>
  <tr><td><code>--tracker</code></td><td>Tracking model (botsort / bytetrack / ocsort)</td><td><code>botsort</code></td></tr>
  <tr><td><code>--reid_weights</code></td><td>Path to re-ID model (BoT-SORT only)</td><td><code>mobilenetv2_x1_4_market1501.pt</code></td></tr>
  <tr><td><code>--conf_thresh</code></td><td>Minimum confidence for detection</td><td><code>0.99</code></td></tr>
  <tr><td><code>--max_faces</code></td><td>Max face thumbnails in gallery</td><td><code>6</code></td></tr>
</table>

<h2>📌 References</h2>

<ul>
  <li>
    <strong>Dataset</strong>: 
    <a href="https://motchallenge.net/vis/MOT16-08" target="_blank">MOTChallenge - MOT16-08</a>
  </li>
  <li>
    <strong>Tracker Library</strong>: 
    <a href="https://github.com/mikel-brostrom/boxmot" target="_blank">boxmot (GitHub)</a>
  </li>
</ul>

## 🎬 Demo Videos

<table>
  <tr>
    <td align="center"><strong>🔹 Original Video (MOT16-08)</strong></td>
    <td align="center"><strong>🔸 Tracking Result (BoT-SORT)</strong></td>
  </tr>
  <tr>
    <td>
      <video width="350" controls>
        <source src="./data/MOT16-08-raw.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video width="350" controls>
        <source src="./output_custom_draw.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
</table>

