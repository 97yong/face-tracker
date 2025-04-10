import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Face Tracking with BoxMot + MTCNN")

    parser.add_argument('--video_path', type=str, default='./data/MOT16-08-raw.webm',
                        help='Path to input video')
    parser.add_argument('--output_path', type=str, default='output_custom_draw.mp4',
                        help='Path to save output video')
    parser.add_argument('--reid_weights', type=str, default='mobilenetv2_x1_4_market1501.pt',
                        help='Path to re-ID model weights')
    parser.add_argument('--conf_thresh', type=float, default=0.5,
                        help='Minimum confidence for face detection')
    parser.add_argument('--max_faces', type=int, default=8,
                        help='Maximum number of face thumbnails to display')
    
    parser.add_argument('--tracker', type=str, default='botsort', choices=['botsort', 'bytetrack', 'ocsort'],
                        help='Select tracker model (supported by boxmot): botsort | bytetrack | ocsort')
    # https://github.com/mikel-brostrom/boxmot

    return parser.parse_args()
