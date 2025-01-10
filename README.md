# YouTube Video Downloader

The **YouTube Video Downloader** is a Python-based GUI application designed for downloading YouTube videos easily and quickly. With just a YouTube URL, users can download videos in a straightforward and user-friendly interface.

---

## Features
- Simple GUI built with Tkinter.
- Supports downloading videos in MP4 format using `yt-dlp`.
- Displays clear success or error messages for the user.
- Allows users to specify a download location.

---

## Prerequisites
Ensure you have the following installed:
- **Python 3.8 or higher**

Install the required dependencies with:
```bash
pip install -r requirements.txt
```
## Installation

Clone this repository:
   ```bash
   git clone https://github.com/your-username/YouTube-Video-Downloader.git
   cd YouTube-Video-Downloader
   ```


## Running the Application
Run the application with:

```bash
python app.py
```
This will open a GUI window where you can paste the YouTube video URL and start downloading.

## Running with Docker
Alternatively, you can use Docker to run the application:

1. Build the Docker image:
```bash
docker build -t youtube-downloader .
```
2. Run the Docker container:
```bash
docker run -it youtube-downloader
```

## Project Structure
```bash
.
├── YT_Video_Downloader.py.py                # Main Python script to run the application
├── requirements.txt                         # Dependencies required for the project
├── Dockerfile                               # Dockerfile for containerizing the application
├── README.md                                # Documentation file
```

## Screenshots
Adding screenshots of the GUI here to demonstrate the application's functionality. 


## Technologies Used
+ Python 3: Programming language for the application.
+ Tkinter: Standard GUI library for creating the application interface.
+ yt-dlp: Advanced library for downloading YouTube videos.

## Contributing
Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b 'feature-name'
```
3. Commit your changes:
```bash
git commit -m 'Add some feature'
```
4. Push to the branch:
```bash
git push origin 'feature-name'
```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Support
If you encounter any issues or have questions, please open an issue on GitHub or contact me directly.