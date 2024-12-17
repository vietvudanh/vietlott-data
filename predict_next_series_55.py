import json
from collections import Counter
from datetime import datetime, timedelta
from typing import List, Tuple
import random
import pandas as pd
import numpy as np
from collections import Counter, defaultdict
from typing import List, Dict, Tuple

def load_data(file_path: str) -> List[dict]:
    with open(file_path, 'r') as f:
        return [json.loads(line) for line in f]

def analyze_patterns(data: List[dict]) -> dict:
    # Overall frequency analysis
    number_frequency = Counter()
    # Recent frequency (last 30 draws)
    recent_frequency = Counter()
    # Number pairs analysis
    pair_frequency = Counter()
    # Last appearance of each number
    last_appearance = {i: 0 for i in range(1, 56)}
    
    # Process each draw
    for idx, draw in enumerate(data):
        numbers = draw['result']
        number_frequency.update(numbers)
        
        # Recent frequency (last 30 draws)
        if idx >= len(data) - 30:
            recent_frequency.update(numbers)
        
        # Update pair frequency
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                pair = tuple(sorted([numbers[i], numbers[j]]))
                pair_frequency[pair] += 1
        
        # Update last appearance
        current_draw_idx = len(data) - idx - 1
        for num in numbers:
            if last_appearance[num] == 0:
                last_appearance[num] = current_draw_idx

    # Calculate hot and cold numbers
    avg_frequency = sum(number_frequency.values()) / len(number_frequency)
    hot_numbers = {num: freq for num, freq in number_frequency.items() 
                  if freq > avg_frequency}
    cold_numbers = {num: freq for num, freq in number_frequency.items() 
                   if freq <= avg_frequency}

    return {
        'number_frequency': number_frequency,
        'recent_frequency': recent_frequency,
        'pair_frequency': pair_frequency,
        'last_appearance': last_appearance,
        'hot_numbers': hot_numbers,
        'cold_numbers': cold_numbers
    }

def predict_next_draw(patterns: dict, num_numbers: int = 6) -> List[int]:
    number_frequency = patterns['number_frequency']
    recent_frequency = patterns['recent_frequency']
    pair_frequency = patterns['pair_frequency']
    last_appearance = patterns['last_appearance']
    hot_numbers = patterns['hot_numbers']
    
    predicted_numbers = []
    
    # Step 1: Select 2 numbers from recent hot numbers (high recent frequency)
    recent_hot = [num for num, _ in recent_frequency.most_common(10)]
    predicted_numbers.extend(random.sample(recent_hot, 2))
    
    # Step 2: Select 1 number that pairs well with the selected numbers
    potential_pairs = []
    for num in range(1, 56):
        if num not in predicted_numbers:
            pair_score = sum(pair_frequency.get(tuple(sorted([num, pred])), 0) 
                           for pred in predicted_numbers)
            potential_pairs.append((num, pair_score))
    potential_pairs.sort(key=lambda x: x[1], reverse=True)
    predicted_numbers.append(potential_pairs[0][0])
    
    # Step 3: Select 1 number that hasn't appeared in a while (due for appearance)
    due_numbers = sorted([(num, gap) for num, gap in last_appearance.items() 
                         if num not in predicted_numbers],
                        key=lambda x: x[1], reverse=True)
    predicted_numbers.append(due_numbers[0][0])
    
    # Step 4: Select 2 numbers randomly with probability weighted by overall frequency
    remaining_numbers = list(set(range(1, 56)) - set(predicted_numbers))
    weights = [number_frequency[num] for num in remaining_numbers]
    predicted_numbers.extend(random.choices(remaining_numbers, weights=weights, k=2))
    
    return sorted(predicted_numbers)

def get_next_draw_date(data: List[dict]) -> str:
    last_date = max(datetime.strptime(d['date'], "%Y-%m-%d") for d in data)
    days_to_add = (3 - last_date.weekday()) % 3  # Giả sử xổ số diễn ra 3 ngày một lần
    next_draw_date = (last_date + timedelta(days=days_to_add)).strftime("%Y-%m-%d")
    return next_draw_date

def load_data_from_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    # Convert Result column from string to list of numbers
    df['Result'] = df['Result'].apply(lambda x: [int(n) for n in x.split(',')])
    return df

def analyze_detailed_patterns(df: pd.DataFrame) -> Dict:
    patterns = {}
    
    # 1. Frequency Analysis for different periods
    all_numbers = [num for result in df['Result'] for num in result]
    patterns['overall_frequency'] = Counter(all_numbers)
    
    # Last 50 draws
    recent_numbers = [num for result in df['Result'].tail(50) for num in result]
    patterns['recent_frequency'] = Counter(recent_numbers)
    
    # 2. Sequential Numbers Analysis
    sequential_count = 0
    for result in df['Result']:
        sorted_nums = sorted(result)
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                sequential_count += 1
    patterns['sequential_probability'] = sequential_count / len(df)
    
    # 3. Even/Odd Distribution
    even_odd_dist = []
    for result in df['Result']:
        even_count = len([x for x in result if x % 2 == 0])
        even_odd_dist.append((even_count, 6-even_count))
    patterns['even_odd_distribution'] = Counter(even_odd_dist)
    
    # 4. High/Low Distribution (1-27 low, 28-55 high)
    high_low_dist = []
    for result in df['Result']:
        low_count = len([x for x in result if x <= 27])
        high_low_dist.append((low_count, 6-low_count))
    patterns['high_low_distribution'] = Counter(high_low_dist)
    
    # 5. Sum and Average Patterns
    sums = [sum(result) for result in df['Result']]
    patterns['sum_stats'] = {
        'mean': np.mean(sums),
        'std': np.std(sums),
        'min': min(sums),
        'max': max(sums)
    }
    
    # 6. Gap Analysis
    gaps = defaultdict(list)
    last_seen = {i: -1 for i in range(1, 56)}
    
    for idx, result in enumerate(df['Result']):
        for num in range(1, 56):
            if num in result:
                gap = idx - last_seen[num] - 1
                if last_seen[num] != -1:
                    gaps[num].append(gap)
                last_seen[num] = idx
    
    patterns['average_gaps'] = {num: np.mean(gap_list) if gap_list else float('inf') 
                              for num, gap_list in gaps.items()}
    
    return patterns

def predict_next_draw_v2(patterns: Dict, num_numbers: int = 6) -> List[int]:
    predicted_numbers = []
    
    # 1. Lấy danh sách số theo tần suất gần đây
    recent_numbers = sorted(patterns['recent_frequency'].items(), 
                          key=lambda x: (-x[1], x[0]))  # Sắp xếp theo tần suất giảm dần, nếu bằng nhau thì theo số
    
    # 2. Lọc ra các số "đến kỳ" xuất hiện
    avg_gap = np.mean(list(patterns['average_gaps'].values()))
    due_numbers = [num for num, _ in recent_numbers 
                  if patterns['average_gaps'][num] > avg_gap]
    
    # 3. Lấy phân phối chẵn/lẻ phổ biến nhất
    most_common_even_odd = max(patterns['even_odd_distribution'].items(), 
                              key=lambda x: x[1])[0]
    target_even = most_common_even_odd[0]
    
    # 4. Chọn số theo thứ tự ưu tiên
    candidates = []
    
    # Ưu tiên 1: Số đến kỳ xuất hiện và có tần suất cao
    for num in due_numbers:
        if patterns['recent_frequency'][num] > np.mean(list(patterns['recent_frequency'].values())):
            candidates.append(num)
    
    # Ưu tiên 2: Top số xuất hiện nhiều gần đây
    for num, _ in recent_numbers:
        if num not in candidates:
            candidates.append(num)
    
    # Chọn số từ candidates, đảm bảo tỷ lệ chẵn/lẻ
    current_even = 0
    for num in candidates:
        if len(predicted_numbers) >= num_numbers:
            break
            
        # Kiểm tra điều kiện chẵn/lẻ
        is_even = num % 2 == 0
        if (is_even and current_even < target_even) or \
           (not is_even and (len(predicted_numbers) - current_even) < (num_numbers - target_even)):
            if not any(abs(num - x) == 1 for x in predicted_numbers):  # Tránh số liên tiếp
                predicted_numbers.append(num)
                if is_even:
                    current_even += 1
    
    # Nếu chưa đủ số, lấy thêm từ candidates
    while len(predicted_numbers) < num_numbers:
        for num in candidates:
            if num not in predicted_numbers and \
               not any(abs(num - x) == 1 for x in predicted_numbers):
                predicted_numbers.append(num)
                break
    
    return sorted(predicted_numbers[:num_numbers])

def print_pattern_insights(patterns: Dict):
    print("\nQuy luật phân tích từ dữ liệu Power 655:")
    
    print("\n1. Phân bố Chẵn/Lẻ phổ biến nhất:")
    for (even, odd), count in sorted(patterns['even_odd_distribution'].items(), 
                                   key=lambda x: x[1], reverse=True)[:3]:
        print(f"- {even} số chẵn, {odd} số lẻ")
    
    print("\n2. Phân bố Cao/Thấp phổ biến nhất:")
    for (low, high), count in sorted(patterns['high_low_distribution'].items(), 
                                   key=lambda x: x[1], reverse=True)[:3]:
        print(f"- {low} số thấp (1-27), {high} số cao (28-55)")
    
    print("\n3. Thống kê tổng các số:")
    print(f"- Trung bình: {patterns['sum_stats']['mean']:.1f}")
    print(f"- Độ lệch chuẩn: {patterns['sum_stats']['std']:.1f}")
    print(f"- Khoảng: {patterns['sum_stats']['min']} đến {patterns['sum_stats']['max']}")
    
    print("\n4. Xác suất xuất hiện số liên tiếp:", 
          f"{patterns['sequential_probability']*100:.1f}%")
    
    print("\n5. Top 10 số xuất hiện nhiều nhất gần đây:")
    for num, freq in sorted(patterns['recent_frequency'].items(), 
                          key=lambda x: x[1], reverse=True)[:10]:
        print(f"- Số {num}: {freq} lần")

# Main execution
if __name__ == "__main__":
    file_path = 'data/power655.jsonl'
    data = load_data(file_path)
    patterns = analyze_patterns(data)
    prediction = predict_next_draw(patterns)
    next_draw_date = get_next_draw_date(data)

    print(f"Dự đoán cho ngày {next_draw_date}:")
    print(f"Dãy số: {prediction}")

    file_path_csv = 'power655_results.csv'
    df = load_data_from_csv(file_path_csv)
    patterns = analyze_detailed_patterns(df)
    print_pattern_insights(patterns)
    
    prediction = predict_next_draw_v2(patterns)
    print("\nDự đoán cho kỳ tiếp theo:", prediction)


    # python predict_next_series_55.py  

    # PYTHONPATH=src python src/vietlott/cli/crawl.py power_655