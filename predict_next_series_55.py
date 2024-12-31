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
    
    # 7. Pair Frequency Analysis
    pair_frequency = {}
    for result in df['Result']:
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                pair = (result[i], result[j])
                pair_frequency[pair] = pair_frequency.get(pair, 0) + 1
                # Thêm cả chiều ngược lại
                pair_rev = (result[j], result[i])
                pair_frequency[pair_rev] = pair_frequency[pair]
    patterns['pair_frequency'] = pair_frequency
    
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
    
    return sorted(predicted_numbers)

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

def test_prediction_accuracy(df: pd.DataFrame, test_size: int = 50) -> dict:
    """
    Test the prediction accuracy using historical data.
    
    Args:
        df: DataFrame containing historical lottery results
        test_size: Number of recent draws to use for testing
        
    Returns:
        Dictionary containing accuracy metrics
    """
    # Split data into training and testing sets
    train_df = df.iloc[:-test_size]
    test_df = df.iloc[-test_size:]
    
    metrics = {
        'exact_matches': 0,  # Predictions that match exactly
        'partial_matches': [],  # Number of correct numbers in each prediction
        'avg_correct_numbers': 0.0,  # Average number of correct numbers per prediction
    }
    
    for idx, test_row in test_df.iterrows():
        # Get training data up to this point
        current_train = df[df.index < idx]
        
        # Analyze patterns and make prediction
        patterns = analyze_detailed_patterns(current_train)
        predicted_numbers = predict_next_draw_v2(patterns)
        actual_numbers = set(test_row['Result'])
        
        # Compare prediction with actual results
        correct_numbers = len(set(predicted_numbers) & actual_numbers)
        metrics['partial_matches'].append(correct_numbers)
        
        if correct_numbers == 6:  # All numbers match
            metrics['exact_matches'] += 1
    
    # Calculate average accuracy
    metrics['avg_correct_numbers'] = sum(metrics['partial_matches']) / len(metrics['partial_matches'])
    metrics['accuracy_by_matches'] = {
        i: metrics['partial_matches'].count(i) / len(metrics['partial_matches']) * 100
        for i in range(7)
    }
    
    return metrics

def analyze_time_patterns(df: pd.DataFrame) -> dict:
    """
    Analyze patterns related to time and date of number appearances.
    """
    time_patterns = {
        'weekday_patterns': {},  # Patterns for each day of week
        'number_cycles': {},     # Average cycles for each number
        'last_appearances': {},  # Last appearance date for each number
        'seasonal_patterns': {}  # Monthly patterns
    }
    
    # Convert date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Analyze weekday patterns
    df['weekday'] = df['Date'].dt.dayofweek
    weekday_numbers = {}
    for day in range(7):
        day_numbers = []
        for numbers in df[df['weekday'] == day]['Result']:
            day_numbers.extend(numbers)
        weekday_numbers[day] = Counter(day_numbers)
    time_patterns['weekday_patterns'] = weekday_numbers
    
    # Analyze cycles and gaps for each number
    for num in range(1, 56):
        appearances = []
        for idx, row in df.iterrows():
            if num in row['Result']:
                appearances.append(row['Date'])
        
        if appearances:
            # Calculate average cycle (days between appearances)
            if len(appearances) > 1:
                gaps = [(appearances[i+1] - appearances[i]).days 
                       for i in range(len(appearances)-1)]
                avg_cycle = sum(gaps) / len(gaps)
                time_patterns['number_cycles'][num] = avg_cycle
            
            # Record last appearance
            time_patterns['last_appearances'][num] = appearances[-1]
    
    # Analyze seasonal patterns (monthly)
    df['month'] = df['Date'].dt.month
    monthly_numbers = {}
    for month in range(1, 13):
        month_numbers = []
        for numbers in df[df['month'] == month]['Result']:
            month_numbers.extend(numbers)
        monthly_numbers[month] = Counter(month_numbers)
    time_patterns['seasonal_patterns'] = monthly_numbers
    
    return time_patterns

def predict_next_draw_v3(patterns, time_patterns, next_date):
    available_numbers = list(range(1, 56))
    selected_numbers = []
    current_even = 0
    current_high = 0
    
    # Calculate base weights for all numbers
    weights = np.zeros(55)
    
    # Weight based on frequency (40%)
    frequency_weight = 0.4
    for num, freq in patterns['overall_frequency'].items():
        weights[num-1] += freq * frequency_weight
    
    # Weight based on recency (30%)
    recency_weight = 0.3
    for num, gap in patterns['average_gaps'].items():
        recency_score = 1.0 / (gap + 1)  # Inverse of average gap
        weights[num-1] += recency_score * recency_weight
    
    # Weight based on weekday patterns (15%)
    weekday_weight = 0.15
    next_weekday = next_date.weekday()
    weekday_patterns = time_patterns['weekday_patterns'].get(next_weekday, {})
    for num, freq in weekday_patterns.items():
        weights[num-1] += (freq / (max(weekday_patterns.values()) + 1e-10)) * weekday_weight
    
    # Weight based on pair frequency (15%)
    pair_weight = 0.15
    if len(selected_numbers) > 0:
        for num in available_numbers:
            pair_score = 0
            for selected in selected_numbers:
                pair_key = (min(num, selected), max(num, selected))
                if pair_key in patterns['pair_frequency']:
                    pair_score += patterns['pair_frequency'][pair_key]
            weights[num-1] += pair_score * pair_weight
    
    # Add hot/cold number strategy
    recent_freq = patterns['recent_frequency']
    hot_numbers = set([num for num, freq in sorted(recent_freq.items(), 
                                                 key=lambda x: x[1], reverse=True)[:10]])
    cold_numbers = set([num for num, freq in sorted(recent_freq.items(), 
                                                 key=lambda x: x[1])[:10]])
    
    # Select numbers one by one
    for i in range(6):
        current_weights = weights.copy()
        
        # Apply constraints for even/odd and high/low numbers
        if current_even >= 4:  # Too many even numbers
            for j, num in enumerate(available_numbers):
                if num % 2 == 0:
                    current_weights[num-1] *= 0.3
        elif current_even <= 1 and i >= 4:  # Too few even numbers
            for j, num in enumerate(available_numbers):
                if num % 2 == 0:
                    current_weights[num-1] *= 1.5
                    
        if current_high >= 4:  # Too many high numbers
            for j, num in enumerate(available_numbers):
                if num > 28:
                    current_weights[num-1] *= 0.3
        elif current_high <= 1 and i >= 4:  # Too few high numbers
            for j, num in enumerate(available_numbers):
                if num > 28:
                    current_weights[num-1] *= 1.5
        
        # Adjust weights based on hot/cold strategy
        for num in available_numbers:
            if num in hot_numbers:
                current_weights[num-1] *= 1.2
            elif num in cold_numbers:
                current_weights[num-1] *= 0.8
        
        # Normalize weights for available numbers only
        available_indices = [num-1 for num in available_numbers]
        current_weights[available_indices] = current_weights[available_indices] / np.sum(current_weights[available_indices])
        
        # Selection strategy: 70% highest weight, 30% weighted random from top 5
        if random.random() < 0.7:
            selected_idx = available_indices[np.argmax(current_weights[available_indices])]
        else:
            # Get top 5 indices from available numbers
            top_indices = sorted(available_indices, key=lambda x: current_weights[x])[-5:]
            top_weights = current_weights[top_indices]
            top_weights = top_weights / np.sum(top_weights)  # Renormalize
            selected_idx = np.random.choice(top_indices, p=top_weights)
        
        selected_num = selected_idx + 1
        
        # Update counters
        if selected_num % 2 == 0:
            current_even += 1
        if selected_num > 28:
            current_high += 1
            
        selected_numbers.append(selected_num)
        available_numbers.remove(selected_num)
        
        # Update pair weights after each selection
        if i < 5:  # Don't need to update for the last number
            for num in available_numbers:
                pair_score = 0
                for selected in selected_numbers:
                    pair_key = (min(num, selected), max(num, selected))
                    if pair_key in patterns['pair_frequency']:
                        pair_score += patterns['pair_frequency'][pair_key]
                weights[num-1] = weights[num-1] * 0.7 + pair_score * pair_weight * 0.3
    
    return sorted(selected_numbers)

def test_prediction_accuracy_v2(df: pd.DataFrame, test_size: int = 50) -> dict:
    train_df = df.iloc[:-test_size]
    test_df = df.iloc[-test_size:]
    
    metrics = {
        'exact_matches': 0,
        'partial_matches': [],
        'avg_correct_numbers': 0.0,
    }
    
    for idx, test_row in test_df.iterrows():
        current_train = df[df.index < idx]
        patterns = analyze_detailed_patterns(current_train)
        time_patterns = analyze_time_patterns(current_train)
        
        test_date = pd.to_datetime(test_row['Date'])
        predicted_numbers = predict_next_draw_v3(patterns, time_patterns, test_date)
        actual_numbers = set(test_row['Result'])
        
        correct_numbers = len(set(predicted_numbers) & actual_numbers)
        metrics['partial_matches'].append(correct_numbers)
        
        if correct_numbers == 6:
            metrics['exact_matches'] += 1
    
    metrics['avg_correct_numbers'] = sum(metrics['partial_matches']) / len(metrics['partial_matches'])
    metrics['accuracy_by_matches'] = {
        i: metrics['partial_matches'].count(i) / len(metrics['partial_matches']) * 100
        for i in range(7)
    }
    
    return metrics

if __name__ == "__main__":
    print("\n=== VIETLOTT POWER 655 - DỰ ĐOÁN KẾT QUẢ ===\n")
    
    # Load data
    df = load_data_from_csv('power655_results.csv')
    
    # Get time patterns
    time_patterns = analyze_time_patterns(df)
    
    # Get next draw date
    last_date = pd.to_datetime(df['Date'].max())
    today = pd.Timestamp.now()
    
    # Map thứ trong tuần (0 = thứ 2, 6 = chủ nhật) sang ngày xổ (2 = thứ 3, 4 = thứ 5, 6 = thứ 7)
    draw_days = [2, 4, 6]  # Thứ 3, 5, 7
    
    # Tìm ngày xổ gần nhất
    current_weekday = today.weekday()
    next_draw_day = None
    
    for draw_day in draw_days:
        if draw_day > current_weekday:
            next_draw_day = draw_day
            break
    
    if next_draw_day is None:  # Nếu đã qua thứ 7, lấy thứ 3 tuần sau
        next_draw_day = draw_days[0]
        days_to_add = 7 - current_weekday + next_draw_day
    else:
        days_to_add = next_draw_day - current_weekday
    
    next_date = today + pd.Timedelta(days=days_to_add)
    next_date = next_date.normalize()  # Chuẩn hóa về 00:00:00
    
    # Get patterns and make prediction
    patterns = analyze_detailed_patterns(df)
    prediction = predict_next_draw_v3(patterns, time_patterns, next_date)
    

    
    # Test prediction accuracy
    print("\nKIỂM TRA ĐỘ CHÍNH XÁC CỦA THUẬT TOÁN")
    print("=" * 50)
    
    accuracy_metrics = test_prediction_accuracy_v2(df)
    
    print(f"\nKết quả đánh giá độ chính xác:")
    print(f"Số lần dự đoán chính xác hoàn toàn: {accuracy_metrics['exact_matches']}")
    print(f"Trung bình số con số đúng mỗi lần dự đoán: {accuracy_metrics['avg_correct_numbers']:.2f}")
    print("\nPhần trăm dự đoán theo số lượng con số đúng:")
    for matches, percentage in accuracy_metrics['accuracy_by_matches'].items():
        print(f"{matches} số đúng: {percentage:.2f}%")


    print("=" * 50)
    print(f"DỰ ĐOÁN CHO NGÀY: {next_date.strftime('%d-%m-%Y')} (Thứ {next_draw_day + 1})")
    print(f"DÃY SỐ DỰ ĐOÁN: {prediction}")
    
# Hướng dẫn sử dụng:
    
# 1. Để chạy dự đoán:
# python3 predict_next_series_55.py
    
# 2. Để cập nhật dữ liệu mới:
# - Cài đặt môi trường:
#   python3 -m venv venv
#   source venv/bin/activate
#   pip install pandas numpy
    
# - Chạy script cào dữ liệu:
#   PYTHONPATH=src python src/vietlott/cli/crawl.py power_655
    
# - File kết quả sẽ được lưu tại:
#   power655_results.csv
    
# Lưu ý: 
# - Nên cập nhật dữ liệu định kỳ để có kết quả dự đoán chính xác hơn
# - Dữ liệu càng mới càng tốt vì thuật toán có xét đến yếu tố thởi gian