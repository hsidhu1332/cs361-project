import zmq

import numpy as np

def determine_trend(numbers):
    if len(numbers) < 2:
        return 'N/A'
    x = np.arange(len(numbers))
    y = np.array(numbers)

    m, b = np.polyfit(x, y, 1)

    if m > 0:
        return "increasing"
    elif m < 0:
        return "decreasing"
    else:
        return "constant"


def calculate_average(numbers):
    if not numbers:
        return "Error: No numbers provided"
    numbers = [float(num) for num in numbers]
    average = sum(numbers) / len(numbers)
    trend = determine_trend(numbers)
    return f"Average: {average}, Trend: {trend}"

def calculate_average_and_trend(numbers):
        numbers_str = ' '.join(map(str, numbers))
        return numbers_str

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5558")

    while True:
        message = socket.recv_pyobj()
        message_calc = calculate_average_and_trend(message)
        numbers = message_calc.split()
        result = calculate_average(numbers)
        print('Sending trend of random player')
        socket.send_string(result)

if __name__ == "__main__":
    main()