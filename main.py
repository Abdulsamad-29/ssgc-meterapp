import threading
from yolov5_meter.detect import start_program
from yolov5_digits.detect import digits_detection

# if __name__ == "__main__":
def run():
    base_path = "D:/FAST/Sem8/FYP-II/REST_API_2/Model_Compilation_New_Compilation/meter_digit_recognition"
    start_program()
    digits = digits_detection()
    return digits
