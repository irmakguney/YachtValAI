import cv2
import os

def analyze_images(image_folder):
    results = {}
    for img_file in os.listdir(image_folder):
        if img_file.endswith('.jpg') or img_file.endswith('.png'):
            img_path = os.path.join(image_folder, img_file)
            img = cv2.imread(img_path)
            # rnek: Resim boyutunu al
            h, w, _ = img.shape
            results[img_file] = {'height': h, 'width': w}
    return results

if __name__ == "__main__":
    folder = '../data/images'
    res = analyze_images(folder)
    print(res)

