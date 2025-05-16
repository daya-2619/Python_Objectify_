document.getElementById('camera-icon').addEventListener('click', () => {
    const video = document.getElementById('webcam');
    const canvas = document.getElementById('output');
    const context = canvas.getContext('2d');

    // Access webcam
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
            video.srcObject = stream;
            video.play();

            // Continuously capture frames and send them to the backend for detection
            setInterval(() => {
                context.drawImage(video, 0, 0, 640, 480);

                // Send the current frame to the backend
                canvas.toBlob((blob) => {
                    const formData = new FormData();
                    formData.append('image', blob, 'frame.png');
                    
                    fetch('http://localhost:5000/detect', {
                        method: 'POST',
                        body: formData
                    })
                    .then(response => response.json())
                    .then(data => {
                        // Process and display detected objects
                        const predictions = data.map(prediction => 
                            `${prediction.class} (${Math.round(prediction.score * 100)}%)`
                        ).join(', ');

                        document.getElementById('predictions').innerText = 
                            predictions ? `Detected objects: ${predictions}` : 'No objects detected';
                    })
                    .catch(err => console.error(err));
                }, 'image/png');
            }, 500); // Capture and send frames every 500 ms
        });
    } else {
        alert("Sorry, your browser does not support webcam access.");
    }
});

// Handle video upload and playback
document.getElementById('video-upload').addEventListener('change', (event) => {
    const file = event.target.files[0];
    const videoElement = document.getElementById('user-video');
    
    if (file) {
        const fileURL = URL.createObjectURL(file);
        videoElement.src = fileURL;
        videoElement.play();
    }
});
