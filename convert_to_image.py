import cv2
import os
import concurrent.futures


# Video framelerine ayırma fonksiyonu
def process_video(video_info):
    video_path, output_folder, file_suffix = video_info

    # 'images' klasörü yoksa oluştur ve videoyu framelerine ayır
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_filename = os.path.join(
            output_folder, f"frame_{frame_count:04d}_{file_suffix}.jpg"
        )
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()
    print(f"Toplam {frame_count} kare '{output_folder}' klasörüne kaydedildi.")


# Tüm alt klasörlerdeki videoları toplama ve işleme fonksiyonu
def process_videos_in_subfolders(parent_folder):
    video_infos = []
    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            if file == "video.mp4":
                video_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, parent_folder)
                folder_parts = relative_path.split(os.sep)
                file_suffix = "_".join(folder_parts)
                output_folder = os.path.join(root, "images")

                # 'images' klasörü varsa videoyu işlemeye gerek yok
                if os.path.exists(output_folder):
                    print(f"'{output_folder}' zaten mevcut, video atlandı.")
                    continue

                # İşlenecek video bilgilerini listeye ekle
                video_infos.append((video_path, output_folder, file_suffix))

    # Videoları paralel olarak işle
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_video, video_infos)


# Ana klasör yolunu belirtin
parent_folder = "C:\\Users\\albur\\Desktop\\Datasets\\stanford\\video"

# Videoları işleyin
process_videos_in_subfolders(parent_folder)
