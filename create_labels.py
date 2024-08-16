import os
from PIL import Image


# Tüm alt klasörlerde annotations.txt ve reference.jpg dosyalarını bulup işleyecek fonksiyon
def process_annotations_in_subfolders(parent_folder):
    for root, dirs, files in os.walk(parent_folder):
        if "annotations.txt" in files and "reference.jpg" in files:
            # Dosya yolları
            input_file = os.path.join(root, "annotations.txt")
            reference_image = os.path.join(root, "reference.jpg")
            output_folder = os.path.join(root, "labels")

            # Alt klasörlerin adını al
            relative_path = os.path.relpath(root, parent_folder)
            folder_parts = relative_path.split(os.sep)
            file_suffix = "_".join(folder_parts)

            # reference.jpg boyutlarını al
            with Image.open(reference_image) as img:
                image_width, image_height = img.size

            # labels klasörünü oluştur
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Anotasyon dosyasını oku
            with open(input_file, "r") as file:
                lines = file.readlines()

            # Satırları frame numarasına göre grupla
            frames = {}
            for line in lines:
                parts = line.split()
                (
                    track_id,
                    xmin,
                    ymin,
                    xmax,
                    ymax,
                    frame,
                    lost,
                    occluded,
                    generated,
                    label,
                ) = parts

                # Etiketleri değiştir ve istenen formatta yeni satırı oluştur
                label = label.replace('"Pedestrian"', "1").replace('"Biker"', "1")

                # YOLOv5 formatında x_center, y_center, width, height hesaplama
                xmin = float(xmin)
                ymin = float(ymin)
                xmax = float(xmax)
                ymax = float(ymax)

                x_center = (xmin + xmax) / 2.0 / image_width
                y_center = (ymin + ymax) / 2.0 / image_height
                width = (xmax - xmin) / image_width
                height = (ymax - ymin) / image_height

                new_line = (
                    f"{label} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"
                )

                # Frame numarasıyla grupla
                if frame not in frames:
                    frames[frame] = []
                frames[frame].append(new_line)

            # Frame dosyalarını oluştur
            frame_index = 0
            for frame_number in sorted(frames.keys(), key=int):
                output_filename = os.path.join(
                    output_folder, f"frame_{frame_index:04d}_{file_suffix}.txt"
                )

                with open(output_filename, "w") as output_file:
                    output_file.writelines(frames[frame_number])

                frame_index += 1

            print(
                f"Toplam {frame_index} adet dosya '{output_folder}' klasörüne kaydedildi."
            )


# Ana klasör yolunu belirtin
parent_folder = "C:\\Users\\albur\\Desktop\\Datasets\\stanford\\annotations"

# Anotasyonları işleyin
process_annotations_in_subfolders(parent_folder)
