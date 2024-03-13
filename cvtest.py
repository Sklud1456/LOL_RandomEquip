import cv2 as cv
import os
import sys
import numpy as np
def cv_read(file_path):
    cv_img = cv.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img


# 中文文件路径
path = "./EquipIco/黯影阔剑.png"

picture = cv_read(path)
# 显示图片
cv.imshow("Image", picture)

# 等待按下任意按键后关闭窗口
cv.waitKey(0)
cv.destroyAllWindows()