from pathlib import Path
from boxmot import BotSort, ByteTrack, OcSort
# https://github.com/mikel-brostrom/boxmot

def get_tracker(name, device, reid_weights=None):
    if name == 'botsort':
        return BotSort(
            reid_weights=Path(reid_weights),
            device=device,
            with_reid=True,
            half=True,
            track_buffer=120,
            match_thresh=0.9,
            new_track_thresh=0.95
        )
    elif name == 'bytetrack':
        return ByteTrack(track_thresh=0.5, match_thresh=0.8)
    elif name == 'ocsort':
        return OcSort(det_thresh=0.5, iou_threshold=0.5)
    else:
        raise ValueError(f"Unsupported tracker: {name}")
