#!/usr/bin/env python
import argparse
import whisper


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model', type=str, default='small')
    parser.add_argument('--input_file', type=str, default='input.mp3')
    parser.add_argument('--output_file', type=str, default='output.txt')
    parser.add_argument('--language', type=str, default='ja')
    parser.add_argument('--initial_prompt', type=str, default='ExcelのVLOOKUP関数や、SQLの副問い合わせは、慣れるまで難しいですね。')

    args = parser.parse_args()

    return args


def main():
    args = get_args()

    model_name = args.model
    input_file = args.input_file
    output_file = args.output_file
    language = args.language
    initial_prompt = args.initial_prompt 

    whisper_model = whisper.load_model(model_name, download_root='./')

    result = whisper_model.transcribe(input_file, verbose=True, language=language, initial_prompt=initial_prompt)

    with open(output_file, mode='w') as f:
        f.write(result['text'])

if __name__ == "__main__":
    main()
