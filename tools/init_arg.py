
import argparse

def args():
    sp = 0
    parser = argparse.ArgumentParser(description='tracking')
    parser.add_argument('--video_name0', default='F:/video/video-0-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name1', default='F:/video/video-1-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name2', default='F:/video/video-2-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name3', default='F:/video/video-3-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name4', default='F:/video/video-4-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name5', default='F:/video/video-5-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name6', default='F:/video/video-6-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name7', default='F:/video/video-7-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name8', default='F:/video/video-8-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name9', default='F:/video/video-9-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name10', default='F:/video/video-10-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name11', default='F:/video/video-11-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name12', default='F:/video/video-12-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name13', default='F:/video/video-13-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name14', default='F:/video/video-14-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name15', default='F:/video/video-15-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name16', default='F:/video/video-16-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name17', default='F:/video/video-17-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name18', default='F:/video/video-18-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name19', default='F:/video/video-19-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name20', default='F:/video/video-20-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name21', default='F:/video/video-21-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name22', default='F:/video/video-22-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name23', default='F:/video/video-23-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name24', default='F:/video/video-24-' + str(sp) + '.avi', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name25', default='F:/video/video-25-' + str(sp) + '.avi', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name26', default='F:/video/video-26-' + str(sp) + '.avi', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name27', default='F:/video/video-27-' + str(sp) + '.avi', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name28', default='F:/video/video-28-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name29', default='F:/video/video-29-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name30', default='F:/video/video-30-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name31', default='F:/video/video-31-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name32', default='F:/video/video-32-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')
    parser.add_argument('--video_name33', default='F:/video/video-33-' + str(sp) + '.mp4', type=str,
                        help='videos or image files')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args1 = args()
    print(args1)
    print(args1.video_name0)