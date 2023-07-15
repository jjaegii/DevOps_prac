import unittest
import detect

class DetectTests(unittest.TestCase):
    
    def test_load_model(self):
        try:
            detect.load_model()
        except:
            self.assertFalse()

    def test_detect(self):
        model = detect.load_model()
        f_path = "test_img.jpg"
        self.assertNotEqual(detect.run_model(f_path, model), (-1, -1))


