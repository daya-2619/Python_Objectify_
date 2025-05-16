from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import cv2

# Load the pre-trained TensorFlow Hub model
model = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2")

# Create Flask app
app = Flask(__name__)

# COCO Class Labels
COCO_LABELS = {1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
               7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
               13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
               18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
               24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
               32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
               37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
               41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
               46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon', 51: 'bowl',
               52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange', 56: 'broccoli',
               57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut', 61: 'cake',
               62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed', 67: 'dining table',
               70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse', 75: 'remote', 76: 'keyboard',
               77: 'cell phone', 78: 'microwave', 79: 'oven', 80: 'toaster', 81: 'sink',
               82: 'refrigerator', 84: 'book', 85: 'clock', 86: 'vase', 87: 'scissors',
               88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush', 91: 'fan', 92: 'pencil',93: 'pen',94:'notebook'}

# Example database of object descriptions
object_descriptions = {
    "person": "A person is a human being.",
    "chair": "A chair is a piece of furniture designed for sitting.",
    "laptop": "A laptop is a portable computer used for various tasks.",
    "bottle": "A bottle is a container used to hold liquids.",
    "book": "A book is a set of written or printed pages bound together."
}

def preprocess_frame(frame):
    """Prepares the image for TensorFlow model"""
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    img_resized = cv2.resize(img, (300, 300))  # Resize to model input size
    input_tensor = np.expand_dims(img_resized, axis=0)  # Add batch dimension
    input_tensor = tf.convert_to_tensor(input_tensor, dtype=tf.uint8)  # Convert to Tensor
    return input_tensor

def detect_objects(frame):
    """Detects objects in a given frame using the model"""
    input_tensor = preprocess_frame(frame)
    results = model(input_tensor)

    # Extract detection information
    detection_boxes = results["detection_boxes"].numpy()[0]
    detection_classes = results["detection_classes"].numpy()[0].astype(int)
    detection_scores = results["detection_scores"].numpy()[0]

    return detection_boxes, detection_classes, detection_scores

@app.route('/detect', methods=['POST'])
def detect():
    """Handles image upload and performs object detection"""
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)  # Corrected deprecated function
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)  # Convert image to OpenCV format

    # Perform object detection
    boxes, classes, scores = detect_objects(frame)

    # Prepare response
    detection_list = []
    for i in range(len(scores)):
        if scores[i] > 0.5:  # Confidence threshold
            detection_list.append({
                'box': boxes[i].tolist(),
                'score': float(scores[i]),
                'class': COCO_LABELS.get(classes[i], 'Unknown')
            })

    return jsonify(detection_list)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    query = data.get("query", "").lower()
    detected_objects = data.get("detected_objects", [])

    # Find a matching object in the detected objects
    for obj in detected_objects:
        if obj.lower() in query:
            description = object_descriptions.get(obj.lower(), f"No description available for {obj}.")
            return jsonify({"response": f"The object '{obj}' is detected. {description}"})

    return jsonify({"response": "I couldn't find the object in the detected list."})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
