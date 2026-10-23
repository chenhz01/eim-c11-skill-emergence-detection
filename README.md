# C11 · Skill Emergence Detection

> **机制簇**：技能涌现检测 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
你反复写同一套做法，工具帮你发现「这已经算个技能了，抽出来复用」。

**L1 · 机制本质**
从代码/轨迹挖重复模式，聚成候选技能，按复用度与独立性评分，产出候选卡供人工确认。

**L2 · 怎么用上**
pattern-miner 挖模式；skill-clusterer 聚类；reuse-scorer 评分与阈值筛选。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c11-skill-emergence-detection.git && cd eim-c11-skill-emergence-detection
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p40-skill-emergence-scanner/impl.py        # 看 demo 输出
python components/p40-skill-emergence-scanner/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P40` | skill-emergence-scanner | 统计函数名动词前缀频次，频次高的提示可封装技能。 | `components/p40-skill-emergence-scanner/` |
| `P41` | duplicate-skill-detector | Jaccard 相似度超阈值即判近重复。 | `components/p41-duplicate-skill-detector/` |
| `P42` | skill-maturity-grader | 按 有文档/有测试/有示例 三维加权打分。 | `components/p42-skill-maturity-grader/` |
| `P43` | cross-repo-skill-harvester | 按描述关键词聚类，输出能力簇。 | `components/p43-cross-repo-skill-harvester/` |

## 该用 / 不该用 / 常见误用

**该用**
多仓库、多会话的个人或团队知识沉淀；长跑项目的能力盘点。

**不该用**
一次性脚本；代码量极小的项目（样本不足必然误判）。

**常见误用（这条最重要）**
出现两次就判为技能。须过复用阈值与边界检验，否则造出一堆伪技能。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C11 · Skill Emergence Detection © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
