# import cv2
# import numpy
#
# # cap = cv2.VideoCapture(1)   # 调整参数实现读取视频或调用摄像头
# # while 1:
# #     ret, frame = cap.read()
# #     # cv2.imshow("cap", frame)
# #     # if cv2.waitKey(100) & 0xff == ord('q'):
# #     #     break
# #
# # cap.release()
# # cv2.destroyAllWindows()
#
# cap = cv2.VideoCapture('C:/Users/sunxingba/Desktop/picture/feidaou.mp4')
#
# while 1:
#     ret, frame = cap.read()
#     cv2.imshow("capture", frame)  # 显示
#     if cv2.waitKey(100) & 0xff == ord('q'):  # 按q退出
#         break
#     # cv2.imwrite("example.png", frame)  # 将拍摄内容保存为png图片
# cap.release()   # 关闭调用的摄像头
