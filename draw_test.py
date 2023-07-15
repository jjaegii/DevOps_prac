import unittest
import draw

class DrawTests(unittest.TestCase):
    
    maxDiff = None

    def test_frame1(self):
        frame = '''
                    ##         .
                ## ## ##        ==
            ## ## ## ## ##    ===
        /\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"___/ ===
    ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
        \______ o           __/
            \    \         __/
            \____\_______/
    '''
        self.assertEqual(draw.set_frames()[0], frame)
        
    
    def test_frame2(self):
        frame = '''
                    ##         .
                ## ## ##        ==
            ## ## ## ## ##    ===
        /\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"___/ ===
    ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ /  ===- ~~~
        \______ o           __/
            \    \         __/
            \____\_______/
    '''
        self.assertEqual(draw.set_frames()[1], frame)


