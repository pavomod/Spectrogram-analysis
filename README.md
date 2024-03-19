# Spectrogram-analysys

# Analysis

### Preparatory Phase
To carry out the analysis of the instruments based on their spectrogram on different notes, I have selected four musical instruments and two (same) notes for each, specifically:

* Clarinet (A3, A4)
* Trumpet (A3, A4)
* Guitar (A3, A4)
* Mandolin (A3, A4)

## Code
#### Modules used
* **Librosa:** for uploading audio files, calculating the Short-time Fourier Transform (STFT), converting amplitudes to decibels.
* **NumPy:** for calculating the magnitude of the STFT.
* **Matplotlib:** for creating and visualizing the spectrogram.

#### uploading files
The file containing the musical note is converted into a series of audio samples, denoted with **y**, while **sr** represents the sampling rate of the audio file, i.e., the number of samples per second. By setting **sr=None**, we keep the original sampling rate of the file.
#### Spectrogram
Subsequently, we perform the *Short-time Fourier Transform (STFT)*, breaking down the audio signal into time-varying frequency components. We calculate the magnitude of each component of the transformation to obtain the magnitude, ignoring the phase, resulting in the matrix **D** which contains the amplitudes of the frequencies as a function of time.
Finally, we convert the amplitudes into decibels, using the maximum amplitude value as a reference point **(ref=np.max)**, in order to improve the readability of the spectrogram.

## Spectrogram Analysis
For the analysis of the spectrograms, I considered the following factors:

* **Fundamental Frequency:** The most intense horizontal line at the bottom of the graph
* **Harmonics:** Horizontal lines of higher frequency than the fundamental frequency
* **Attack Shape:** Increase in intensity
* **Sustain:** Phase between the attack and decay
* **Decay:** Decrease in intensity after the sustain

#### Clarinet
In the clarinet, we can identify the fundamental frequency of the note **A3** at about **200Hz** while for the note **A4** at about **440Hz**. The most intense harmonics are present in the range between **500Hz** and **4000Hz**, the higher the frequency, the lower its intensity and duration over time; there is also a distance between the frequencies that decreases as the frequency increases.
We notice a quick attack, but not too abrupt, which could be caused by air friction or by the initial, not too intense blow, followed by a constant sustain without sudden intensity fluctuations. Finally, we note a gradual decay.


#### Trumpet
In the trumpet's spectrogram, the fundamental frequency for the note **A3** is visible around **240Hz**, though less evident compared to the **A4** note which is clear at **500Hz** and the other instruments which are well-defined. The delta between the harmonics is very small and they reach very high frequencies, perhaps due to the very loud sound of the instrument. The attack is sharp, and we deduce this from the sudden change in intensity in the colors at the beginning of the note, continuing as with the clarinet with a uniform sustain and ending with a gradual decrease in the intensity of the colors (from lighter to darker).

#### Guitar
The guitar has a fundamental frequency that appears to be around **200Hz**, although it is noted that around **64Hz** the magnitude is high for both the note **A3** and the note **A4**. There is a defined attack, with a less intense but prolonged sustain, which slowly decreases in intensity until it decays. From the spectrogram, it is noted that the sound seems as if it "*vibrates*," likely due to the oscillation of the strings. The harmonics are not very intense, remaining at a frequency below **5000Hz** with lines much thinner compared to the fundamental frequency.

#### Mandolin
In the mandolin's spectrogram, the fundamental frequency for the note **A3** is found around **220Hz**, while it is around **440Hz** for the note **A4**. The mandolin's harmonics are very numerous, I suppose due to the sound box, and in this case also have a "*vibrating*" effect, similar to the guitar. The increase in intensity in the attack is rapid, with a sustain that loses intensity very quickly until it decays. The harmonics, unlike the guitar, last over time even at the frequency peak of about **16000Hz**.

# Results


In the experiment, we noticed interesting differences and similarities in the spectrogram of the instruments.

Clarinets and trumpets, which are wind instruments, behaved differently regarding the start (attack) of the sound and the layout of their notes (harmonics). The clarinet has a softer beginning and a steady sound, with notes gradually changing from low to high. On the other hand, the trumpet starts more abruptly, and its notes reach much higher, which explains why it sounds louder.

For string instruments, the guitar and mandolin, both have a "vibrating" sound due to the strings. However, they differ in their sounds: the guitar has a clear start and a sound that continues for a while before slowly fading, while the mandolin starts quickly and stops just as fast, with many more note variations lasting until the end.

Overall, wind instruments start and end their sounds more controlled, while string instruments start quickly and end gradually. Each instrument has its unique way of making music, especially when the notes change. String instruments "vibrate" more, while wind instruments have a more regular progression of notes.

# Consideration

The implementation of this task has been a very rewarding and educational experience. It offered me the opportunity to learn how to interpret spectrograms, a tool that, until now, was unfamiliar to me. Through this process, I have been able to discover aspects of music that I had never considered before, deepening my understanding of the different sound characteristics of musical instruments.

The main challenge was identifying the most important parts of the spectrogram to analyze and understanding how specific features differed among various instruments. This required careful observation and analysis, in addition to the ability to distinguish between the various visual elements of the chart. Despite the initial difficulties, overcoming these challenges made the experience even more rewarding
