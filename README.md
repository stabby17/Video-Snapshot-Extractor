# Video Snapshot Extractor

A fast and efficient Python tool for extracting frames from videos at specified time intervals. This tool is perfect for creating thumbnails, analyzing video content, or generating training data for machine learning models.

## Features

- Extract frames at precise time intervals
- Efficient frame processing without sleep delays
- Progress tracking with frame counts
- Organized output structure
- Support for any video format compatible with OpenCV

## Requirements

- Python 3.6+
- OpenCV (`cv2`)
- NumPy

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/video-snapshot-extractor.git
cd video-snapshot-extractor
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage with default settings (1-second intervals):
```bash
python snapshot_extractor.py --video_path path/to/your/video.mp4
```

Extract frames every 0.5 seconds:
```bash
python snapshot_extractor.py --video_path path/to/your/video.mp4 --seconds_interval 0.5
```

### Arguments

- `--video_path`: Path to the input video file (required)
- `--seconds_interval`: Time interval between snapshots in seconds (default: 1.0)

## Output

The script creates a `snapshots` directory containing subdirectories for each processed video. Frames are saved as JPEG files with names formatted as `frame_XXXXX.jpg`.

Example output structure:
```
snapshots/
└── video_name/
    ├── frame_00000.jpg
    ├── frame_00001.jpg
    ├── frame_00002.jpg
    └── ...
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV community for their excellent video processing library
- All contributors who help improve this tool
