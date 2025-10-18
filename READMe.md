People Counter - Educational Demo

A minimal people counter demo using Python, OpenCV, and Streamlit. This project demonstrates real-time people detection using the HOG (Histogram of Oriented Gradients) algorithm. It detects people in front of the webcam, shows bounding boxes around them, counts the number of detected persons, and provides a simple Streamlit interface with a checkbox to start the camera.



Features

Detects people in front of the webcam

Shows bounding boxes around detected people

Counts the number of detected persons

Simple Streamlit interface with a checkbox to start the câmera



Installation

Clone the repository:
git clone https://github.com/joaolucasdev/people-counter-demo.git

Change to the project folder:
cd people-counter-demo

Install dependencies:
pip install -r requirements.txt



Usage

Run the Streamlit app:
streamlit run count_people_hog.py

Open the browser and check "Start Camera" to start detection



Notes

This is a minimal educational demo. HOG detection works best with people standing clearly in front of the camera and in good lighting

If detection seems unreliable, consider using a motion-based approach or a modern neural network detector for production



Links

GitHub Repository: https://github.com/joaolucasdev/people-counter-demo

Live Demo (Streamlit Cloud): https://joaolucasdev-people-counter-demo.streamlit.app

