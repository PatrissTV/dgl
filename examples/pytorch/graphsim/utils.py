import os

import cv2 as cv
import matplotlib
import matplotlib.animation as manimation
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("agg")

# Make video can be used to visualize test data


def make_video(xy, filename):
    FFMpegWriter = manimation.writers["ffmpeg"]
    metadata = dict(
        title="Movie Test", artist="Matplotlib", comment="Movie support!"
    )
    writer = FFMpegWriter(fps=15, metadata=metadata)
    fig = plt.figure()
    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    fig_num = len(xy)
    color = ["ro", "bo", "go", "ko", "yo", "mo", "co"]
    with writer.saving(fig, filename, len(xy)):
        for i in range(len(xy)):
            for j in range(len(xy[0])):
                plt.plot(xy[i, j, 1], xy[i, j, 0], color[j % len(color)])
            writer.grab_frame()
