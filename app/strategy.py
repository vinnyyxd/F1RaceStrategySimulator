TRACK_DATA = {
    'Monza': {'laps': 53, 'base_lap': 80},
    'Silverstone': {'laps': 52, 'base_lap': 90},
    'Spa': {'laps': 44, 'base_lap': 105}
}

TYRE_DATA = {
    'Soft': 0.15,
    'Medium': 0.10,
    'Hard': 0.05
}

PIT_STOP_PENALTY = 25  # seconds


def simulate_strategy(circuit, tyre, pit_stops):
    track = TRACK_DATA[circuit]
    degradation = TYRE_DATA[tyre]
    total_time = 0
    lap_time = track['base_lap']

    for lap in range(track['laps']):
        total_time += lap_time
        lap_time += degradation

    total_time += pit_stops * PIT_STOP_PENALTY
    return {
        'circuit': circuit,
        'tyre': tyre,
        'pit_stops': pit_stops,
        'total_time': round(total_time, 2)
    }
