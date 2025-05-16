// server.js
const express = require('express');
const multer = require('multer');
const sharp = require('sharp');
const app = express();
const port = 5000;

// Setup multer for file handling
const upload = multer({ storage: multer.memoryStorage() });

// Endpoint to handle image upload and detection
app.post('/detect', upload.single('image'), async (req, res) => {
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }

    try {
        // Process the image (for demonstration, we just convert it to grayscale)
        const processedImage = await sharp(req.file.buffer)
            .grayscale() // Example processing step
            .toBuffer();

        // For demonstration, we'll return a mock response
        // In a real application, you would perform object detection here
        const mockPredictions = [
            { class: 'Object1', score: 0.85 },
            { class: 'Object2', score: 0.75 }
        ];

        res.json(mockPredictions);
    } catch (error) {
        console.error('Error processing image:', error);
        res.status(500).send('Error processing image.');
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
