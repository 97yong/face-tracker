import cv2
import numpy as np

def draw_face_gallery(frame, face_gallery, max_faces=6):
    gallery_width = 120
    frame_h, frame_w = frame.shape[:2]
    extended_frame = np.zeros((frame_h, frame_w + gallery_width, 3), dtype=np.uint8)
    extended_frame[:, :frame_w] = frame

    y_offset = 10
    for i, (tid, face) in enumerate(sorted(face_gallery.items())[:max_faces]):
        thumb = cv2.resize(face, (100, 100))
        y = y_offset + i * 110
        if y + 100 > frame_h:
            break
        extended_frame[y:y+100, frame_w+10:frame_w+110] = thumb
        cv2.putText(extended_frame, f'ID {tid}', (frame_w+10, y+95), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    return extended_frame