# Python_Objectify_
---

```markdown
# Objectify - Assistive Real-Time Object Recognition

**Objectify** is an accessible AI-powered web application that enables real-time object detection and natural language interaction. It is designed to support individuals with visual impairments or those needing help identifying objects through a webcam interface.

## 🔍 Features

- 🎥 **Live Object Detection** using webcam and TensorFlow.js in-browser
- 🧠 **AI-powered Object Chatbot** (MAYA AI) to describe detected objects
- 🌐 **Flask Backend** for enhanced server-side processing using TensorFlow Hub
- 🎨 **Responsive UI** with styled components for seamless UX
- 📦 **Pre-trained SSD MobileNet v2 Model** for accurate object detection

## 🚀 Live Demo

[Insert link here if deployed]

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, TensorFlow.js, COCO-SSD
- **Backend**: Flask, TensorFlow, TensorFlow Hub, OpenCV, NumPy
- **Model**: [SSD MobileNet v2](https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2)

---

## 📁 Project Structure

```

├── app.py               # Flask backend with object detection & chatbot
├── requirements.txt     # Python dependencies
├── index.html           # Frontend layout and logic
├── styles.css           # UI styling
└── static/
├── camera\_icon.png
├── download.png
└── ai-images\_1247965-5623.jpg

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/objectify.git
cd objectify
````

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Backend

```bash
python app.py
```

The backend will start on `http://0.0.0.0:5000/`

### 4. Open `index.html`

Simply open `index.html` in your browser to launch the front-end.

> ✅ Make sure the Flask server is running and accessible from the browser.

---

## 💬 How It Works

1. **Webcam Feed** is used to capture real-time frames.
2. **TensorFlow\.js (frontend)** or **TensorFlow Hub (backend)** detects objects in the frame.
3. Detected objects are listed visually.
4. The user can **ask questions about detected objects**, and the AI will respond with descriptive information.

---

## 🧠 Example Chatbot Use

```plaintext
User: What is the laptop?
MAYA AI: The object 'laptop' is detected. A laptop is a portable computer used for various tasks.
```

---

## 🧩 Customization

You can update the `object_descriptions` dictionary in `app.py` to add more object explanations, or even connect it to a knowledge base or AI service for dynamic responses.

---

## 🛡️ License

MIT License

---

## 👥 Contributors

* [Dayamay Das](https://github.com/daya-2619)

---

## ❤️ Acknowledgments

* TensorFlow Team
* COCO Dataset
* OpenCV
* Flask

---

## 📌 Note

This project is intended for educational and accessibility-enhancing purposes.


