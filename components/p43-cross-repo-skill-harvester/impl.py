# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P43 cross-repo-skill-harvester — 技能涌现检测

L0: 横扫很多仓库，把能复用的能力捞出来。
L1: 按描述关键词聚类，输出能力簇。
L2: harvest(repo_descs) → {keyword: [repos]}。
"""

def harvest(repo_descs, keys=("parse","render","deploy","test","scan")):
    out = {k: [] for k in keys}
    for name, d in repo_descs.items():
        for k in keys:
            if k in d.lower(): out[k].append(name)
    return {k: v for k, v in out.items() if v}

def demo():
    print("[P43]", harvest({"r1":"fast parser","r2":"image render","r3":"parser & render"}))


if __name__ == "__main__":
    demo()
