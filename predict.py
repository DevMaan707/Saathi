from ultralytics import YOLO

model=YOLO('best).pt')

model.predict('download.jpg',save=True)
