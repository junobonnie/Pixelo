# PIXELO


설명: knn based img2pixel program

사용한 라이브러리: opencv & pyqt 사용

라이센스: GNU GPL LISENCE

v0.2 변경사항: 이미지 가로 최대 사이즈를 512pixel로 제한함으로써 큰 이미지에서 img2pixel 변환속도 증가.
               실행 파일 크기를 344MB에서 65MB로 줄임.

v0.2 Download Link: https://github.com/junobonnie/Pixelo/releases/download/image/PIXELO.zip

v0.1 Download Link: https://drive.google.com/file/d/1SC2q-t61r7lgrS6PzvWnYrcKHcFRTqF4/view?usp=sharing


사용예시:
![Animation4](https://user-images.githubusercontent.com/60418809/133888856-0dcbb1a0-d003-4680-b440-4b9338b66d0a.gif)
</br>
</br>
</br>
![Animation4](https://user-images.githubusercontent.com/60418809/133888864-77a1c324-0e2f-45f5-9f52-bd0ea1fe02d7.gif)
</br>
</br>
</br>
![image](https://user-images.githubusercontent.com/60418809/133888661-d4bda5e6-cc8d-4663-b5b0-e1d18836b363.png)

v0.1 여담: pyinstaller에서 matplotlib를 사용한 코드를 빌드하려고 하니 오류가 났다. 알고보니 파이썬에 설치되어있는 pathlib이란 녀석을 삭제해주면 문제가 없더라. 뭔가 충수꼬리같은 라이브러리 같다.

v0.2 여담: numpy가 conda install 되었을 경우 별에 별 종속성 파일들을 다운로드하기 때문에 pyinstaller로 변환시 그만큼 dll파일이 늘어나서 용량이 커진다고 한다. 그래서 pyqt라는 이름의 새로운 가상환경을 만들고 numpy 및 다른 라이브러리들을 pip install 하고 exe 파일로 변환하니 280MB정도의 용량을 줄일 수 있었다. (변환시  upx라는 dll 압축 프로그램도 같이 사용했다.)
