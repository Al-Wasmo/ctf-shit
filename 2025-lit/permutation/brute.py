import random
import time
from itertools import permutations

# All permutations of "0123" 
perms = [''.join(p) for p in permutations("0123")]
# Filter to only permutations that start with '0'
zero_perms = [p for p in perms if p.startswith('0')]

print(f"Permutations starting with 0: {zero_perms}")

best_seq = None
best_count = 0
call_count = 0
MAX_CALLS = 200000

def count_unique_windows(seq):
    """Fast window counting"""
    seen = set()
    for i in range(len(seq) - 3):
        window = seq[i:i+4]
        if len(set(window)) == 4:
            seen.add(window)
    return len(seen)

def get_new_windows(current_seq, new_perm):
    """Count only the NEW windows that would be added by appending new_perm"""
    if not current_seq:
        return count_unique_windows(new_perm)
    
    extended = current_seq + new_perm
    new_windows = set()
    
    # Only check windows that include part of the new permutation
    start_idx = max(0, len(current_seq) - 3)
    for i in range(start_idx, len(extended) - 3):
        window = extended[i:i+4]
        if len(set(window)) == 4:
            new_windows.add(window)
    
    # Count existing windows
    existing = set()
    if len(current_seq) >= 4:
        for i in range(len(current_seq) - 3):
            window = current_seq[i:i+4]
            if len(set(window)) == 4:
                existing.add(window)
    
    return len(new_windows - existing)

def backtrack(current_seq, current_count, depth=0):
    global best_seq, best_count, call_count
    
    call_count += 1
    if call_count > MAX_CALLS:
        return
    
    # Stop if sequence would be too long (33 is our target)
    if len(current_seq) > 33:
        return
    
    # Update best solution
    if current_count > best_count or (current_count == best_count and (best_seq is None or len(current_seq) < len(best_seq))):
        best_count = current_count
        best_seq = current_seq
        print(f"New best: {best_count} windows, length={len(current_seq)}, depth={depth}")
        print(f"Sequence: {current_seq}")
    
    # Pruning: estimate maximum possible improvement
    remaining_length = 33 - len(current_seq)
    max_possible_new_windows = remaining_length // 4 * 4
    if current_count + max_possible_new_windows <= best_count:
        return
    
    # For the first move, only use zero_perms
    if not current_seq:
        available_perms = zero_perms
    else:
        available_perms = perms
    
    # Try extending with each available perm (randomized order)
    perm_list = available_perms.copy()
    random.shuffle(perm_list)
    
    # Sort by potential (try most promising first)
    perm_scores = []
    for p in perm_list[:15]:  # Evaluate more candidates
        if len(current_seq + p) <= 33:
            new_windows = get_new_windows(current_seq, p)
            perm_scores.append((new_windows, p))
    
    # Sort by score descending, with some randomness
    perm_scores.sort(key=lambda x: x[0] + random.uniform(-0.3, 0.3), reverse=True)
    
    for score, p in perm_scores:
        if call_count > MAX_CALLS:
            break
        new_seq = current_seq + p
        new_count = current_count + score
        backtrack(new_seq, new_count, depth + 1)

def greedy_start():
    """Generate a good starting solution using greedy approach, starting with 0"""
    current = ""
    current_count = 0
    
    # First, must start with a 0-permutation
    best_perm = None
    best_gain = -1
    
    for p in zero_perms:
        if len(p) <= 33:
            gain = get_new_windows("", p)
            if gain > best_gain:
                best_gain = gain
                best_perm = p
    
    if best_perm:
        current = best_perm
        current_count = best_gain
    
    # Continue greedily
    while len(current) <= 25:  # Leave room for more
        best_perm = None
        best_gain = -1
        
        for p in perms:
            if len(current + p) > 33:
                continue
            gain = get_new_windows(current, p)
            if gain > best_gain:
                best_gain = gain
                best_perm = p
        
        if best_perm is None or best_gain == 0:
            break
            
        current += best_perm
        current_count += best_gain
    
    return current, current_count

def multi_start_search(num_starts=15):
    """Run multiple randomized searches"""
    global best_seq, best_count, call_count
    
    for start_num in range(num_starts):
        print(f"\n=== START {start_num + 1}/{num_starts} ===")
        call_count = 0
        
        # Mix of greedy and random starts
        if start_num == 0 or random.random() < 0.7:
            start_seq, start_count = greedy_start()
            print(f"Greedy start: {start_count} windows, length={len(start_seq)}")
        else:
            # Random start with a 0-permutation
            start_perm = random.choice(zero_perms)
            start_seq = start_perm
            start_count = count_unique_windows(start_seq)
            print(f"Random start with {start_perm}: {start_count} windows")
        
        # Update global best if this start is better
        if start_count > best_count:
            best_count = start_count
            best_seq = start_seq
            print(f"New global best from start: {best_count}")
        
        # Continue with backtracking from this start
        backtrack(start_seq, start_count)
        
        print(f"Calls made: {call_count}")

# Run multiple iterations to find the best 33-byte sequence
for iteration in range(50):
    print(f"\n{'='*20} ITERATION {iteration + 1} {'='*20}")
    
    start_time = time.time()
    multi_start_search(num_starts=8)
    end_time = time.time()
    
    print(f"\n=== ITERATION {iteration + 1} RESULTS ===")
    print(f"Best sequence: {best_seq}")
    print(f"Length: {len(best_seq) if best_seq else 0}")
    print(f"Unique windows: {best_count}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    
    # Verify the result
    if best_seq:
        verify_count = count_unique_windows(best_seq)
        print(f"Verification: {verify_count} windows")
        
        # Show the windows
        windows = set()
        for i in range(len(best_seq) - 3):
            window = best_seq[i:i+4]
            if len(set(window)) == 4:
                windows.add(window)
        
        print(f"All windows: {sorted(list(windows))}")
        print(f"Starts with 0: {best_seq[0] == '0'}")
        print(f"Length constraint (≤33): {len(best_seq) <= 33}")
        
        # If we hit 24 windows (maximum possible), we can stop
        if best_count >= 24:
            print("MAXIMUM ACHIEVED!")
            break
        
        # If we get a really good result, we might want to continue a bit more
        if best_count >= 23:
            print("Very good result! Running a few more iterations...")
            if iteration > iteration + 10:  # Run 10 more after hitting 23
                break

# 02130123102312031230132013021032