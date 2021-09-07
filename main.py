import utilities_controller as uc

if __name__ == '__main__':
    utFunc = uc.import_utility('utilityFunction', newThread=False)
    print(utFunc.field)

    utThread = uc.import_utility('utilityThread', newThread=True)
    utThread.start()
    print(utThread.queue.get())