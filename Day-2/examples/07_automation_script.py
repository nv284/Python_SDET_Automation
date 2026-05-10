# Loop-driven automation: simulate retrying tasks and batching
tasks = ['task1', 'task2', 'task3', 'task4', 'task5']
batch_size = 2
i = 0
while i < len(tasks):
    batch = []
    j = 0
    while j < batch_size and i < len(tasks):
        batch.append(tasks[i])
        i += 1
        j += 1
    print('Processing batch:', batch)
    # simulate retries
    for t in batch:
        attempts = 0
        success = False
        while attempts < 3:
            attempts += 1
            if attempts == 2:
                success = True
                print('Succeeded', t, 'on attempt', attempts)
                break
            else:
                print('Retrying', t, 'attempt', attempts)
        if not success:
            print('Failed after retries:', t)
