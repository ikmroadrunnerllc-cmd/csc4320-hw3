# AI Usage Statement & Concept Learning Log

**Student:** Mario Leonel Gutierrez Espinal  
**Course:** CSC 4320 / CSC 6320 - Operating Systems (Fall 2026)  
**Instructor:** Dr. Roya Hosseini  
**Assignment:** Homework 3 (Chapters 3 & 4)  
**Date:** November 8, 2026  

---

## 1. Summary of AI Assistance
An AI assistant was used in an educational, tutoring capacity to explain complex Operating Systems concepts in simple, plain English without heavy jargon. 

The tool acted like a teaching assistant or study partner to help me build intuition for tricky concurrency and deadlock topics before I solved the homework problems myself.

---

## 2. Concepts Explained by AI

### Concurrency vs. Parallelism (Question 1)
- **Concept:** I asked for a simple explanation of why an I/O task and a CPU task running on a single-core machine count as concurrent but not parallel.
- **Tutor Explanation:** Concurrency means juggling multiple tasks in overlapping time windows (making progress on both). Parallelism means literally doing two things at the exact same physical instant (which requires multiple CPU cores). On one core, only one thread uses the CPU at any instant, but overlapping CPU with device I/O is concurrent.

### The Mechanism of Lost Updates (Question 2)
- **Concept:** Understanding how two threads doing additions can overwrite each other.
- **Tutor Explanation:** The AI walked me through the 3-step Read-Modify-Write cycle (`read`, `add`, `write`). It explained that if Thread B reads the balance before Thread A writes back its new sum, Thread B calculates from the old number and completely overwrites Thread A's change.

### Semaphores vs. Mutexes in Bounded Buffers (Question 4)
- **Concept:** Why calling `wait(m)` before `wait(full)` causes a deadlock.
- **Tutor Explanation:** The AI used the analogy of holding the room key while waiting for a package. If the consumer locks the door (`wait(m)`) on an empty buffer, the producer cannot enter the room to deliver the package (`signal(full)`), leaving both stuck forever.

### Condition Variables & While Loops (Question 5)
- **Concept:** Why `while` loops are required with condition variables instead of `if` statements.
- **Tutor Explanation:** In Mesa semantics, when a producer wakes up waiting consumers, another consumer might grab the item first before you reacquire the lock. If you only used `if`, you would try to remove an item from an empty queue and crash. A `while` loop forces the thread to re-check the condition upon waking up.

### Resource Allocation Graphs with Multiple Instances (Question 8)
- **Concept:** Why a cycle does not always mean a deadlock.
- **Tutor Explanation:** A cycle guarantees deadlock only when every resource has exactly 1 instance. If a resource has 2 instances and the other instance is held by an independent process that has no requests, that process will finish, release its resource, break the cycle, and allow everyone else to complete.

### Banker's Algorithm & Unsafe States (Questions 9 & 10)
- **Concept:** The difference between an unsafe state and an actual deadlock.
- **Tutor Explanation:** An unsafe state is not a deadlock yet—it just means the system has no guarantee of avoiding a deadlock if every process suddenly requests its declared maximum. The Banker's Algorithm runs simulated completions to find a safe order before granting requests.

---

## 3. Student Ownership & Verification
- All final written answers, calculations, traces, and pseudocode in `Homework3_Answers.txt` were written and reviewed by me.
- I wrote and ran an automated Python test script (`verify_homework3.py`) to independently verify the timing math, interleaving values, Banker's Algorithm safety vectors, and deadlock detection sets.
