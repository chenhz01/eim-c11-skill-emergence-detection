# P41 · duplicate-skill-detector

> 机制簇：**技能涌现检测** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
两个技能其实干的是同一件事，留着浪费。这个工具找重复。

**L1 · 机制本质**
Jaccard 相似度超阈值即判近重复。

**L2 · 怎么用上**
dups(skills, thr) → 重复对。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P41] [('a', 'b')]
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 大代码库、多轮运行日志、需要把重复解法沉淀为可复用能力。 |
| **不该用** | 一次性脚本、无重复模式的探索性代码。 |
| **常见误用** | 把重复代码直接当技能——未抽象就封装，等于把负债固化成 API。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P40` skill-emergence-scanner · `P42` skill-maturity-grader · `P43` cross-repo-skill-harvester
- 本仓是 **P41 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P41-duplicate-skill-detector/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P41 · duplicate-skill-detector © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
