import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

class PutExif2Pic():
    def PutExif2Pic(self, list, image_path):
        old_image = cv2.imread(image_path)
        height, width = old_image.shape[:2]

        white_border_h = 0
        if height > width:
            white_border_h = height / 8
        else:
            white_border_h = height / 6
        image = self.AddWhiteBorder(old_image, round(white_border_h))

        font_path = "res/Trebuchet MS Italic.ttf"
        font_size = 120
        pil_font = ImageFont.truetype(font_path, font_size)
        pil_image = Image.fromarray(image)
        draw = ImageDraw.Draw(pil_image)

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 5
        font_thickness = 12
        text_color = (0, 0, 0)
        text_base_y = height + 150
        text_base_x = 120

        text_x = 0
        text_y = 0
        model_text_y = 0

        for tag, value in list:
            text = f"{value}"
            if tag == 'Model':
                text_x = text_base_x
                text_y = text_base_y
                model_text_y = text_y
            elif tag == 'DateTime':
                (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
                text_x = text_base_x
                text_y = model_text_y + baseline + 200
            elif tag == 'pic_param':
                (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
                text_x = width / 2 + 400
                text_y = text_base_y
            elif tag == 'LensModel':
                (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
                text_x = width / 2 + 400
                text_y = model_text_y + baseline + 200
            else:
                text_x = 100
                text_y = 100
            draw.text((text_x, text_y), text, font=pil_font, fill=text_color)
            # cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness, cv2.LINE_AA)
            opencv_img = numpy.array(pil_image)

        logo_in_pic_x = int(width / 5 * 2)
        loge_in_pic_y = int(height + 150)
        self.AddLogo2Pic(opencv_img, 'res/icon/icons8-nikon-500.png', logo_in_pic_x, loge_in_pic_y)
        cv2.imwrite("./res/output_pic.jpg", opencv_img)

    # 增加白色边框
    def AddWhiteBorder(self, image, border_size):
        height, width = image.shape[:2]

        bottom_border_h = border_size
        bottom_border_w = width

        white_border = numpy.full((bottom_border_h, bottom_border_w, 3), 255, dtype=numpy.uint8)
        result_image = numpy.vstack((image, white_border))

        return result_image

    # 将logo写到图片中
    def AddLogo2Pic(self, image, logo_path, logo_in_pic_x, logo_in_pic_y):
        logo_image = cv2.imread(logo_path)
        # image = cv2.imread(image_path)
        logo_h, logo_w = logo_image.shape[:2]
        roi = image[logo_in_pic_y:logo_in_pic_y + logo_h, logo_in_pic_x:logo_in_pic_x + logo_w]
        roi[:, :] = logo_image
