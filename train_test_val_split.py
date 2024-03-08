import os
import random
root_dir="C:\\Users\\rudra\\Downloads\\Object_Detection_other_method"
images = []
for filename in os.listdir(root_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        images.append(filename)

random.shuffle(images)
num_train_images = int(len(images) * 0.8)
num_test_images = int(len(images) * 0.1)
num_val_images = len(images) - num_train_images - num_test_images

train_images = []
test_images = []
val_images = []

for i in range(num_train_images):
    train_images.append(images[i])

for i in range(num_test_images):
    test_images.append(images[i + num_train_images])

for i in range(num_val_images):
    val_images.append(images[i + num_train_images + num_test_images])

for image in train_images:
    os.rename(
        os.path.join(root_dir, image), os.path.join(root_dir, "train", "image", image)
    )

for image in test_images:
    os.rename(
        os.path.join(root_dir, image), os.path.join(root_dir, "test", "image", image)
    )

for image in val_images:
    os.rename(
        os.path.join(root_dir, image), os.path.join(root_dir, "val", "image", image)
    )