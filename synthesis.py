import sys
sys.path.append('assem-vc/')
sys.path.append('assem-vc/hifi-gan/')

from wav2mel import wav2mel
from mel2wav import mel2wav

def main(src_audio_num=0, target_audio_path='example/p237_007-22k.wav'):
    save_path = 'output%s.wav' % src_audio_num
    mel = wav2mel(target_audio_path)
    audio = mel2wav(src_audio_num, mel, save_path)
    print(f'saved {save_path}')


if __name__ == '__main__':
    for i in range(3):
        main(src_audio_num=i)