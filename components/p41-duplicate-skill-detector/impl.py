# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P41 duplicate-skill-detector — 技能涌现检测

L0: 两个技能其实干的是同一件事，留着浪费。这个工具找重复。
L1: Jaccard 相似度超阈值即判近重复。
L2: dups(skills, thr) → 重复对。
"""

def _j(a, b):
    A, B = set(a.lower().split()), set(b.lower().split())
    return len(A & B) / max(1, len(A | B))
def dups(skills, thr=0.5):
    out, ks = [], list(skills.items())
    for i in range(len(ks)):
        for j in range(i+1, len(ks)):
            if _j(ks[i][1], ks[j][1]) >= thr:
                out.append((ks[i][0], ks[j][0]))
    return out

def demo():
    print("[P41]", dups({"a":"run tests fast", "b":"run tests quickly", "c":"deploy"}))


if __name__ == "__main__":
    demo()
