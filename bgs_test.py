import cv2


def main():
    video = cv2.VideoCapture(0)
    bgs = cv2.createBackgroundSubtractorMOG2()

    try:
        while True:
            ret, frame = video.read()
            if ret is None:
                break

            fg_mask = bgs.apply(frame)
            _, th_fg_mask = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)

            cv2.imshow('Lepton Radiometry', frame)
            cv2.imshow('FG Mask', fg_mask)
            cv2.imshow('FG Mask (applied threshold)', th_fg_mask)
            cv2.waitKey(1)
    except KeyboardInterrupt:
        print()
    finally:
        cv2.destroyAllWindows()
        video.release()

    print("done")


if __name__ == '__main__':
    main()
