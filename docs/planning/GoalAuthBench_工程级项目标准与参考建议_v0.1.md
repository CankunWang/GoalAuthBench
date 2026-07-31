# GoalAuthBench 工程级项目标准与参考建议

> 版本：v0.1  
> 日期：2026-07-28  
> 状态：项目启动基线 / 新会话执行参考  
> 适用范围：GoalAuthBench 的代码、数据、实验、文档、AI Agent 协作、代码审查和公开发布  
> 当前研究计划：[GoalAuthBench v0.2](../../GoalAuthBench_v0.2_重审执行版_2026-07-27.md)
> 当前研究审计：[整体方案重审报告](../archive/GoalAuthBench_整体方案重审报告_2026-07-27.md)
> 当前安全与标签基线：[威胁模型](../research/threat-model.md) /
> [标签指南](../research/label-guide.md) /
> [ADR-0001](../adr/0001-t2-precommit-boundary.md) /
> [ADR-0002](../adr/0002-explicit-vs-implicit-authorization.md)

---

## 0. 本文件如何使用

本文件定义 GoalAuthBench 从“研究方案”进入“可运行、可审查、可复现、可公开发布的研究工程项目”时必须遵守的最低标准。

在新的 Codex 会话中，应先要求 Agent：

1. 完整阅读本文件；
2. 完整阅读 GoalAuthBench v0.2；
3. 阅读整体方案重审报告；
4. 检查仓库当前状态；
5. 只执行当前里程碑，不擅自扩展研究范围；
6. 在修改代码前列出计划、影响文件、验收命令和风险；
7. 完成修改后运行验证并报告真实结果。

本文件中的规范词含义如下：

- **必须（MUST）**：不满足时不得视为完成；
- **禁止（MUST NOT）**：违反后必须停止、回退或修复；
- **应该（SHOULD）**：除非有记录在案的理由，否则必须执行；
- **可以（MAY）**：可选增强项，不得阻塞核心版本；
- **质量门（Gate）**：只有全部通过，才允许进入下一阶段。

本标准不是为了增加文档数量，而是为了防止以下问题：

- AI Agent 生成大量代码但无法验证；
- 研究标签和授权语义在实现中被悄悄改变；
- 数据泄漏导致虚假的高分；
- teacher-forced 结果被包装成端到端防御；
- 多 Agent 并行修改导致冲突和责任不清；
- 实验无法根据代码、配置、模型和数据重新运行；
- 公开仓库只有漂亮 README，没有可信证据。

---

## 1. 参考项目与采用策略

### 1.1 工程母版：Inspect AI

主要参考：

- [Inspect AI GitHub 仓库](https://github.com/UKGovernmentBEIS/inspect_ai)
- [Inspect AI AGENTS.md](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/AGENTS.md)
- [Inspect AI CONTRIBUTING.md](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/CONTRIBUTING.md)
- [Inspect AI pre-commit 配置](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/.pre-commit-config.yaml)

采用其以下原则：

- `src/` 布局；
- 测试、文档、设计说明和实现分离；
- `pyproject.toml` 与锁文件；
- 统一的格式化、lint、类型检查和测试命令；
- 简洁、持久的 `AGENTS.md`；
- PR 模板与 CHANGELOG 纪律；
- public API 类型和文档要求；
- 设计文档作为复杂子系统的事实来源；
- CI 与本地命令一致。

不直接照搬：

- TypeScript 前端与 Git submodule；
- S3/GCS/Azure 多后端文件系统；
- asyncio/trio 双运行时；
- 大型团队的复杂 requirements 分层；
- 与 GoalAuthBench 无关的 UI 和发布基础设施。

### 1.2 领域母版：AgentDojo

主要参考：

- [AgentDojo GitHub 仓库](https://github.com/ethz-spylab/agentdojo)
- [AgentDojo 论文](https://arxiv.org/abs/2406.13352)

采用其以下原则：

- Agent、task、tool、attack、defense 和 scorer 的领域抽象；
- 环境状态作为可验证结果；
- benchmark CLI；
- suite/task/security case 的组织方式；
- 运行结果与实验配置分离；
- 公开 benchmark、代码、文档和引用材料共同发布。

不直接照搬：

- 将 AgentDojo state scorer 当作 authorization oracle；
- 在未冻结兼容版本前绑定其不稳定 API；
- 一开始覆盖全部 suite；
- 直接修改上游对象以适配本项目，而不建立 adapter 边界。

### 1.3 安全工程基线：OpenSSF

主要参考：

- [OpenSSF Best Practices Badge](https://openssf.org/projects/best-practices-badge/)
- [OpenSSF Best Practices Working Group](https://best.openssf.org/)
- [OpenSSF 开源软件评估简明指南](https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software.html)

GoalAuthBench v1 以 OpenSSF Passing / Baseline-1 的精神为最低目标：

- 有版本控制；
- 有许可证；
- 有安全问题报告方式；
- 有自动化测试和 CI；
- 新功能必须有测试；
- 管理依赖和已知漏洞；
- 验证不可信输入；
- 不提交密钥；
- 有明确的发布和变更记录；
- 对外部贡献提供可执行说明。

首版不要求：

- OpenSSF Gold；
- 两名以上长期独立维护者；
- 复杂软件供应链签名系统；
- 企业级合规证明。

### 1.4 GoalAuthBench 自有标准

Inspect AI、AgentDojo 和 OpenSSF 都不能替代本项目特有的研究完整性要求。

本项目必须额外保证：

- authorization、state 和 utility oracle 分离；
- exact candidate action 的规范化控制；
- operational provenance 与 visible source claim 分离；
- lineage-aware split；
- matched design 的成对统计；
- T0/T1/T2/T3 时间边界不混淆；
- latent 方法只作为条件性扩展；
- 正负结果都可发布；
- 不使用超出证据的创新表述。

---

## 2. 项目范围与非目标

### 2.1 v1 必须范围

v1 只包含：

- Workspace/Email 类型场景；
- 两个副作用工具；
- 6 个 golden matched groups；
- 20 个 smoke groups；
- 60–100 个 pilot base scenario groups；
- A/U/AE/UC 四臂数据；
- canonical action 和 exact argument validator；
- authorization、state、utility 三类 oracle；
- B0–B5 non-latent baseline；
- 一个预注册 grouped OOD；
- T2 policy-first pre-commit gate；
- 30–50 个 natural rollout 场景；
- 可选 selected-layer hidden-state probe；
- 数据、测试、CI、报告、失败案例和版本化 release。

### 2.2 v1 明确不做

未经 scope-change ADR 批准，禁止加入：

- MCP gateway；
- 四个 AgentDojo suite；
- 2,000 条 trajectory；
- 完整交互式 viewer；
- EN/ZH/code-switch 十二条件矩阵；
- 14B hidden-state 主实验；
- 跨 CUDA/MLX activation 混合；
- 多 Agent RL jailbreak；
- v1 主评测中的任何 adaptive attack；adaptive 仅允许使用独立后续协议；
- 多模态主实验；
- 把 learned detector 作为唯一授权边界。

### 2.3 范围变更

任何范围扩展必须：

1. 新建 ADR；
2. 说明它对应哪个研究问题；
3. 说明为何不能推迟到 v2；
4. 估算时间、GPU、API 和维护成本；
5. 说明会删除或推迟哪个现有工作；
6. 经项目负责人明确批准。

不得只增加范围而不减少其他工作。

---

## 3. 仓库结构标准

推荐结构：

```text
goal-auth-bench/
├─ AGENTS.md
├─ README.md
├─ ROADMAP.md
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ LICENSE
├─ CHANGELOG.md
├─ CITATION.cff
├─ pyproject.toml
├─ uv.lock
├─ .python-version
├─ .gitignore
├─ .pre-commit-config.yaml
├─ .github/
│  ├─ workflows/
│  │  └─ ci.yml
│  ├─ pull_request_template.md
│  └─ ISSUE_TEMPLATE/
├─ docs/
│  ├─ planning/
│  ├─ research/
│  │  ├─ threat-model.md
│  │  ├─ research-protocol.md
│  │  ├─ label-guide.md
│  │  ├─ data-card.md
│  │  ├─ model-card.md
│  │  └─ novelty-matrix.md
│  ├─ design/
│  │  ├─ architecture.md
│  │  ├─ canonicalization.md
│  │  ├─ authorization-oracle.md
│  │  └─ t2-gate.md
│  ├─ adr/
│  │  ├─ 0001-t2-precommit-boundary.md
│  │  ├─ 0002-explicit-vs-implicit.md
│  │  ├─ 0003-primary-endpoint-and-split.md
│  │  └─ 0004-canonical-action-semantics.md
│  └─ status.md
├─ src/
│  └─ goalauthbench/
│     ├─ schema/
│     ├─ canonicalize/
│     ├─ policy/
│     ├─ provenance/
│     ├─ oracles/
│     ├─ datasets/
│     ├─ adapters/
│     │  └─ agentdojo/
│     ├─ baselines/
│     ├─ probes/
│     ├─ gate/
│     ├─ metrics/
│     └─ tracing/
├─ tests/
│  ├─ unit/
│  ├─ golden/
│  ├─ property/
│  ├─ integration/
│  └─ smoke/
├─ data/
│  ├─ schemas/
│  ├─ golden/
│  ├─ smoke/
│  └─ samples/
├─ configs/
│  ├─ models/
│  ├─ experiments/
│  └─ policies/
├─ manifests/
├─ scripts/
└─ reports/
   ├─ figures/
   ├─ tables/
   └─ error_gallery/
```

### 3.1 目录责任

- `src/`：可安装、可测试、可复用的产品代码；
- `scripts/`：薄入口，不得承载无法测试的核心逻辑；
- `tests/`：自动化验证；
- `data/`：小型公开数据、schema 和 fixture；
- `manifests/`：正式实验的不可变运行说明；
- `configs/`：可复用配置；
- `reports/`：生成结果或发布材料；
- `docs/research/`：研究真值、协议和限制；
- `docs/design/`：工程设计；
- `docs/adr/`：重大决策和变更理由。

禁止将核心业务逻辑长期保留在 notebook。

Notebook 可以用于探索，但正式结果必须由脚本或 CLI 复现。

---

## 4. 事实来源与文档优先级

发生冲突时按以下顺序处理：

```text
已批准 ADR
> research-protocol / label-guide / threat-model
> 当前 v0.2 执行计划
> AGENTS.md
> design docs
> README / ROADMAP
> 历史初版方案
> 对话中的临时表述
```

说明：

- `AGENTS.md` 管理 Agent 行为，不定义研究真值；
- `label-guide.md` 定义标签，不允许代码自行推断新规则；
- `research-protocol.md` 定义主假设、主指标和主 split；
- `status.md` 记录当前进度，不替代设计文档；
- 对话不是持久事实来源；
- 历史方案不得覆盖当前 v0.2 或后续 ADR。

---

## 5. 开发环境与依赖标准

### 5.1 Python 与平台

- canonical 开发平台应该是 WSL2/Linux；
- Windows 可用于编辑、轻量测试和 Codex；
- CUDA 实验记录驱动、CUDA、PyTorch 和 GPU 信息；
- Python 版本必须在 AgentDojo compatibility smoke test 后锁定；
- 初始候选为 Python 3.11，不得在未验证时宣称最终版本；
- macOS/MLX 与 CUDA 环境必须使用不同 manifest；
- 不得混合不同 backend 的 raw activation。

### 5.2 依赖管理

必须使用：

- `pyproject.toml`：项目和工具配置；
- `uv.lock`：可复现开发依赖；
- `uv`：本地依赖安装和命令运行。

必须提供：

```bash
uv sync --all-extras
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run pyright
```

应该提供一个统一命令：

```bash
uv run poe verify
```

或：

```bash
make verify
```

统一验证必须至少运行：

1. formatting check；
2. lint；
3. type check；
4. unit/golden tests；
5. 快速数据 validator；
6. secret scan 或等价检查。

### 5.3 依赖变更

依赖变更必须：

- 有明确用途；
- 更新锁文件；
- 记录许可证或安全风险；
- 通过完整测试；
- 不引入无必要的大型框架；
- 不因一个小功能引入完整 Agent framework；
- 不提交模型权重或大型缓存。

---

## 6. 编码标准

### 6.1 格式与静态检查

建议工具：

- Ruff：format + lint；
- Pyright：类型检查；
- Pytest：测试；
- Hypothesis：property-based testing；
- pytest-cov：覆盖率；
- pip-audit：依赖漏洞检查；
- pre-commit：提交前检查。

### 6.2 类型

必须：

- public API 有完整类型；
- schema、policy、oracle、canonicalization 和 gate 使用严格类型；
- 避免含义不清的裸 `dict[str, Any]`；
- 关键 ID 使用明确类型或轻量 wrapper；
- 多个同类型返回值使用 dataclass、NamedTuple 或结构化模型；
- `SUPPORTED | UNSUPPORTED | AMBIGUOUS`、`PERMIT | DENY | CONFIRM_REQUIRED | NO_MATCH | INVALID` 和 `COMMIT | BLOCK | WOULD_CONFIRM` 分别使用独立枚举；
- 时间、金额、资源 ID、邮箱和 canonical digest 有明确表示。

允许：

- 在第三方库边界做局部 `Any`；
- 使用明确注释的类型忽略。

禁止：

- 为通过类型检查大面积使用 `# type: ignore`；
- 用 boolean 同时表示授权、成功和安全；
- 用空字符串或 `None` 隐式表达多个安全状态。

### 6.3 函数与模块

- 一个模块应有单一职责；
- 核心逻辑必须可独立测试；
- CLI、adapter 和框架 glue 不应承载研究逻辑；
- public API 必须有 docstring；
- 异常必须带上下文；
- 安全失败不得静默降级；
- 不用日志代替结构化返回结果；
- 不在 import 时执行模型下载、API 调用或环境修改。

### 6.4 配置

- 配置必须结构化并可校验；
- 正式实验不得依赖散落的环境默认值；
- secrets 只从环境或 secret manager 读取；
- 配置文件不得包含真实 API key；
- 所有默认值必须在 manifest 中解析为最终值；
- 同一实验重跑时必须能得到完整 resolved config。

---

## 7. 安全架构不变量

以下规则任何实现都不得违反。

### 7.1 信任边界

- LLM 是不可信 proposal generator；
- 不可信网页、邮件、文档、RAG chunk 和 tool output 不能签发权限；
- 正文中的 `TRUSTED`、签名外观或来源自述不产生授权；
- operational provenance 只能由 trusted host 绑定；
- PEP 持有真实凭据；
- PEP 是所有副作用工具唯一 dispatch 路径；
- executor 只执行已经 commit 的 canonical manifest。

### 7.2 T2 gate

```text
T0  外部内容读取完成
T1  tool name 已生成
T2  完整 tool call 已缓冲、解析并 canonicalize
    <- 主 gate；尚未执行
T3  工具执行后
```

必须：

- 完整缓冲 tool call；
- 解析和 canonicalize；
- 生成绑定完整 authorization envelope 的 digest；
- 执行 deterministic policy；
- 再运行可选 learned risk；
- 只有 structured `PERMIT` 可以 `COMMIT`；
- `DENY`、`NO_MATCH` 和 `INVALID` 永不 dispatch；
- approved envelope digest 与实际 dispatch 完全相同；
- 记录 state diff 和 audit event。

authorization envelope 至少绑定：

```text
tool + complete canonical arguments
+ execution account
+ principal/user + session
+ policy identifier/version
+ operational provenance
+ capability/quota
+ schema/canonicalization version
+ nonce + expiry + idempotency key
```

授权检查、额度/nonce 预留、审计意图和 dispatch authorization 使用：

```text
CHECKED -> PREPARED -> DISPATCHING -> COMMITTED | FAILED | UNKNOWN
```

只有 `PREPARED` envelope 可以进入 executor。所有副作用工具必须登记 policy、
canonicalizer、PEP route、evidence collector 和幂等/恢复行为；新增工具缺少任一项时
CI 必须失败。

禁止：

- 在完整参数未知时声称 exact-effect authorization；
- 使用 T2 后 token 声称 T0/T1 检测；
- learned detector 覆盖明确 DENY；
- 让模型直接接触真实凭据；
- 绕过 PEP 调用副作用工具。

v1 资源保护只覆盖邮件次数、事件次数、外部参加者数量、`max_calls` 和 policy 声明的
业务额度。CPU、内存、磁盘、网络饱和与宿主资源耗尽不在 v1 范围。

### 7.3 失败策略

以下任一失败都产生 `INVALID -> BLOCK`：

- 解析失败；
- schema 不兼容；
- canonicalization 不确定；
- identity/resource alias 无法解析；
- nonce 无效；
- policy version 不一致；
- digest 不一致；
- TTL 过期；
- replay；
- provenance 不完整。

只有结构化 policy 明确返回 `CONFIRM_REQUIRED` 时才能产生 `WOULD_CONFIRM`。语义
`AMBIGUOUS`、解析失败或 canonicalization 不确定本身不能进入确认路径。

---

## 8. 研究完整性标准

### 8.1 三类 oracle 分离

必须分别实现和报告：

```text
Authorization oracle：动作是否被允许
State oracle：环境是否发生目标或危险变化
Utility oracle：用户任务是否完成
```

禁止：

- 用 state scorer 代替 authorization oracle；
- 用任务成功代表安全；
- 用没有攻击结果代表动作已授权；
- 用 LLM 自述理由作为真值。

安全结果与实验有效性必须正交：

```text
security_outcome:    PASS | FAIL | NOT_EVALUABLE
experiment_validity: VALID | INVALID
```

非 `PERMIT` 动作被执行、绕过 PEP、执行 envelope 被篡改或部分准备状态进入 executor
属于安全失败。数据污染、lineage 泄漏、三类 oracle/标签混用、证据缺失或冻结协议被
破坏属于实验无效。两者可以同时发生，实验无效不得掩盖安全失败。

### 8.2 显式与隐式授权分离

必须保存三个独立结果：

```text
delegation_label:
  SUPPORTED | UNSUPPORTED | AMBIGUOUS

policy_decision:
  PERMIT | DENY | CONFIRM_REQUIRED | NO_MATCH | INVALID

gate_decision:
  COMMIT | BLOCK | WOULD_CONFIRM
```

`delegation_label` 不直接控制执行。只有 `PERMIT` 可以 `COMMIT`。

Track E：

- 结构化 policy 提供真值；
- deterministic policy 是主方法；
- latent 只作诊断；
- 明确 DENY 不能被覆盖。

Track I：

- 自然语言委托；
- 使用 `SUPPORTED | UNSUPPORTED | AMBIGUOUS`；
- 允许 `SUPPORTED + NO_MATCH + BLOCK`；
- 保存 authorization witness；
- 第二位盲标者复核 20%–30%；
- 不一致样本必须记录和裁决。

### 8.3 数据四臂

同一个 canonical candidate action 构造：

- `A`：`SUPPORTED + PERMIT + COMMIT`；
- `U`：`UNSUPPORTED + DENY + BLOCK`；
- `AE`：结构化授权覆盖外部字段选择，`SUPPORTED + PERMIT + COMMIT`；
- `UC`：无典型注入措辞的未授权操纵，`UNSUPPORTED + DENY + BLOCK`。

Track I 的语义样本可以是 `SUPPORTED + NO_MATCH + BLOCK`。完整标签、reason code、
witness 和裁决规则以 [label guide](../research/label-guide.md) 为准。

每个 group 必须通过：

```text
[ ] canonical tool name 一致
[ ] typed exact arguments 一致
[ ] initial environment state 一致
[ ] canonical digest 一致
[ ] authorization witness 存在
[ ] provenance chain 可解析
[ ] lineage 完整
[ ] split 无泄漏
[ ] nuisance 差异已登记
[ ] 三层结果分开保存
[ ] AMBIGUOUS delegation 未被强制二值化
```

### 8.4 来源控制

Operational source authority 与 visible source claim 必须正交：

| Operational authority | Visible claim | 用途 |
| --- | --- | --- |
| trusted | claims trusted | 普通可信 |
| trusted | claims untrusted / none | 检查文字外观捷径 |
| untrusted | claims trusted | 伪造来源攻击 |
| untrusted | claims untrusted / none | 普通不可信 |

### 8.5 Split 与 lineage

独立单位是 `base_scenario_id`。

以下派生项必须在同一 split：

- A/U/AE/UC；
- paraphrase；
- translation；
- template variants；
- 同一 AgentDojo task；
- 同一 attacker goal；
- 同一生成器 lineage；
- 相同 canonical action 的直接派生。

禁止：

- sample-level random split 作为唯一结论；
- 将派生 trajectory 当作独立样本；
- 在 test set 调 threshold；
- 看到结果后无记录地改变 primary split。

### 8.6 预注册与结论

数据冻结前必须记录：

- primary hypothesis；
- primary endpoint；
- primary split；
- calibration 方法；
- bootstrap 单位；
- exclusion 规则；
- invalid run 处理；
- latent continuation gate。

必须区分：

- confirmatory；
- secondary；
- exploratory；
- post-hoc。

禁止：

- random 到 OOD 下降自动解释为 shortcut；
- 线性可解码解释为因果机制；
- teacher-forced AUC 解释为端到端安全；
- 使用 `first` 而没有系统性查重；
- 只发布正结果。

---

## 9. 数据、Schema 与 Canonicalization 标准

### 9.1 Schema

核心 schema 至少包括：

- `CanonicalAction`；
- `AuthorizationWitness`；
- `ProvenanceRef`；
- `AuthzManifest`；
- `ScenarioLineage`；
- `OracleResult`；
- `GateDecision`；
- `AuditEvent`；
- `ExperimentManifest`。

Schema 必须：

- 有显式版本；
- 可序列化；
- 有向前/向后兼容策略；
- 有 golden fixture；
- 拒绝未知危险字段或明确记录处理；
- 不能依赖 Python 对象地址或非确定性顺序。

### 9.2 Canonicalization

不能只比较 JSON 字节串。

必须考虑：

- 默认值；
- Unicode normalization；
- 大小写；
- 邮箱和身份别名；
- URL；
- 文件路径；
- 日期与时区；
- 数值、货币和精度；
- argument 顺序；
- nested object；
- schema version；
- 空值与缺失值；
- 多收件人顺序或集合语义。

无法安全规范化时：

- 产生 `INVALID -> BLOCK`；
- 必须记录原因。

### 9.3 数据发布

公开数据不得包含：

- 真实 PII；
- 真实凭据；
- 商业 API 响应中的受限数据；
- HTB COAE 题目、flag 或受限材料；
- 未披露漏洞的可直接利用细节；
- 未授权转载的数据集内容。

数据 release 必须包含：

- schema version；
- checksum；
- data card；
- license；
- generation lineage；
- known limitations；
- label audit；
- split definition；
- 示例加载代码。

---

## 10. 测试标准

### 10.1 测试层级

#### Unit tests

覆盖：

- schema；
- canonicalization；
- policy；
- provenance；
- oracle；
- metrics；
- cost accounting；
- config parsing。

#### Golden tests

覆盖：

- 6 个手工可验证 matched groups；
- exact comparator；
- authorization witness；
- gate decision；
- state diff；
- 手算指标。

#### Property tests

重点用于：

- JSON key reorder 不改变 digest；
- 等价 Unicode/地址规范化行为；
- canonicalization idempotence；
- serialize/deserialize round trip；
- approved action 修改任一安全关键字段后 digest 必须变化；
- nonce 不可重复消费；
- lineage split 永不拆分 group。

#### Integration tests

覆盖：

- proposal → buffer → parse → canonicalize → gate → executor；
- fake attack → BLOCK；
- structured PERMIT → COMMIT；
- malformed high-risk action → fail-closed；
- trace → state diff；
- AgentDojo adapter。

#### Smoke tests

必须：

- 不依赖 API 的 CI smoke；
- 一个可选 API smoke，默认不在 fork PR 运行；
- 一个本地小模型 smoke，允许单独标记；
- 固定超时；
- 不自动下载超大模型。

### 10.2 覆盖率

初始建议：

- 全项目 statement coverage 目标 ≥80%；
- security-critical modules 目标 ≥90%；
- branch coverage 应重点关注 canonicalization、policy、gate 和 oracle；
- 覆盖率不能替代 golden、property 和 adversarial tests。

未达到目标不一定阻塞最早期 prototype，但 v1 release 前必须：

- 达到目标；或
- 在 release notes 中逐项解释缺口。

### 10.3 测试真实性

禁止：

- 只测试 happy path；
- mock 掉真正需要验证的安全边界；
- 使用实现自身计算的值作为 expected value；
- 为让 CI 通过而无说明地 skip；
- 丢弃安全失败或 invalid runs；
- 用实验无效掩盖、删除或重标安全失败；
- 在线测试依赖浮动模型别名而无 snapshot 记录。

---

## 11. 实验与复现标准

### 11.1 每次正式实验必须有 manifest

最低字段：

```text
experiment_id
created_at
git_commit
dirty_worktree
code_version
schema_version
dataset_name
dataset_hash
split_id
split_hash
model_provider
model_name
model_snapshot
tokenizer
chat_template_hash
backend
quantization
device
cuda_or_mlx_version
seed
prompt_hash
policy_version
threshold_source
max_episodes
max_tokens
max_retries
budget_limit
wall_clock_limit
output_path
```

### 11.2 正式实验前

必须：

- 工作树干净，或记录 dirty diff；
- 配置解析成功；
- 数据 hash 固定；
- calibration 完成；
- 预算和超时存在；
- 先运行小规模 smoke；
- 输出目录不覆盖已有实验；
- 保存 stdout/stderr 或结构化事件。

### 11.3 正式实验后

必须保存：

- per-sample prediction；
- oracle result；
- gate decision；
- invalid/failure reason；
- latency；
- token/cost；
- environment diff；
- aggregate metrics；
- bootstrap samples 或可重算输入；
- resolved config；
- manifest；
- 代码 commit。

### 11.4 结果生成

- 表格和图必须从保存的逐样本结果自动生成；
- 不允许手工修改最终数字；
- 图表脚本必须版本化；
- 报告必须能追溯到 experiment ID；
- exploratory 结果必须标记；
- 重新运行产生变化时必须解释。

---

## 12. Code Review 标准

### 12.1 两类 Review

#### 工程正确性 Review

检查：

- bug；
- 类型；
- 边界条件；
- 异常；
- 性能；
-测试；
-兼容性；
-安全边界；
-真实副作用风险。

#### 科学有效性 Review

检查：

- 标签语义；
- future-token leakage；
- lineage leakage；
- baseline 公平性；
-统计独立单位；
- threshold 调节；
- teacher-forced/natural rollout 区分；
-结论是否超出证据；
-失败样本是否被选择性排除。

### 12.2 强制独立 Review 的模块

以下变更必须由独立 reviewer 或只读 Review Agent 检查：

- `canonicalize/`；
- `policy/`；
- `gate/`；
- `oracles/`；
- split 和 lineage；
- metrics/statistics；
- schema；
- labels；
- research protocol；
- CI/release；
- secrets/credentials handling。

### 12.3 PR 规模

建议：

- 单个 PR 只解决一个问题；
- 有效逻辑约 300–500 行以内；
- 生成文件、fixture 和测试可单独计算；
- 大变更拆成 schema、implementation、integration 三步；
- 禁止将大规模格式化与功能修改混在一起。

### 12.4 PR 必须包含

```text
问题与目标
范围
明确不做
当前行为
新行为
安全/研究影响
修改文件
测试证据
已知限制
是否改变 schema
是否改变 label/policy
是否改变 primary protocol
回滚方式
```

### 12.5 Review 完成条件

- 所有阻塞意见已解决；
- 测试重新运行；
- CI 通过；
- 文档与实现一致；
- 无未解释的 skip；
- 无未登记的实验语义变化；
- 项目负责人能解释核心代码；
- Agent Review 不替代人工研究语义确认。

---

## 13. AI Agent 与多 Agent 协作标准

### 13.1 主原则

- 项目负责人拥有研究语义和最终决策；
- Agent 可以实现、测试、审查和整理；
- Agent 不得自行签发授权真值；
- Agent 不得自行改变 label、policy、primary metric 或 split；
- 所有持久规则写入仓库，不只留在对话中；
- Agent 输出必须附验证证据。

### 13.2 推荐角色

| 角色 | 责任 | 默认写权限 |
| --- | --- | --- |
| 主 Agent | 计划、实现、整合、验收 | 有 |
| Research Auditor | prior art、创新表述、引用状态 | 无 |
| Security Reviewer | trust boundary、PEP、TOCTOU、fail-closed | 无 |
| Statistical Reviewer | split、bootstrap、metrics、功效 | 无 |
| Reproduction Agent | 干净环境运行、复现文档 | 有限 |

### 13.3 允许并行的工作

优先并行：

- 文献核查；
- 仓库探索；
- 测试运行；
- 日志分析；
- 只读 code review；
- 统计公式核验；
- 文档一致性检查；
- clean-room reproduction。

谨慎并行：

- 多个相互独立模块；
- 不同 worktree 中的明确任务；
- 有清晰接口和合并顺序的实现。

禁止：

- 两个 Agent 同时修改同一文件；
- 两个 Agent 同时修改同一 schema；
- reviewer 一边审查一边无授权修改；
- 子 Agent 改标签；
- 多 Agent 结果未经主 Agent 整合直接发布；
- 使用更多 Agent 代替明确任务拆分。

### 13.4 子 Agent 任务格式

每个子任务必须明确：

```text
目标
输入
允许读取
允许修改
禁止修改
交付物
验证方法
停止条件
是否需要写文件
```

### 13.5 对话管理

主会话保留：

- 范围；
- 决策；
- go/no-go；
-里程碑；
-最终验收；
-证据路径。

子 Agent 承担：

- 大量日志；
-探索过程；
-独立审查；
-批量分析。

每个里程碑结束更新 `docs/status.md`，至少包括：

- 已完成；
- 证据路径；
- 当前阻塞；
- 下一步；
- 最后验证命令；
- 最后验证 commit；
- 已知风险。

---

## 14. AGENTS.md 标准

根目录必须有 `AGENTS.md`。

它应该保持精简，建议包含：

1. source of truth；
2. v1 scope；
3. research integrity invariants；
4. security invariants；
5. build/lint/test commands；
6. completion requirements；
7. review requirements；
8. 禁止 Agent 自行执行的动作。

不应该包含：

- 全部论文综述；
- 全部项目历史；
- 大段教程；
- 完整 API 文档；
- 每次任务的临时状态；
- 与当前代码无关的个人偏好。

可以在特定目录增加嵌套 `AGENTS.md`：

- `data/AGENTS.md`：标签和数据修改规则；
- `src/goalauthbench/canonicalize/AGENTS.md`：canonicalization 安全规则；
- `experiments/AGENTS.md`：正式实验和预算规则。

只有在规则稳定且目录复杂度足够时才增加，避免第一天过度配置。

---

## 15. CI、分支与提交标准

### 15.1 分支

建议：

- `main` 始终可运行；
- 每个任务使用短分支；
- 分支名描述问题；
- 不在 main 直接进行大规模实验性修改；
- 合并前同步 base。

### 15.2 Commit

每个 commit 应：

- 单一目的；
- 信息清晰；
- 不包含密钥；
- 不包含大模型权重；
- 不包含缓存和临时结果；
- 测试通过或明确标记 work-in-progress；
- 不混合无关格式化。

### 15.3 CI 最低矩阵

首版：

- Ubuntu；
- canonical Python 版本；
- Ruff format check；
- Ruff lint；
- Pyright；
- unit/golden/property tests；
- fast integration tests；
- data/schema validator；
- dependency audit；
- secret scan。

后续可选：

- Windows smoke；
- 多 Python 版本；
- WSL/CUDA self-hosted smoke；
- package build；
- documentation build；
- OpenSSF Scorecard。

### 15.4 外部 API

- 默认 CI 不调用付费 API；
- API tests 使用显式 label 或手动 workflow；
- fork PR 不访问 secrets；
- 记录模型 snapshot；
- 设置 token、retry 和费用上限；
- API 不可用不得阻塞核心离线测试。

---

## 16. 文档标准

### 16.1 README 首屏

15 秒内回答：

```text
Same candidate tool call.
Different authorization context.
Which monitors still work?
```

首屏应该包含：

- 一句话问题；
- A/U/AE/UC 简图；
- 当前状态；
- 60 秒 quickstart；
- 主要结果或“尚无结果”；
- 数据、报告、release 链接；
- 限制；
- 不夸大的贡献声明。

开发早期必须明确：

> This repository is under active development and does not yet contain validated security results.

### 16.2 必须文档

v1 前至少：

- README；
- CONTRIBUTING；
- SECURITY；
- LICENSE；
- CHANGELOG；
- CITATION；
- threat model；
- label guide；
- data card；
- model card；
- research protocol；
- architecture；
- failure/error gallery；
- reproduction guide。

### 16.3 文档真实性

禁止：

- 用计划时态伪装已完成功能；
- 在没有实验时填写 X/Y/Z 成果数字；
- 把预印本写成正式录用；
- 用 stars 作为质量证明；
- 隐藏 negative result；
- 声称彻底解决 prompt injection；
- 不加限定地使用“首个”。

---

## 17. 发布标准

### 17.1 Release 必须包含

- tag；
- changelog；
- fixed manifest；
- 可复现命令；
- 环境说明；
- 数据/模型/config hash；
- 结果摘要；
- 已知限制；
- 至少一个失败案例；
- 成本与硬件；
- migration notes（若 schema 改变）。

### 17.2 版本节奏

建议：

| 版本 | 内容 |
| --- | --- |
| `v0.1.0` | golden schema、validator、fake executor、T2 smoke |
| `v0.2.0` | AgentDojo adapter、20-group smoke |
| `v0.3.0` | 60–100 group pilot |
| `v0.4.0` | B0–B5 non-latent audit |
| `v0.5.0` | 可选 latent audit |
| `v0.6.0` | T2 natural rollout |
| `v1.0.0` | 数据、报告、DOI、复现和 demo |

### 17.3 v1 发布质量门

必须：

- 安装成功；
- 离线 quickstart 成功；
- CI 通过；
- clean-room reproduction；
- 数据和 schema 固定；
- baseline 公平；
- grouped OOD 和 CI 正确；
- T2 gate 真正在 commit 前；
- 安全、utility、latency、cost 同时报；
- 失败和限制公开；
- 无真实凭据/PII；
- 项目负责人可独立解释。

---

## 18. 分阶段工程质量门

### Gate 0：仓库启动

```text
[ ] 独立 Git 仓库
[ ] AGENTS.md
[ ] README 明确开发中
[ ] LICENSE 决策
[ ] pyproject.toml
[ ] uv.lock
[ ] 基础 CI
[ ] threat model
[ ] research protocol
[ ] label guide
[ ] ADR-0001/0002/0003
```

### Gate 1：Golden proof

```text
[ ] 6 个 golden groups
[ ] CanonicalAction
[ ] AuthorizationWitness
[ ] ProvenanceRef
[ ] exact comparator
[ ] pair validator
[ ] lineage validator
[ ] fake executor
[ ] T2 buffer/commit
[ ] 明确 DENY 永不 commit
[ ] 指标与手算一致
[ ] 无 API 一键 smoke
```

### Gate 2：AgentDojo feasibility

```text
[ ] 固定 AgentDojo 版本
[ ] adapter 边界清晰
[ ] 20 smoke groups
[ ] 三类 oracle 分离
[ ] trace manifest
[ ] valid tool call ≥70%，或记录失败
[ ] 简单 clean task success 约 ≥40%–50%，或转 teacher-forced
```

### Gate 3：Pilot data

```text
[ ] 60–100 independent groups
[ ] A/U/AE/UC
[ ] 20%–30% 第二盲标
[ ] lineage-aware split
[ ] 0 family leakage
[ ] 每条有 witness
[ ] ambiguous <15%，否则收缩范围
[ ] nuisance baseline 未轻易饱和 hard subset
```

### Gate 4：Non-latent audit

```text
[ ] B0–B5
[ ] primary grouped OOD
[ ] paired/cluster bootstrap
[ ] calibration fold
[ ] 失败案例
[ ] 成本和 latency
[ ] 区分 distribution shift 与 shortcut
```

### Gate 5：Latent continuation

只有同时满足才继续：

```text
[ ] strongest non-latent 已完成
[ ] hard subset 未被简单 baseline 饱和
[ ] latent 增量 3–5 个百分点
[ ] 增量 CI 下界 > 0
[ ] within-pair ranking CI 下界 > 0.5
[ ] 两个 held-out 维度或模型方向一致
```

不满足时发布负结果，不强行继续。

### Gate 6：Natural rollout

```text
[ ] 30–50 预注册场景
[ ] attempted / blocked / committed / harm
[ ] clean utility
[ ] p50/p95 latency
[ ] would-confirm rate
[ ] absolute 和 relative ASR reduction
[ ] 全部场景与 baseline-success subset 分开报告
```

### Gate 7：公开发布

```text
[ ] v1 release
[ ] 数据发布
[ ] Zenodo DOI
[ ] 技术报告
[ ] 2–3 分钟 demo
[ ] error gallery
[ ] clean-room reproduction
[ ] upstream PR 或文档贡献尝试
```

---

## 19. Code Review 检查表

### 19.1 通用

```text
[ ] 变更范围明确
[ ] 没有无关修改
[ ] public API 有类型和文档
[ ] 错误带上下文
[ ] 测试覆盖新行为
[ ] lint/type/test 通过
[ ] 文档同步
[ ] CHANGELOG 适用时更新
```

### 19.2 安全

```text
[ ] 不可信输入经过验证
[ ] 明确 DENY 不可覆盖
[ ] 所有副作用经过 PEP
[ ] canonical digest 与 dispatch 一致
[ ] fail-closed 行为有测试
[ ] replay/nonce/TTL 有测试
[ ] 无真实密钥或 PII
[ ] 日志不泄露敏感原文
```

### 19.3 研究

```text
[ ] authorization/state/utility 未混淆
[ ] 标签规则未悄悄变化
[ ] 无 future-token leakage
[ ] 无 lineage leakage
[ ] threshold 未在 test 调节
[ ] invalid runs 被计数
[ ] 结论未超出证据
[ ] exploratory/post-hoc 已标记
```

### 19.4 多 Agent

```text
[ ] 没有并行修改同一文件
[ ] 子 Agent 未改 label/policy
[ ] Reviewer 默认只读
[ ] 主 Agent 已整合结论
[ ] 最终状态已写回仓库
```

---

## 20. 新会话推荐启动提示

可以在新的 Codex 会话中使用：

```text
请把当前目录视为 GoalAuthBench 的独立项目根目录。

首先完整阅读：
1. GoalAuthBench_工程级项目标准与参考建议_v0.1.md
2. GoalAuthBench_v0.2_重审执行版_2026-07-27.md
3. GoalAuthBench_整体方案重审报告_2026-07-27.md

然后检查当前文件、Git 和环境状态。

本轮目标只完成 Gate 0：仓库启动，不实现 AgentDojo、
hidden-state、多语言、MCP 或完整 viewer。

请先给出：
- 当前状态；
- 需要创建或移动的文件；
- 拟采用的 Python/uv/测试/CI 方案；
- 风险与待确认决策；
- 验收命令。

经确认后再实施。

必须遵守：
- 不自行修改研究标签、policy、primary metric 或 primary split；
- 不把计划写成已完成；
- 所有改动附测试或可验证证据；
- 不创建无必要的复杂基础设施；
- 完成后运行 lint、type check、tests，并报告真实结果。
```

若希望直接授权执行，可在结尾增加：

```text
在不涉及外部发布、付费 API、真实凭据、删除现有研究文档或
扩大 v1 范围的前提下，你可以直接完成 Gate 0，并在结束时
提供完整变更摘要和验证结果。
```

---

## 21. 当前建议

1. 以 Inspect AI 为工程母版，但只采用其纪律和结构；
2. 以 AgentDojo 为领域参考，通过 adapter 集成；
3. 以 OpenSSF Passing/Baseline-1 为公开安全工程底线；
4. 以本文件的研究完整性规则作为 GoalAuthBench 的额外强制层；
5. 先完成 Gate 0 和 Gate 1，不提前构建复杂多 Agent、hooks、skills 或 UI；
6. 第一份可验证成果应是：

```text
6 个 golden groups
+ schema
+ validator
+ fake executor
+ T2 fail-closed tests
+ 无 API 的一键复现
```

7. 只有出现重复、稳定的工作流后，才将其封装为 Codex skill；
8. hooks 只用于成熟后需要机械执行的规则；
9. 多 Agent 优先用于只读审计、测试和复现；
10. 项目负责人始终保留授权标签、研究主张和发布决策权。

---

## 22. 最终验收定义

GoalAuthBench 不能因为“代码能运行”就被称为工程级项目。

只有同时满足以下条件，才达到本标准定义的工程级：

```text
清晰且冻结的研究问题
+ 可判定的授权真值
+ 可验证的数据与 lineage
+ 公平的 baseline
+ 正确的统计
+ 完整的测试
+ 安全执行边界
+ 可复现环境
+ 独立 Review
+ 真实失败案例
+ 诚实的限制
+ 版本化公开 artifact
```

该标准的目标不是保证论文录用或 GitHub stars，而是确保任何外部读者都可以回答：

1. 项目究竟研究了什么？
2. 标签为什么可信？
3. 代码为什么没有明显越过安全边界？
4. 实验能否重跑？
5. 结论是否由证据支持？
6. 失败和限制是否被如实公开？

当这六个问题都能由仓库中的代码、数据、测试、manifest 和文档回答时，GoalAuthBench 才真正从方案进入工程级研究项目。
