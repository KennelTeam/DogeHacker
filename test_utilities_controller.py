import utilities_controller as uc

if __name__ == '__main__':
    utFunc = uc.import_utility('utility_function', newThread=False)
    print(utFunc.field)

    utThread = uc.import_utility('utility_thread', newThread=True)
    utThread.start()
    print(utThread.queue.get())
