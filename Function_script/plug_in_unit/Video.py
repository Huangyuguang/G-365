class Video:
    def __init__(self):
        import cv2
        import numpy as np

        # 打开默认的摄像头
        cap = cv2.VideoCapture(0)

        while True:
            # 读取视频流中的一帧图像
            ret, frame = cap.read()

            # 对图像进行处理，例如缩放、转灰度等等
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            # 进行目标检测
            # <TODO>

            # 显示图像
            cv2.imshow('视频监控', frame)

            # 按下 'q' 键退出窗口
            if cv2.waitKey(1) & 0xff == ord('q'):
                break

        # 释放资源并关闭窗口
        cap.release()
        cv2.destroyAllWindows()


# V0.0.3
