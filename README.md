🚗 Automated Car Parking System using Machine Learning
An intelligent computer vision-based system that automatically detects parking space occupancy in real-time using machine learning and image processing techniques.

📋 Project Overview
This system processes video footage from parking lots to identify available and occupied parking spaces. It uses a combination of traditional computer vision and machine learning approaches to provide real-time parking space monitoring without requiring expensive sensor infrastructure.

🛠️ Technical Implementation
Approaches Used
1. Background Subtraction Method
   - Uses MOG2 background subtractor for motion detection
   - Processes video frames to detect changes in parking spaces
   - Calculates occupancy based on pixel differences

2. Color-based Detection
- Utilizes color thresholding in HSV color space
- Detects vehicles based on color characteristics
- Provides an alternative detection methodology

Key Features
- Real-time Processing: Processes video streams in real-time
- Multiple Detection Methods: Implements both background subtraction and color-based detection
- Visual Feedback: Displays parking status with color-coded bounding boxes
- Occupancy Statistics: Tracks and displays available/total parking spaces
- Configurable Parameters: Adjustable thresholds for different lighting conditions

🚀 Installation & Setup
Prerequisites
- Python 3.7+
- OpenCV
- NumPy

Installation Steps
- Clone the repository
  - git clone https://github.com/shail0iri/Automated-Car-Parking-System-using-ML.git
- cd Automated-Car-Parking-System-using-ML

- Install dependencies
pip install -r requirements.txt

- Run the application
python main.py


💻 Usage
Running the System
1. Ensure you have a video file named parking.mp4 in the project directory
2. Execute the main script:
    python main.py


The system will:
- Open the video stream
- Process frames in real-time
- Display parking space status with color-coded indicators
- Show occupancy statistics in the console

Controls
- Press q to quit the application
- Press p to pause/resume video playback

🔧 Configuration:

The system includes several configurable parameters:
- Detection Threshold: Sensitivity for space occupancy detection
- ROI Coordinates: Parking space boundaries (currently hardcoded)
- Processing Resolution: Frame size optimization
- Color Ranges: HSV values for vehicle detection

📊 Output
- Visual Display: Real-time video with overlaid parking status

  🟢 Green: Available space
  🔴 Red: Occupied space

- Console Output: Continuous updates of available/total spaces
- Statistics: Occupancy percentage and space utilization

🎯 Key Algorithms & Techniques
1. Computer Vision
- Frame differencing and background subtraction
- Color space transformation (BGR to HSV)
- Contour detection and analysis
- Region of Interest (ROI) processing

2. Machine Learning
- MOG2 (Mixture of Gaussians) background subtractor
- Adaptive thresholding for various lighting conditions
- Noise reduction and morphological operations

🤝 Contributing
- Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

📝 License
- This project is open source and available under the MIT License.

🙏 Acknowledgments
- OpenCV community for comprehensive computer vision libraries

Contributors to the Python ecosystem

- Sample data providers for testing and development
This project is designed for educational and research purposes. For production deployment, additional considerations for lighting conditions, camera angles, and environmental factors would be necessary.
