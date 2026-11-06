def test_q1():
    t_a_io = 14
    t_b_cpu = 9
    seq_time = t_a_io + t_b_cpu
    conc_time = max(t_a_io, t_b_cpu)
    assert seq_time == 23
    assert conc_time == 14
    print("Q1 timing verified: Sequential = 23 ms, Concurrent = 14 ms")

def test_q2():
    balance = 100
    temp_a = balance
    temp_b = balance
    temp_a += 30
    balance = temp_a
    temp_b += 20
    balance = temp_b
    assert balance == 120
    print("Q2 lost update trace verified: Final balance = 120")

def test_q9():
    alloc = {
        'P0': [1, 0],
        'P1': [1, 1],
        'P2': [0, 1]
    }
    max_claim = {
        'P0': [2, 1],
        'P1': [1, 2],
        'P2': [2, 2]
    }
    avail = [1, 1]

    need = {}
    for p in alloc:
        need[p] = [max_claim[p][0] - alloc[p][0], max_claim[p][1] - alloc[p][1]]

    assert need['P0'] == [1, 1]
    assert need['P1'] == [0, 1]
    assert need['P2'] == [2, 1]

    def find_safe_sequence(curr_alloc, curr_need, curr_avail):
        work = list(curr_avail)
        finish = {p: False for p in curr_alloc}
        seq = []
        while len(seq) < len(curr_alloc):
            found = False
            for p in curr_alloc:
                if not finish[p]:
                    if curr_need[p][0] <= work[0] and curr_need[p][1] <= work[1]:
                        work[0] += curr_alloc[p][0]
                        work[1] += curr_alloc[p][1]
                        finish[p] = True
                        seq.append(p)
                        found = True
                        break
            if not found:
                break
        return seq, work, all(finish.values())

    orig_seq, orig_work, is_safe = find_safe_sequence(alloc, need, avail)
    assert is_safe
    print(f"Q9(a, b) verified: Need computed, Safe sequence = {orig_seq}, Final Work = {orig_work}")

    req = [1, 1]
    assert req[0] <= need['P2'][0] and req[1] <= need['P2'][1]
    assert req[0] <= avail[0] and req[1] <= avail[1]

    t_avail = [avail[0] - req[0], avail[1] - req[1]]
    t_alloc = {
        'P0': list(alloc['P0']),
        'P1': list(alloc['P1']),
        'P2': [alloc['P2'][0] + req[0], alloc['P2'][1] + req[1]]
    }
    t_need = {
        'P0': list(need['P0']),
        'P1': list(need['P1']),
        'P2': [need['P2'][0] - req[0], need['P2'][1] - req[1]]
    }
    _, _, t_safe = find_safe_sequence(t_alloc, t_need, t_avail)
    assert not t_safe
    print("Q9(c) verified: Request passes initial checks but tentative state is UNSAFE (grant denied)")

def test_q10():
    total = 4
    alloc = [2, 2]
    max_c = [3, 3]
    avail = total - sum(alloc)
    need = [max_c[0] - alloc[0], max_c[1] - alloc[1]]
    assert avail == 0
    assert need == [1, 1]
    safe = any(n <= avail for n in need)
    assert not safe
    print("Q10 verified: State is UNSAFE (available 0 < need 1), but NOT deadlocked currently")

def test_q11():
    alloc = {
        'P0': [1, 0],
        'P1': [0, 1],
        'P2': [1, 0]
    }
    req_a = {
        'P0': [0, 1],
        'P1': [1, 0],
        'P2': [1, 0]
    }
    avail_a = [0, 0]

    def detect_deadlock(curr_alloc, curr_req, curr_avail):
        work = list(curr_avail)
        finish = {}
        for p in curr_alloc:
            finish[p] = (curr_alloc[p] == [0, 0])
        seq = []
        while True:
            found = False
            for p in curr_alloc:
                if not finish[p]:
                    if curr_req[p][0] <= work[0] and curr_req[p][1] <= work[1]:
                        work[0] += curr_alloc[p][0]
                        work[1] += curr_alloc[p][1]
                        finish[p] = True
                        seq.append(p)
                        found = True
                        break
            if not found:
                break
        deadlocked = [p for p in finish if not finish[p]]
        return seq, deadlocked

    seq_a, dead_a = detect_deadlock(alloc, req_a, avail_a)
    assert dead_a == ['P0', 'P1', 'P2']
    print(f"Q11(a) verified: Deadlock detected, deadlocked processes = {dead_a}")

    req_b = {
        'P0': [0, 1],
        'P1': [1, 0],
        'P2': [0, 0]
    }
    seq_b, dead_b = detect_deadlock(alloc, req_b, avail_a)
    assert dead_b == []
    print(f"Q11(b) verified: No deadlock, completion sequence = {seq_b}")

if __name__ == "__main__":
    test_q1()
    test_q2()
    test_q9()
    test_q10()
    test_q11()
    print("ALL TESTS PASSED SUCCESSFULLY!")
