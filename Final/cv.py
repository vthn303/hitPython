import numpy as np
import cv2

# Tạo nền đen kích thước 430x350, 3 là màu chủ đạo, uint8 là unsigned integer 8 bit
# np.zeros: làm cho hình nền đen , 0: đen, 1: trắng
img = np.zeros((430, 350, 3), dtype=np.uint8)

# Định nghĩa cho tâm và bán kính
center_coordinates = (175, 215)
radius = 150
thickness = 2
# màu theo bgr ( mã của rgb )
color = (240, 108, 37)

# vẽ hình tròn với các thông số (hình cần vẽ lên, vtri tâm, độ dài bán kính, màu sắc htron, độ dày của htron)
img = cv2.circle(img, center_coordinates, radius, color, 2)

# chèn chữ vào hình
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "HIT", (75, 250), font, 4, color, 10, cv2.LINE_AA)  # cv2.LINE_AA: khử răng cưa, giúp hình mượt hơn
img = cv2.putText(img, "CLB TIN HOC DH CNHN", (85, 280), font, 0.5, color, 2, cv2.LINE_AA)
# vẽ con chuột
axes_length = (15, 10)  # Độ dài trục chính và trục phụ
angle = 180  # Góc xoay elip
img = cv2.ellipse(img, (175, 130), axes_length, angle, 0, 360, color, thickness)

img = cv2.line(img, (175, 120), (175, 140), color, thickness)
img = cv2.line(img, (175, 130), (200, 130), color, thickness)
img = cv2.ellipse(img, (210, 130), (10, 15), angle, 0, 45, color, thickness)

# làm mờ ảnh bằng filter2d
# kernel = np.ones((5, 5), np.float32) / 25
# blur_img = cv2.filter2D(img, -1, kernel)

# Làm mịn ảnh bằng Median Blur
# ksize = 5  # Kích thước của kernel, phải là số lẻ và không âm
# blur_img = cv2.medianBlur(img, ksize)

# chuyển màu từ bgr sang rgb
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Logo",img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
