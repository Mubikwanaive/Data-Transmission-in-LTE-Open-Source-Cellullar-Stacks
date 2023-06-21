# Data-Transmission-in-LTE-Open-Source-Cellullar-Stacks

This project aims to design and implement a 4G network system for transmitting video data from a User Equipment (UE) to a Base Station. It leverages the use of two software solutions, OpenAirInterface and srsRAN, to establish the network infrastructure. 

## Key Features

- Configuration of EnodeB and Core Network using Oracle VirtualBox and Docker-pulled nodes.
- Step-by-step instructions for attaching a UE to the network using OpenAirInterface and srsRAN.
- Two methods for video data transmission:
  - Method 1: Utilizing VLC media player to create a data transmission tunnel. The camera video feed from the Raspberry Pi (UE) is streamed over the http protocol and played on the Base Station (EPC) via the network URL.
  - Method 2: Establishing an SSH connection and using X11 forwarding to view the video feed from the Raspberry Pi on the Base Station.
- Object classification from the video stream using an image-classification model from TensorFlow Hub.
- Implementation of object classification on the Base Station using the TensorFlow Lite API and OpenCV library.

## Usage

1. Clone the repository.
2. Follow the provided instructions for setting up the network infrastructure using OpenAirInterface and srsRAN.
3. Attach a UE to the network following the specified steps for both OpenAirInterface and srsRAN.
4. Choose the preferred method for video data transmission:
   - Method 1: Configure VLC media player and establish the data transmission tunnel.
   - Method 2: Set up an SSH connection with X11 forwarding to view the video feed.
5. Implement object classification on the Base Station using TensorFlow Hub, TensorFlow Lite API, and OpenCV library.
6. Enjoy seamless video data transmission from the UE to the Base Station!

## Contribution

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please submit a pull request.


## Acknowledgments

This project was developed as part of a research effort and serves as a comprehensive resource for researchers and developers working on similar 4G network systems. We would like to thank the creators of OpenAirInterface, srsRAN, TensorFlow Hub, TensorFlow Lite API, and OpenCV for their valuable contributions to the field.
