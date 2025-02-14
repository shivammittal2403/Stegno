import argparse
from steganography.image_steg import ImageSteg
from steganography.audio_steg import AudioSteg
from ai.data_analysis import analyze_data

def main():
    parser = argparse.ArgumentParser(description='Steganography with AI/ML capabilities.')
    parser.add_argument('mode', choices=['embed', 'extract', 'analyze'], help='Choose mode: embed, extract, or analyze.')
    parser.add_argument('--file', required=True, help='Input file (image/audio) for embedding or extraction.')
    parser.add_argument('--message', help='Message to embed (for embed mode).')
    
    args = parser.parse_args()

    if args.mode == 'embed' and args.message:
        if args.file.endswith('.png') or args.file.endswith('.jpg'):
            steg = ImageSteg(args.file)
            steg.embed_message(args.message)
            print("Message embedded in image.")
        elif args.file.endswith('.wav'):
            steg = AudioSteg(args.file)
            steg.embed_message(args.message)
            print("Message embedded in audio.")
        else:
            print("Unsupported file type for embedding.")
    
    elif args.mode == 'extract':
        if args.file.endswith('.png') or args.file.endswith('.jpg'):
            steg = ImageSteg(args.file)
            message = steg.extract_message()
            print(f"Extracted message: {message}")
        elif args.file.endswith('.wav'):
            steg = AudioSteg(args.file)
            message = steg.extract_message()
            print(f"Extracted message: {message}")
        else:
            print("Unsupported file type for extraction.")
    
    elif args.mode == 'analyze':
        analyze_data(args.file)

if __name__ == "__main__":
    main()
