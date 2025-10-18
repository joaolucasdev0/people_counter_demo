import cv2
import streamlit as st
import numpy as np

st.title("People Counter - Educational Demo")

run_camera = st.checkbox('Start Camera')

if run_camera:
    stframe = st.empty()
    cap = cv2.VideoCapture(0)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.write("Camera not available")
            break

        frame_small = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)
        boxes, weights = hog.detectMultiScale(gray, winStride=(8,8))
        count = len(boxes)

        for (x, y, w, h) in boxes:
            cv2.rectangle(frame_small, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame_small, f"People: {count}", (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        frame_rgb = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB")

    cap.release()