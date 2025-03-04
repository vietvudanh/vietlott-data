import json
from collections import Counter, defaultdict
from datetime import datetime, timedelta
import random
import pandas as pd
import numpy as np
from itertools import combinations
from typing import List, Dict, Tuple

# Hàm tải dữ liệu từ file JSON Lines (.jsonl)
def load_jsonl(file_path: str) -> List[dict]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

# Phân tích chi tiết các mẫu từ danh sách dict (dữ liệu JSON)
def analyze_detailed_patterns(data: List[dict]) -> Dict:
    patterns = {}
    all_numbers = [num for result in [d['result'] for d in data] for num in result]
    patterns['overall_frequency'] = Counter(all_numbers)
    
    recent_numbers = [num for result in [d['result'] for d in data[-50:]] for num in result]
    patterns['recent_frequency'] = Counter(recent_numbers)
    
    sequential_count = 0
    for result in [d['result'] for d in data]:
        sorted_nums = sorted(result)
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                sequential_count += 1
    patterns['sequential_probability'] = sequential_count / len(data)
    
    even_odd_dist = []
    for result in [d['result'] for d in data]:
        even_count = len([x for x in result if x % 2 == 0])
        even_odd_dist.append((even_count, 7-even_count))  # Bao gồm số phụ
    patterns['even_odd_distribution'] = Counter(even_odd_dist)
    
    high_low_dist = []
    for result in [d['result'] for d in data]:
        low_count = len([x for x in result if x <= 27])
        high_low_dist.append((low_count, 7-low_count))
    patterns['high_low_distribution'] = Counter(high_low_dist)
    
    sums = [sum(result[:6]) for result in [d['result'] for d in data]]  # Chỉ tính 6 số chính
    patterns['sum_stats'] = {
        'mean': np.mean(sums),
        'std': np.std(sums),
        'min': min(sums),
        'max': max(sums)
    }
    
    gaps = defaultdict(list)
    last_seen = {i: -1 for i in range(1, 56)}
    for idx, result in enumerate([d['result'] for d in data]):
        for num in range(1, 56):
            if num in result:
                gap = idx - last_seen[num] - 1
                if last_seen[num] != -1:
                    gaps[num].append(gap)
                last_seen[num] = idx
    patterns['average_gaps'] = {num: np.mean(gap_list) if gap_list else float('inf') 
                              for num, gap_list in gaps.items()}
    
    pair_frequency = Counter()
    for result in [d['result'] for d in data]:
        for pair in combinations(sorted(result), 2):
            pair_frequency[pair] += 1
    patterns['pair_frequency'] = pair_frequency
    
    return patterns

# Phân tích mẫu theo thời gian
def analyze_time_patterns(data: List[dict]) -> dict:
    time_patterns = {
        'weekday_patterns': {},
        'number_cycles': {},
        'last_appearances': {},
        'seasonal_patterns': {}
    }
    
    dates = [pd.to_datetime(d['date']) for d in data]
    weekdays = [d.weekday() for d in dates]
    results = [d['result'] for d in data]
    
    weekday_numbers = {}
    for day in range(7):
        day_numbers = [num for idx, result in enumerate(results) if weekdays[idx] == day for num in result]
        weekday_numbers[day] = Counter(day_numbers)
    time_patterns['weekday_patterns'] = weekday_numbers
    
    for num in range(1, 56):
        appearances = [dates[idx] for idx, result in enumerate(results) if num in result]
        if appearances and len(appearances) > 1:
            gaps = [(appearances[i+1] - appearances[i]).days for i in range(len(appearances)-1)]
            time_patterns['number_cycles'][num] = sum(gaps) / len(gaps)
        time_patterns['last_appearances'][num] = appearances[-1] if appearances else None
    
    months = [d.month for d in dates]
    monthly_numbers = {}
    for month in range(1, 13):
        month_numbers = [num for idx, result in enumerate(results) if months[idx] == month for num in result]
        monthly_numbers[month] = Counter(month_numbers)
    time_patterns['seasonal_patterns'] = monthly_numbers
    
    return time_patterns

# Dự đoán dãy số tiếp theo
def predict_next_draw_v3(patterns: Dict, time_patterns: Dict, next_date: pd.Timestamp) -> Tuple[List[int], int]:
    available_numbers = list(range(1, 56))
    selected_numbers = []
    current_even = 0
    current_high = 0
    
    weights = np.zeros(55)
    
    frequency_weight = 0.5  # Tăng trọng số tần suất tổng thể
    for num, freq in patterns['overall_frequency'].items():
        weights[num-1] += freq * frequency_weight
    
    recency_weight = 0.35  # Tăng trọng số tần suất gần đây
    for num, gap in patterns['average_gaps'].items():
        recency_score = 1.0 / (gap + 1)
        weights[num-1] += recency_score * recency_weight
    
    weekday_weight = 0.1  # Giảm trọng số ngày trong tuần
    next_weekday = next_date.weekday()
    weekday_patterns = time_patterns['weekday_patterns'].get(next_weekday, {})
    max_freq = max(weekday_patterns.values(), default=1)
    for num, freq in weekday_patterns.items():
        weights[num-1] += (freq / max_freq) * weekday_weight
    
    pair_weight = 0.05  # Giảm trọng số cặp số
    recent_freq = patterns['recent_frequency']
    hot_numbers = set([num for num, freq in sorted(recent_freq.items(), key=lambda x: x[1], reverse=True)[:10]])
    cold_numbers = set([num for num, freq in sorted(recent_freq.items(), key=lambda x: x[1])[:10]])
    
    for i in range(6):
        current_weights = weights.copy()
        
        if current_even >= 4:
            for num in available_numbers:
                if num % 2 == 0:
                    current_weights[num-1] *= 0.3
        elif current_even <= 1 and i >= 4:
            for num in available_numbers:
                if num % 2 == 0:
                    current_weights[num-1] *= 1.5
                    
        if current_high >= 4:
            for num in available_numbers:
                if num > 27:
                    current_weights[num-1] *= 0.3
        elif current_high <= 1 and i >= 4:
            for num in available_numbers:
                if num > 27:
                    current_weights[num-1] *= 1.5
        
        for num in available_numbers:
            if num in hot_numbers:
                current_weights[num-1] *= 1.2
            elif num in cold_numbers:
                current_weights[num-1] *= 0.8
        
        available_indices = [num-1 for num in available_numbers]
        if sum(current_weights[available_indices]) > 0:
            current_weights[available_indices] /= sum(current_weights[available_indices])
        
        if random.random() < 0.7:
            selected_idx = available_indices[np.argmax(current_weights[available_indices])]
        else:
            top_indices = sorted(available_indices, key=lambda x: current_weights[x])[-5:]
            top_weights = current_weights[top_indices]
            top_weights = top_weights / sum(top_weights) if sum(top_weights) > 0 else np.ones(len(top_weights)) / len(top_weights)
            selected_idx = np.random.choice(top_indices, p=top_weights)
        
        selected_num = selected_idx + 1
        if selected_num % 2 == 0:
            current_even += 1
        if selected_num > 27:
            current_high += 1
            
        selected_numbers.append(selected_num)
        available_numbers.remove(selected_num)
        
        if i < 5:
            for num in available_numbers:
                pair_score = sum(patterns['pair_frequency'].get((min(num, sel), max(num, sel)), 0) 
                               for sel in selected_numbers)
                weights[num-1] = weights[num-1] * 0.7 + pair_score * pair_weight * 0.3
    
    # Dự đoán số phụ
    bonus_candidates = available_numbers
    bonus_weights = [patterns['overall_frequency'].get(num, 0) for num in bonus_candidates]
    bonus_number = random.choices(bonus_candidates, weights=bonus_weights, k=1)[0] if bonus_weights else random.choice(bonus_candidates)
    
    return sorted(selected_numbers), bonus_number

# Kiểm tra độ chính xác
def test_prediction_accuracy_v2(data: List[dict], test_size: int = 50) -> dict:
    train_data = data[:-test_size]
    test_data = data[-test_size:]
    
    metrics = {
        'exact_matches': 0,
        'partial_matches': [],
        'bonus_matches': 0,
        'avg_correct_numbers': 0.0,
    }
    
    for idx in range(len(test_data)):
        current_train = data[:len(data) - test_size + idx]
        patterns = analyze_detailed_patterns(current_train)
        time_patterns = analyze_time_patterns(current_train)
        
        test_date = pd.to_datetime(test_data[idx]['date'])
        predicted_numbers, bonus_number = predict_next_draw_v3(patterns, time_patterns, test_date)
        actual_numbers = set(test_data[idx]['result'][:6])  # 6 số chính
        actual_bonus = test_data[idx]['result'][6]  # Số phụ
        
        correct_numbers = len(set(predicted_numbers) & actual_numbers)
        metrics['partial_matches'].append(correct_numbers)
        if correct_numbers == 6:
            metrics['exact_matches'] += 1
        if bonus_number == actual_bonus:
            metrics['bonus_matches'] += 1
    
    metrics['avg_correct_numbers'] = sum(metrics['partial_matches']) / len(metrics['partial_matches'])
    metrics['accuracy_by_matches'] = {
        i: metrics['partial_matches'].count(i) / len(metrics['partial_matches']) * 100
        for i in range(7)
    }
    
    return metrics

# In thông tin chi tiết về mẫu
def print_pattern_insights(patterns: Dict):
    print("\nQuy luật phân tích từ dữ liệu Power 6/55:")
    print("\n1. Phân bố Chẵn/Lẻ phổ biến nhất:")
    for (even, odd), count in sorted(patterns['even_odd_distribution'].items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"- {even} số chẵn, {odd} số lẻ")
    
    print("\n2. Phân bố Cao/Thấp phổ biến nhất:")
    for (low, high), count in sorted(patterns['high_low_distribution'].items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"- {low} số thấp (1-27), {high} số cao (28-55)")
    
    print("\n3. Thống kê tổng các số (6 số chính):")
    print(f"- Trung bình: {patterns['sum_stats']['mean']:.1f}")
    print(f"- Độ lệch chuẩn: {patterns['sum_stats']['std']:.1f}")
    print(f"- Khoảng: {patterns['sum_stats']['min']} đến {patterns['sum_stats']['max']}")
    
    print("\n4. Xác suất xuất hiện số liên tiếp:", f"{patterns['sequential_probability']*100:.1f}%")
    
    print("\n5. Top 10 số xuất hiện nhiều nhất gần đây:")
    for num, freq in sorted(patterns['recent_frequency'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"- Số {num}: {freq} lần")

if __name__ == "__main__":
    print("\n=== VIETLOTT POWER 6/55 - DỰ ĐOÁN KẾT QUẢ ===\n")
    
    # Tải dữ liệu từ file JSON Lines
    data = load_jsonl('data/power655.jsonl')
    
    # Phân tích mẫu thời gian
    time_patterns = analyze_time_patterns(data)
    
    # Xác định ngày xổ tiếp theo
    last_date = pd.to_datetime(data[-1]['date'])
    today = pd.Timestamp.now()
    draw_days = [2, 4, 6]  # Thứ 3, 5, 7
    
    current_weekday = today.weekday()
    next_draw_day = min([day for day in draw_days if day >= current_weekday], default=draw_days[0])
    days_to_add = next_draw_day - current_weekday if next_draw_day >= current_weekday else (7 - current_weekday + next_draw_day)
    next_date = today + pd.Timedelta(days=days_to_add)
    next_date = next_date.normalize()
    
    # Phân tích và dự đoán
    patterns = analyze_detailed_patterns(data)
    predicted_numbers, bonus_number = predict_next_draw_v3(patterns, time_patterns, next_date)
    
    # In thông tin chi tiết
    print_pattern_insights(patterns)
    
    # Kiểm tra độ chính xác
    print("\nKIỂM TRA ĐỘ CHÍNH XÁC CỦA THUẬT TOÁN")
    print("=" * 50)
    accuracy_metrics = test_prediction_accuracy_v2(data)
    
    print(f"\nKết quả đánh giá độ chính xác:")
    print(f"Số lần dự đoán chính xác hoàn toàn: {accuracy_metrics['exact_matches']}")
    print(f"Trung bình số con số đúng mỗi lần dự đoán: {accuracy_metrics['avg_correct_numbers']:.2f}")
    print(f"Số lần dự đoán đúng số phụ: {accuracy_metrics['bonus_matches']}")
    print("\nPhần trăm dự đoán theo số lượng con số đúng:")
    for matches, percentage in accuracy_metrics['accuracy_by_matches'].items():
        print(f"{matches} số đúng: {percentage:.2f}%")
    
    print("=" * 50)
    print(f"DỰ ĐOÁN CHO NGÀY: {next_date.strftime('%d-%m-%Y')} (Thứ {next_draw_day + 1})")
    print(f"6 SỐ CHÍNH DỰ ĐOÁN: {predicted_numbers}")
    print(f"SỐ PHỤ DỰ ĐOÁN: {bonus_number}")

# Hướng dẫn sử dụng:
# 1. Chạy dự đoán:
#    python3 predict_next_series_55.py
#
# 2. Cập nhật dữ liệu:
#    - Lưu dữ liệu JSON Lines vào file 'power655.jsonl' với định dạng từng dòng là một object JSON.
#    - Cài đặt môi trường:
#      python3 -m venv venv
#      source venv/bin/activate
#      pip install pandas numpy
#
# Lưu ý:
# - Dữ liệu cần đúng định dạng JSON Lines với các trường: date, id, result, page, process_time
# - Cập nhật dữ liệu thường xuyên để dự đoán chính xác hơn