from PIL import Image
from PIL.ExifTags import TAGS
from fractions import Fraction
class ReadMeatData():
    def read_exif_data(self, image_path):
        try:
            img = Image.open(image_path)
            ret_list = []
            pic_param = ''
            exif_data = img._getexif()
            if exif_data is not None:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    pic_info_list = ['Model', 'DateTime', 'ISOSpeedRatings', 'LensModel', 'ExposureTime', 'FocalLength', 'ApertureValue']
                    if tag_name in pic_info_list:
                        if tag_name == 'FocalLength':
                            focal_length_str = f"{round(value)}mm"
                            pic_param += focal_length_str
                            pic_param += ' '
                        elif tag_name == 'ExposureTime':
                            exposure_time = Fraction(value).limit_denominator()
                            pic_param += str(exposure_time)
                            pic_param += ' '
                        elif tag_name == 'ApertureValue':
                            av_str = f"F{round(value)}"
                            pic_param += av_str
                            pic_param += ' '
                        elif tag_name == 'ISOSpeedRatings':
                            iso_str = f"ISO{value}"
                            pic_param += iso_str
                            pic_param += ' '
                        else:
                            ret_list.append((tag_name, value))
                ret_list.append(('pic_param', pic_param))
            else:
                print("error")
            return ret_list
        except Exception as e:
            print("error")
        finally:
            img.close()
