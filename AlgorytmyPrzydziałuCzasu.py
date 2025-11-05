import random
import numpy as np

# Definicja klasy Procesu
class Process:
    def __init__(self, arrival_time, burst_time):
        self.arrival_time = arrival_time   # Ustawia czas przybycia procesu
        self.burst_time = burst_time       # Ustawia czas trwania procesu


    def __str__(self):
        return f"({self.arrival_time}, {self.burst_time})" # Tekstowa reprezentacja procesu
# Generowanie losowych procesów
def generate_processes(num_processes):
    # Zwraca listę procesów o losowych czasach przybycia i trwania
    return [Process(random.randint(0, 99), random.randint(1, 20)) for _ in range(num_processes)]

# Algorytm FCFS
def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sortuje procesy według czasu przybycia

    current_time = 0  # Inicjalizuje bieżący czas na 0
    waiting_times = []  # Lista na przechowywanie czasów oczekiwania
    turnaround_times = []  # Lista na przechowywanie czasów realizacji

    for process in processes:  # Iteruje przez każdy proces
        if current_time < process.arrival_time:  # Sprawdza, czy bieżący czas jest mniejszy od czasu przybycia procesu
            current_time = process.arrival_time  # Ustawia bieżący czas na czas przybycia procesu
        waiting_time = current_time - process.arrival_time  # Oblicza czas oczekiwania dla procesu
        completion_time = current_time + process.burst_time  # Oblicza czas zakończenia procesu
        turnaround_time = completion_time - process.arrival_time  # Oblicza czas realizacji dla procesu
        waiting_times.append(waiting_time)  # Dodaje czas oczekiwania do listy czasów oczekiwania
        turnaround_times.append(turnaround_time)  # Dodaje czas realizacji do listy czasów realizacji
        current_time = completion_time  # Ustawia bieżący czas na czas zakończenia procesu

    avg_waiting_time = np.mean(waiting_times)  # Oblicza średni czas oczekiwania
    avg_turnaround_time = np.mean(turnaround_times)  # Oblicza średni czas realizacji
    return avg_waiting_time, avg_turnaround_time  # Zwraca średni czas oczekiwania i średni czas realizacji

# Algorytm SJF
def sjf(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sortuje procesy według czasu przybycia
    current_time = 0  # Inicjalizuje bieżący czas na 0
    waiting_times = []  # Lista na przechowywanie czasów oczekiwania
    turnaround_times = []  # Lista na przechowywanie czasów realizacji
    remaining_processes = processes.copy()  # Tworzy kopię listy procesów do przetworzenia

    while remaining_processes:
        # Wybiera dostępne procesy, które przybyły do bieżącego czasu
        available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]

        if not available_processes:
            # Ustawia bieżący czas na najwcześniejszy czas przybycia z pozostałych procesów jeśli nie ma dostępnych procesów
            current_time = min(remaining_processes, key=lambda x: x.arrival_time).arrival_time
            continue  # Przechodzi do następnej iteracji
        # Wybiera proces z najkrótszym czasem trwania spośród dostępnych procesów
        process = min(available_processes, key=lambda x: x.burst_time)
        waiting_time = current_time - process.arrival_time  # Oblicza czas oczekiwania dla procesu
        completion_time = current_time + process.burst_time  # Oblicza czas zakończenia procesu
        turnaround_time = completion_time - process.arrival_time  # Oblicza czas realizacji dla procesu
        waiting_times.append(waiting_time)  # Dodaje czas oczekiwania do listy czasów oczekiwania
        turnaround_times.append(turnaround_time)  # Dodaje czas realizacji do listy czasów realizacji
        current_time = completion_time  # Ustawia bieżący czas na czas zakończenia procesu
        remaining_processes.remove(process)  # Usuwa przetworzony proces z listy pozostałych procesów

    avg_waiting_time = np.mean(waiting_times)  # Oblicza średni czas oczekiwania
    avg_turnaround_time = np.mean(turnaround_times)  # Oblicza średni czas realizacji
    return avg_waiting_time, avg_turnaround_time  # Zwraca średni czas oczekiwania i średni czas realizacji


# Algorytm LCFS
def lcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sortuje procesy według czasu przybycia
    current_time = 0  # Inicjalizuje bieżący czas na 0
    waiting_times = []  # Lista na przechowywanie czasów oczekiwania
    turnaround_times = []  # Lista na przechowywanie czasów realizacji
    remaining_processes = processes.copy()  # Tworzy kopię listy procesów do przetworzenia

    while remaining_processes:  # Dopóki są jeszcze procesy do przetworzenia
        # Wybiera dostępne procesy, które przybyły do bieżącego czasu
        available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]
        if not available_processes:  # Jeśli nie ma dostępnych procesów
            # Ustawia bieżący czas na najwcześniejszy czas przybycia z pozostałych procesów
            current_time = min(remaining_processes, key=lambda x: x.arrival_time).arrival_time
            continue  # Przechodzi do następnej iteracji
        # Wybiera proces z najpóźniejszym czasem przybycia spośród dostępnych procesów
        process = max(available_processes, key=lambda x: x.arrival_time)
        waiting_time = current_time - process.arrival_time  # Oblicza czas oczekiwania dla procesu
        completion_time = current_time + process.burst_time  # Oblicza czas zakończenia procesu
        turnaround_time = completion_time - process.arrival_time  # Oblicza czas realizacji dla procesu
        waiting_times.append(waiting_time)  # Dodaje czas oczekiwania do listy czasów oczekiwania
        turnaround_times.append(turnaround_time)  # Dodaje czas realizacji do listy czasów realizacji
        current_time = completion_time  # Ustawia bieżący czas na czas zakończenia procesu
        remaining_processes.remove(process)  # Usuwa przetworzony proces z listy pozostałych procesów

    avg_waiting_time = np.mean(waiting_times)  # Oblicza średni czas oczekiwania
    avg_turnaround_time = np.mean(turnaround_times)  # Oblicza średni czas realizacji
    return avg_waiting_time, avg_turnaround_time  # Zwraca średni czas oczekiwania i średni czas realizacji
# Testowanie algorytmów

num_tests = 100
num_processes = 100

fcfs_waiting_times = []
fcfs_turnaround_times = []
sjf_waiting_times = []
sjf_turnaround_times = []
lcsf_waiting_times = []
lcsf_turnaround_times = []

# Testowanie FCFS
print("Testing FCFS")
for i in range(num_tests):  # Pętla po liczbie testów
    random.seed(i)  # Ustawia ziarno losowe, aby wyniki były powtarzalne
    processes = generate_processes(num_processes)  # Generuje losowe procesy
    avg_waiting_time, avg_turnaround_time = fcfs(processes)  # Przeprowadza algorytm FCFS
    fcfs_waiting_times.append(avg_waiting_time)  # Dodaje średni czas oczekiwania do listy
    fcfs_turnaround_times.append(avg_turnaround_time)  # Dodaje średni czas realizacji do listy
    print(f"Test {i + 1} FCFS: Średni czas oczekiwania: {avg_waiting_time}, Średni czas cyklu przetwarzania: {avg_turnaround_time}")
    #print(f"Proces: {i +1}", [(p.arrival_time, p.burst_time) for p in processes])
    # Wyświetla numer testu oraz listę krotek (czas przybycia, czas trwania) dla wszystkich procesów w danym teście
# Testowanie SJF
print("\nTesting SJF")
for i in range(num_tests):
    random.seed(i)
    processes = generate_processes(num_processes)
    avg_waiting_time, avg_turnaround_time = sjf(processes)
    sjf_waiting_times.append(avg_waiting_time)
    sjf_turnaround_times.append(avg_turnaround_time)
    print(f"Test {i + 1} SJF: Średni czas oczekiwania: {avg_waiting_time}, Średni czas cyklu przetwarzania: {avg_turnaround_time}")
    #print(f"Proces: {i +1}", [(p.arrival_time, p.burst_time) for p in processes])

# Testowanie LCSF
print("\nTesting LCFS")
for i in range(num_tests):
    random.seed(i)
    processes = generate_processes(num_processes)
    avg_waiting_time, avg_turnaround_time = lcfs(processes)
    lcsf_waiting_times.append(avg_waiting_time)
    lcsf_turnaround_times.append(avg_turnaround_time)
    print(f"Test {i + 1} LCFS: Średni czas oczekiwania: {avg_waiting_time}, Średni czas cyklu przetwarzania: {avg_turnaround_time}")
    #print(f"Proces: {i +1}", [(p.arrival_time, p.burst_time) for p in processes])

print(f"\nFCFS: Średni czas oczekiwania: {np.mean(fcfs_waiting_times)}, Średni czas cyklu przetwarzania: {np.mean(fcfs_turnaround_times)}")
print(f"SJF: Średni czas oczekiwania: {np.mean(sjf_waiting_times)}, Średni czas cyklu przetwarzania: {np.mean(sjf_turnaround_times)}")
print(f"LCFS: Średni czas oczekiwania: {np.mean(lcsf_waiting_times)}, Średni czas cyklu przetwarzania: {np.mean(lcsf_turnaround_times)}")

