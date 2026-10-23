# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P40 skill-emergence-scanner — 技能涌现检测

L0: 代码里反复出现的套路，其实可以打包成一个'技能'。
L1: 统计函数名动词前缀频次，频次高的提示可封装技能。
L2: scan(code) → 候选技能前缀列表。
"""

import ast
def scan(code, top=5):
    from collections import Counter
    c = Counter()
    for n in ast.walk(ast.parse(code)):
        if isinstance(n, ast.FunctionDef):
            c[n.name.split("_")[0]] += 1
    return [k for k, v in c.most_common(top) if v >= 2]

def demo():
    src = "def parse_a(): pass\ndef parse_b(): pass\ndef run_x(): pass\n"
    print("[P40]", scan(src))


if __name__ == "__main__":
    demo()
