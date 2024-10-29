import cv2
import os
import argparse

def extract_frames(video_path, frame_interval=30):
    """
    Extract frames from a video at specified frame intervals.
    
    Args:
        video_path (str): Path to the video file
        frame_interval (int): Number of frames to skip between snapshots
    """
    # Extract the video filename without extension
    video_filename = os.path.splitext(os.path.basename(video_path))[0]
    
    # Create a folder for the video's snapshots
    snapshot_folder = os.path.join('snapshots', video_filename)
    os.makedirs(snapshot_folder, exist_ok=True)
    
    # Read the video
    video = cv2.VideoCapture(video_path)
    
    # Get video properties
    fps = int(video.get(cv2.CAP_PROP_FPS))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    try:
        frame_count = 0
        snapshot_count = 0
        
        while True:
            ret, frame = video.read()
            
            if not ret:
                break
                
            # Save frame at specified intervals
            if frame_count % frame_interval == 0:
                name = os.path.join(snapshot_folder, f'frame_{snapshot_count:05d}.jpg')
                print(f'Saving frame {frame_count}/{total_frames} as {name}')
                cv2.imwrite(name, frame)
                snapshot_count += 1
                
            frame_count += 1
            
    finally:
        video.release()
        cv2.destroyAllWindows()
        
    return snapshot_count

def main():
    parser = argparse.ArgumentParser(description='Extract frames from a video at regular intervals.')
    parser.add_argument('--video_path', type=str, required=True, help='Path to the video file')
    parser.add_argument('--seconds_interval', type=float, default=1.0, 
                        help='Time interval between snapshots in seconds')
    
    args = parser.parse_args()
    
    # Open video to get FPS
    video = cv2.VideoCapture(args.video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    video.release()
    
    # Convert time interval to frame interval
    frame_interval = int(fps * args.seconds_interval)
    
    print(f"Video FPS: {fps}")
    print(f"Frame interval: {frame_interval} frames")
    
    # Extract frames
    num_snapshots = extract_frames(args.video_path, frame_interval)
    print(f"\nExtraction complete. Saved {num_snapshots} snapshots.")

if __name__ == "__main__":
    main()