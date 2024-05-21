from gtts import gTTS
from pydub import AudioSegment
import simpleaudio as sa

def speak(text):
    # 텍스트를 음성으로 변환
    tts = gTTS(text=text, lang='ko')
    # 음성 파일 저장
    tts.save("output.mp3")

    # MP3 파일을 로드하고 WAV로 변환
    audio = AudioSegment.from_mp3("output.mp3")
    audio.export("output.wav", format="wav")

    # WAV 파일 재생
    wave_obj = sa.WaveObject.from_wave_file("output.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()  # 재생이 끝날 때까지 대기

    # 임시 파일 삭제
    import os
    os.remove("output.mp3")
    os.remove("output.wav")

if __name__ == "__main__":
    text_to_speak = "킥보드에서 하차하세요."
    speak(text_to_speak)
