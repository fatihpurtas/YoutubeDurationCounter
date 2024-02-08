<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>YouTube Video Duration Calculator</h1>
    <p>This Python script calculates the total duration of a list of YouTube videos provided in a text file. It utilizes the <code>pytube</code> library to fetch the duration of each video and then sums them up to provide the total duration.</p>
    <h2>Features</h2>
    <ul>
        <li><strong>Video Duration Retrieval:</strong> Retrieves the duration of each YouTube video using the <code>pytube</code> library.</li>
        <li><strong>Total Duration Calculation:</strong> Calculates the total duration of all videos in the list.</li>
        <li><strong>Input from Text File:</strong> Accepts a list of YouTube video links from a text file.</li>
        <li><strong>Error Handling:</strong> Handles errors gracefully and continues processing the remaining videos.</li>
    </ul>
    <h2>Usage</h2>
    <ol>
        <li>Run the script (<code>python video_duration_calculator.py</code>).</li>
        <li>Enter the name of the text file containing the list of YouTube video links when prompted.</li>
        <li>The script will calculate the total duration of all videos and display the result.</li>
    </ol>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>pytube</code> library</li>
    </ul>
    <h2>Example</h2>
    <p>Suppose the input text file (<code>video_links.txt</code>) contains the following list of YouTube video links:</p>
    <pre>
        <code>
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=3GwjfUFyY6M
...
        </code>
    </pre>
</body>
</html>
