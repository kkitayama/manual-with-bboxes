import streamlit as st
import os
from PIL import Image

# 閾値ごとのディレクトリ名
thresholds = [50, 40, 30]
directories = [os.path.join("data", f"NA-FA8H2_with_bboxes_threshold_{threshold}") for threshold in thresholds]

# 各ディレクトリにある画像ファイルを取得
images_dict = {}
for directory in directories:
    image_files = sorted([f for f in os.listdir(directory) if f.endswith(".png")])
    images_dict[directory] = [os.path.join(directory, img) for img in image_files]

# 最初のディレクトリの画像ファイル数を取得
num_images = len(images_dict[directories[0]])

# streamlit で画像を表示
st.title("Threshold Comparison")
for i in range(num_images):
    cols = st.columns(len(directories))
    for col, directory in zip(cols, directories):
        image_path = images_dict[directory][i]
        col.image(Image.open(image_path), caption=f"{directory} - page_{i + 1}.png")