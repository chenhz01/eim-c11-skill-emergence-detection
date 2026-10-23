# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P42 skill-maturity-grader — 技能涌现检测

L0: 给技能打个成熟度分，知道哪个能放心用。
L1: 按 有文档/有测试/有示例 三维加权打分。
L2: grade(skill) → 0-100。
"""

def grade(skill):
    s = 0
    if skill.get("doc"): s += 40
    if skill.get("tests"): s += 40
    if skill.get("example"): s += 20
    return s

def demo():
    print("[P42]", grade({"doc":1,"tests":1}), grade({"doc":1}))


if __name__ == "__main__":
    demo()
