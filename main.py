from arguments import get_args
from face_tracking.face_tracking import run_tracking

def main():
    opt = get_args()
    run_tracking(opt)
    
if __name__ == '__main__':
    main()