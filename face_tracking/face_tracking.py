import cv2
import numpy as np
import torch
from pathlib import Path
from facenet_pytorch import MTCNN

from face_tracking.gallery_drawer import draw_face_gallery
from face_tracking.select_tracker import get_tracker

def run_tracking(opt):
    face_gallery = dict()
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    detector = MTCNN(keep_all=True, device=device).eval().to(device)
    tracker = get_tracker(opt.tracker, str(device), opt.reid_weights)

    vid = cv2.VideoCapture(opt.video_path)
    fps = vid.get(cv2.CAP_PROP_FPS)
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(opt.output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width + 120, height))

    while True:
        ret, frame = vid.read()
        if not ret:
            break

        boxes, confidences = detector.detect(frame)
        dets = []
        if boxes is not None:
            for (x1, y1, x2, y2), conf in zip(boxes, confidences):
                if conf < opt.conf_thresh:
                    continue
                w, h = x2 - x1, y2 - y1
                x1 = max(0, x1 - w * 0.2)
                y1 = max(0, y1 - h * 0.2)
                x2 = min(frame.shape[1], x2 + w * 0.2)
                y2 = min(frame.shape[0], y2 + h * 0.2)
                dets.append([x1, y1, x2, y2, conf, 0])
        dets = np.array(dets)

        track_results = tracker.update(dets, frame)
        for res in track_results:
            x1, y1, x2, y2, track_id = map(int, res[:5])
            face_crop = frame[y1:y2, x1:x2].copy()
            if face_crop.size == 0:
                continue
            face_crop = cv2.resize(face_crop, (100, 100))
            face_gallery[track_id] = face_crop

        tracker.plot_results(frame, show_trajectories=True)
        final_frame = draw_face_gallery(frame, face_gallery, max_faces=opt.max_faces)
        out.write(final_frame)
        cv2.imshow('result', final_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    out.release()
    cv2.destroyAllWindows()