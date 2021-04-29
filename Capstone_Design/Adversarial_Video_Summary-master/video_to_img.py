import cv2, os
from pathlib import Path

root = 'C:/Users/01079/video_summarization_data/only_video02'

root_dir = Path(root)

sub_dirs = [sub_dir for sub_dir in root_dir.iterdir() if sub_dir.is_dir]
file_count = 0
for sub_dir in sub_dirs:
    videos = [video for video in sub_dir.iterdir() if not video.is_dir()]
    for video in videos:
        cap = cv2.VideoCapture(str(video))
        count = 0
        (sub_dir / Path(video.stem)).mkdir(exist_ok=True)
        print("폴더 생성 완료", (sub_dir / Path(video.stem)))

        while True:
            success, image = cap.read()
            created_file = sub_dir / video.stem / Path(video.stem + '_' + str(count).zfill(6) + '.jpg')

            if os.path.isfile(created_file):
                break

            if success:
                cv2.imwrite(str(created_file), image)
                print(f"처리한 파일 수:{file_count}", sub_dir / video.stem / Path(str(count).zfill(6) + '.jpg'))
                count += 1
            else:
                print("오류남!", created_file)
                break
        file_count += 1
        cap.release()

        # while cap.isOpened():
        #     success, image = cap.read()
        #     created_file = sub_dir / video.stem / Path(video.stem + '_' + str(count).zfill(6) + '.jpg')
        #     if image is not None:
        #         cv2.imwrite(str(created_file), image)
        #         print(f"처리한 파일 수:{file_count}", sub_dir / video.stem / Path(str(count).zfill(6) + '.jpg'))
        #         count += 1
        #     else:
        #         cap.release()




