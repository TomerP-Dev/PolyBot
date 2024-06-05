import random
from pathlib import Path
from matplotlib.image import imread, imsave


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


class Img:
    BASE_DIR = Path(r"C:\Users\tomer\Downloads\Python Project")

    def __init__(self, path):
        """
        Do not change the constructor implementation
        """
        self.path = Path(path)
        self.data = None  # Initialize data to None
        image_data = imread(path)
        if image_data is not None:
            self.data = rgb2gray(image_data).tolist()
        else:
            print("Failed to load image")

    def save_img(self, suffix="Grayscale"):
        """
        Do not change the below implementation
        """
        if self.data is None:
            print("No image data to save")
            return None
        new_path = self.BASE_DIR / self.path.with_name(f'Processed_{suffix}' + self.path.suffix).name
        imsave(new_path, self.data, cmap='gray')
        return new_path

    def blur(self, blur_level=16):
        if self.data is None:
            print("No image data to blur")
            return

        height = len(self.data)
        width = len(self.data[0])
        filter_sum = blur_level ** 2

        result = []
        for i in range(height - blur_level + 1):
            row_result = []
            for j in range(width - blur_level + 1):
                sub_matrix = [row[j:j + blur_level] for row in self.data[i:i + blur_level]]
                average = sum(sum(sub_row) for sub_row in sub_matrix) // filter_sum
                row_result.append(average)
            result.append(row_result)

        self.data = result

    def contour(self):
        if self.data is None:
            print("No image data to apply contour")
            return

        for i, row in enumerate(self.data):
            res = []
            for j in range(1, len(row)):
                res.append(abs(row[j - 1] - row[j]))
            self.data[i] = res

    def rotate(self):
        if self.data is None:
            print("No image data to rotate")
            return

        transposed_data = [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
        rotated_data = [row[::-1] for row in transposed_data]
        self.data = rotated_data

    def salt_n_pepper(self):
        if self.data is None:
            print("No image data to apply salt and pepper noise")
            return

        height, width = len(self.data), len(self.data[0])

        for y in range(height):
            for x in range(width):
                random_value = random.random()
                if random_value < 0.2:
                    self.data[y][x] = 255  # Salt
                elif random_value > 0.8:
                    self.data[y][x] = 0  # Pepper
                # Otherwise, keep the original pixel value

    def concat(self, other_img, direction='horizontal'):
        # Implementation here
        pass

    def segment(self):
        # Implementation here
        pass
