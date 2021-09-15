import tensorflow.lite as lite
import argparse

def parse_args():

    parser = argparse.ArgumentParser(description='Keras to TensorFlow Lite converter')

    parser.add_argument('--input_keras',
                        required=False,
                        type=str,
                        default='facenet_weights.h5',
                        help='The input Keras file model (.h5)')

    parser.add_argument('--output_tflite',
                        required=False,
                        type=str,
                        default='tflite.tflite',
                        help='The output TensorFlow Lite file model (.tflite)')

    parser.add_argument('--post_quantize',
                        required=False,
                        type=bool,
                        help='Use post-quantization')

    args = parser.parse_args()
    return args

def convert(args):

    input_file = './model'
    output_file = 'tflite.tflite'

    # Converts the Keras model to TensorFlow Lite
    converter = lite.TocoConverter.from_keras_model_file(input_file)
    converter.post_training_quantize = True
    tflite_model = converter.convert()
    open(output_file, "wb").write(tflite_model)


def run():
    args = parse_args()
    convert(args)

if __name__ == "__main__":
    run()