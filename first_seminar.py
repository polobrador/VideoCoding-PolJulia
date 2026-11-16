class ColorTranslator:
    @staticmethod
    def rgb_to_yuv(rgb_color):
        r = rgb_color[0]
        g = rgb_color[1]
        b = rgb_color[2]

        Y = 0.257*r + 0.504*g + 0.098*b + 16
        Cb = -0.148 * r - 0.291 * g + 0.439 * b + 128
        Cr = 0.439 * r - 0.368 * g - 0.071 * b + 128

        return (Y, Cb, Cr)

    @staticmethod
    def yuv_to_rgb(yuv_color):
        y = yuv_color[0]
        u = yuv_color[1]
        v = yuv_color[2]

        b = 1.164 * (y - 16) + 2.018 * (u - 128)
        g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
        r = 1.164 * (y - 16) + 1.596 * (v - 128)
        return (r,g,b)


ct = ColorTranslator
rgb = (222, 100, 32)
yuv = ct.rgb_to_yuv(rgb)
rgb2 = ct.yuv_to_rgb(yuv)
print("Initial rgb color: ", rgb)
print("Obtained yuv color: ", yuv)
print("Obteined rgb color: ", rgb2)
