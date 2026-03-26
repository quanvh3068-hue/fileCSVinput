class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.priority = int(priority)

        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

    def __repr__(self):
        return f"Process({self.pid}, AT={self.arrival_time}, BT={self.burst_time})"


def calculate_times(processes):
    current_time = 0

    for p in processes:
        if current_time < p.arrival_time:
            current_time = p.arrival_time

        p.start_time = current_time
        p.completion_time = current_time + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        current_time = p.completion_time

    return processes