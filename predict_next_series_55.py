import json
from collections import Counter
from datetime import datetime, timedelta
from typing import List, Tuple
import random

def load_data(file_path: str) -> List[dict]:
    with open(file_path, 'r') as f:
        return [json.loads(line) for line in f]

def analyze_patterns(data: List[dict]) -> dict:
    number_frequency = Counter()
    for draw in data:
        number_frequency.update(draw['result'])
    return {'number_frequency': number_frequency}

def predict_next_draw(patterns: dict, num_numbers: int = 6) -> List[int]:
    number_frequency = patterns['number_frequency']
    
    # Chọn 4 số từ top 20 số xuất hiện nhiều nhất
    top_numbers = [num for num, _ in number_frequency.most_common(20)]
    predicted_numbers = random.sample(top_numbers, 4)
    
    # Chọn 2 số ngẫu nhiên từ các số còn lại
    remaining_numbers = list(set(range(1, 56)) - set(predicted_numbers))
    predicted_numbers.extend(random.sample(remaining_numbers, 2))
    
    return sorted(predicted_numbers)

def get_next_draw_date(data: List[dict]) -> str:
    last_date = max(datetime.strptime(d['date'], "%Y-%m-%d") for d in data)
    days_to_add = (3 - last_date.weekday()) % 3  # Giả sử xổ số diễn ra 3 ngày một lần
    next_draw_date = (last_date + timedelta(days=days_to_add)).strftime("%Y-%m-%d")
    return next_draw_date

# Main execution
file_path = 'data/power655.jsonl'
data = load_data(file_path)
patterns = analyze_patterns(data)
prediction = predict_next_draw(patterns)
next_draw_date = get_next_draw_date(data)

print(f"Dự đoán cho ngày {next_draw_date}:")
print(f"Dãy số: {prediction}")

#  source .venv/bin/activate && PYTHONPATH=src python src/vietlott/cli/crawl.py power_655  

#  python predict_next_series_55.py       