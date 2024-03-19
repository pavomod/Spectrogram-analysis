def plot_spectrogram(file_path, instrument_name):
    y, sr = librosa.load(file_path, sr=None) # y contiene l'audio come una serie di campioni mentre sr contiene il sample rate
    D = np.abs(librosa.stft(y)) # calcola Short-time Fourier transform, utilizzo np.abs per ottenere la magnitudine della trasformazione, ignorando la fase
    DB = librosa.amplitude_to_db(D, ref=np.max) # converto le ampiezze ottenute dalla STFT in decibel impostando il punto di riferimento per la conversione in dB sul valore massimo delle ampiezze
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(DB, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Spectrogram of {instrument_name}')
    plt.tight_layout()
    plt.show()


path_clarinet1='samples/clarinet/clarinet_A3_025_forte_normal.mp3'
path_clarinet2='samples/clarinet/clarinet_A4_025_forte_normal.mp3'
path_trumpet1='samples/trumpet/trumpet_A3_025_forte_normal.mp3'
path_trumpet2='samples/trumpet/trumpet_A4_025_forte_normal.mp3'
path_guitar1='samples/guitar/guitar_A3_very-long_forte_harmonics.mp3'
path_guitar2='samples/guitar/guitar_A4_very-long_forte_harmonics.mp3'
path_mandolin1='samples/mandolin/mandolin_A3_very-long_forte_tremolo.mp3'
path_mandolin2='samples/mandolin/mandolin_A4_very-long_forte_tremolo.mp3'

plot_spectrogram(path_clarinet1,'Clarinet A3')
plot_spectrogram(path_clarinet2,'Clarinet A4')
plot_spectrogram(path_trumpet1,'Trumpet A3')
plot_spectrogram(path_trumpet2,'Trumpet A4')
plot_spectrogram(path_guitar1,'Guitar A3')
plot_spectrogram(path_guitar2,'Guitar A4')
plot_spectrogram(path_mandolin1,'Mandolin A3')
plot_spectrogram(path_mandolin2,'Mandolin A4')