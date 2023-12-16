"""Anomalib OpenVINO Inferencer Script.

This script performs OpenVINO inference by reading a model from
file system, and show the visualization results.
"""

# Copyright (C) 2022 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import warnings
from argparse import ArgumentParser, Namespace
from pathlib import Path
import os
import cv2

from anomalib.data.utils import generate_output_image_filename, get_image_filenames, read_image
from anomalib.deploy import OpenVINOInferencer
from anomalib.post_processing import Visualizer

from gpiozero import AngularServo
from time import sleep

servo =AngularServo(12, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025)

center = 50 # center
servo.angle = center

cam = cv2.VideoCapture(0)
focus = 150  # min: 0, max: 255, increment:5
cam.set(cv2.CAP_PROP_FOCUS, focus) 
result, image = cam.read() 
cv2.imwrite("ScrewsClassifier/input.png", image) 

def approve():
    for x in range(5,50):
        servo.angle = 50 - x
        sleep(0.003)
    sleep(1)
    for x in range(5,55):
        servo.angle = x
        sleep(0.05)
       
def trash():
    for x in range(55,100):
        servo.angle = x
        sleep(0.003)
    sleep(1)
    for x in range(55,100):
        servo.angle = 145 - x
        sleep(0.05) 
        
def get_parser() -> ArgumentParser:
    """Get parser.

    Returns:
        ArgumentParser: The parser object.
    """
    parser = ArgumentParser()
    parser.add_argument("--weights", type=Path, required=True, help="Path to model weights")
    parser.add_argument("--metadata", type=Path, required=True, help="Path to a JSON file containing the metadata.")
    parser.add_argument("--input", type=Path, required=True, help="Path to an image to infer.")
    parser.add_argument("--output", type=Path, required=False, help="Path to save the output image.")
    parser.add_argument(
        "--task",
        type=str,
        required=False,
        help="Task type.",
        default="classification",
        choices=["classification", "detection", "segmentation"],
    )
    parser.add_argument(
        "--device",
        type=str,
        required=False,
        help="Hardware device on which the model will be deployed",
        default="CPU",
        choices=["CPU", "GPU", "VPU"],
    )
    parser.add_argument(
        "--visualization_mode",
        type=str,
        required=False,
        default="simple",
        help="Visualization mode.",
        choices=["full", "simple"],
    )
    parser.add_argument(
        "--show",
        action="store_true",
        required=False,
        help="Show the visualized predictions on the screen.",
    )

    return parser


def infer(args: Namespace) -> None:
    """Infer predictions.

    Show/save the output if path is to an image. If the path is a directory, go over each image in the directory.

    Args:
        args (Namespace): The arguments from the command line.
    """
    # Get the inferencer.
    inferencer = OpenVINOInferencer(path=args.weights, metadata=args.metadata, device=args.device)
    visualizer = Visualizer(mode=args.visualization_mode, task=args.task)

    filenames = get_image_filenames(path=args.input)
    for filename in filenames:
        image = read_image(filename)
        predictions = inferencer.predict(image=image)
        output = visualizer.visualize_image(predictions)
        
        if(predictions.pred_score < 0.50): approve()
        else: trash()

        if args.output is None and args.show is False:
            warnings.warn(
                "Neither output path is provided nor show flag is set. Inferencer will run but return nothing."
            )

        if args.output:
            file_path = generate_output_image_filename(input_path=filename, output_path=args.output)
            visualizer.save(file_path=file_path, image=output)

        # Show the image in case the flag is set by the user.
        if args.show:
            os.system('sudo fbi -a /dev/fb0 --noverbose -T 2 test_result/ScrewsClassifier/input.png')
            sleep(10)
            os.system('rm test_result/ScrewsClassifier/*')
            


if __name__ == "__main__":
    args = get_parser().parse_args()
    infer(args)
