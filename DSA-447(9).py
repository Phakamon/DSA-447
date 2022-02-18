{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "df878700",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bd35822f",
   "metadata": {},
   "outputs": [],
   "source": [
    "capture = cv2.VideoCapture('Elon Musk 320.mp4')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fcfca80d",
   "metadata": {},
   "outputs": [
    {
     "ename": "error",
     "evalue": "OpenCV(4.5.5) D:\\a\\opencv-python\\opencv-python\\opencv\\modules\\imgproc\\src\\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31merror\u001b[0m                                     Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-33fc35fad811>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0m_\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mframe\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcapture\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mimshow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Image'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mframe\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[1;31m# Esc button for closing window\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31merror\u001b[0m: OpenCV(4.5.5) D:\\a\\opencv-python\\opencv-python\\opencv\\modules\\imgproc\\src\\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    _, frame = capture.read()\n",
    "    cv2.imshow('Image', frame)\n",
    "\n",
    "    # Esc button for closing window\n",
    "    keyboard = cv2.waitKey(30 & 0xff)\n",
    "    if keyboard==27:\n",
    "        break\n",
    "capture.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4daeacc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#capture = cv2.VideoCapture(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4fa44e0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
