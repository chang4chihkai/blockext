from blockext import *

class Tutorial:
    def __init__(self):
        self.light = False

    def get_xyz(self, c, j, b):
        import random
        return random.choice(["sunny", "cloudy", "windy"])

descriptor = Descriptor(
    name = "Tutorial Example",
    port = 5000,
    blocks = [
        Block('get_xyz', 'reporter', 'get %m.c position of %m.j on body %m.b'),
    ],
    menus = dict(
        j = ["Left Ankle", "Right Ankle", "Left Elbow", "Right Elbow", "Left Foot", "Right Foot", "Left Hand", "Right Hand", "Left Hand Tip", "Right Hand Tip", "Head", "Left Hip", "Right Hip", "Left Knee", "Right Knee", "Neck", "Left Shoulder", "Right Shoulder", "Spine Base", "Spine Middle", "Spine Shoulder", "Left Thumb", "Right Thumb", "Left Wrist", "Right Wrist"],
        b = ["Body 1", "Body 2", "Body 3", "Body 4", "Body 5", "Body 6"],
        h = ["Unknown", "Not Tracked", "Open", "Closed", "Lasso"],
        c = ["x", "y", "z"],
        d = ["Left", "Right"],
    ),
)

extension = Extension(Tutorial, descriptor)

if __name__ == '__main__':
    extension.run_forever(debug=True)
