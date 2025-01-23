# Drury Signal Analysis

Spring 2025 classification modeling with signal analysis research at Drury University.

## Resources
  * [Kaggle FORS-EMG](https://www.kaggle.com/datasets/ummerummanchaity/fors-emg-a-novel-semg-dataset?resource=download)

## Concepts
  * [Fast Fourier Transforms](https://en.wikipedia.org/wiki/Fourier_transform)
  * [Short Time Fourier Transforms](https://en.wikipedia.org/wiki/Short-time_Fourier_transform)
  * [Long Short Term Neural Network](https://arxiv.org/pdf/1706.03762)
  * [Recurent neural networks](https://www.ibm.com/topics/recurrent-neural-networks)
  * [Convolutional neural networks](https://en.wikipedia.org/wiki/Convolutional_neural_network)
  * [Transformer Deep Learning Neural Net](https://arxiv.org/pdf/1706.03762)
  * [Generative adversarial networks](https://en.wikipedia.org/wiki/Generative_adversarial_network)
  * [Efficient Memory Transformer](https://arxiv.org/pdf/2010.10759)
  * [Convolutional Layering Transformer](https://arxiv.org/pdf/2209.14868)


 ## Tools
   * Torch audio
   * Arduino
   * Muscle Sensor Device (EMG)

## Ideas 
   * Music
   * Voices
      * Train on songs from artist
      * Classify artists
   * Signal separation
  * EEG (brain) and ECG (heart)
    * Look for anomolies
  * Radio communication
  * Sensor data
  * Generative machine learning (text, audio, etc.)

## Genre Classification
  * Dataset
    * Scrape Spotify song audio and genre from metatdata
  * Use neural network to identify genre from audio data

## Signal Separation
 * Isolate instruments

## EMG Sensor
 * Train neural net to detect and interpret specific muscle movements
## Images
 * Using key points in geometry of hands 
### Sources
 * [EMG Article on classification system for identifying hand and finger movements](https://www.sciencedirect.com/science/article/pii/S2772442522000661#:~:text=Abstract,of%20study%20in%20the%20future.)
 * [EMG Arxiv Paper on Machine Learning-based sEMG Signal Classification for Hand Gesture Recognition](https://arxiv.org/html/2411.15655v1#S3)
   * [FORS-EMG Dataset](https://www.kaggle.com/datasets/ummerummanchaity/fors-emg-a-novel-semg-dataset/data)
 * [Gesture Hand Classification from Google AI](https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer)
   * [HaGRID Dataset](https://www.kaggle.com/datasets/kapitanov/hagrid)
   * [MediaPipe Studio](https://mediapipe-studio.webapps.google.com/studio/demo/gesture_recognizer)
 * [Paper on MediaPipe for perception pipelining](https://arxiv.org/pdf/1906.08172)
 * [Article on using MediaPipe to collect Holistic Key points in hand for sign language. (Uses LSTM), why? ](https://stackoverflow.com/questions/71250674/how-to-associate-mediapipe-holistic-key-points-to-a-sign-language)
 * [Uses own data set to leverage German Sign Language Detection](https://medium.com/@ohr.morris/leveraging-google-mediapipe-for-easy-hand-gesture-classification-8ff2365c202c)

## Datasets
 * Audio MNIST
 * HuggingFace
 * Own Sample Data (From EMG Sensor)
 * Kaggle data
 * Image processing w/MediaPipe

## Other repos
 * [Brayden's Neural Audio Classification Repository](https://github.com/braydenoneal/neural-audio-classification)
