import time
from rgbmatrix.graphics import DrawText
from renderer.renderer import Renderer
from utils import align_text_center, load_font, load_image
from constants import ERROR_IMAGE, ROTATION_RATE
from data.color import Color


class ErrorRenderer(Renderer):
    """
    Renderer for error messages

    Arguments:
        data (api.Data):        Data instance

    Attributes:
        error_msg (str):        Error message string
    """

    def __init__(self, matrix, canvas, config, data):
        super().__init__(matrix, canvas, config)

        self.error_msg = data.status

    def render(self):
        self.canvas.Clear()

        self.render_error_msg()
        time.sleep(ROTATION_RATE)

        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def render_error_msg(self):
        x, y = align_text_center(self.error_msg,
                                 self.canvas.width,
                                 self.canvas.height,
                                 self.secondary_font.baseline - 1,
                                 self.secondary_font.height)
        DrawText(self.canvas, self.secondary_font, x, y, Color.RED, self.error_msg)

    def render_image(self):
        img = load_image(ERROR_IMAGE, (4, 6))
        x_offset, y_offset = 0, 0
        self.canvas.SetImage(img, x_offset, y_offset)
