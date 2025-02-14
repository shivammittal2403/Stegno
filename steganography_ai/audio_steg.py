from pydub import AudioSegment

class AudioSteg:
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.audio = AudioSegment.from_file(audio_path)

    def embed_message(self, message):
        binary_message = ''.join(format(ord(i), '08b') for i in message)
        data_index = 0

        # Modify the least significant bit of the audio samples
        samples = self.audio.get_array_of_samples()
        for i in range(len(samples)):
            if data_index < len(binary_message):
                sample = samples[i]
                samples[i] = (sample & ~1) | int(binary_message[data_index])
                data_index += 1

        # Save the modified audio
        self.audio._data = samples.tobytes()
        self.audio.export('output_' + self.audio_path, format="wav")

    def extract_message(self):
        binary_message = ''
        samples = self.audio.get_array_of_samples()
        for sample in samples:
            binary_message += str(sample & 1)

        message = ''.join(chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8))
        return message.split('\x00', 1)[0]  # Return message until null character
