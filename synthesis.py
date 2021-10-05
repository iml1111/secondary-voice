import sys
sys.path.append('assem-vc/')
sys.path.append('assem-vc/hifi-gan/')

from stt import stt
from wav2mel import wav2mel
from mel2wav import mel2wav

def synthesis(src_audio_num, target_audio_path, save_path):
    

    script = stt(src_audio_num)
    mel = wav2mel(target_audio_path)
    audio = mel2wav(src_audio_num, mel, save_path, script)
    print(f'saved {save_path}')


if __name__ == '__main__':
    synthesis('example/p286_010-22k.wav', 'example/a001.wav')