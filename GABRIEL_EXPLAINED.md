# GABRIEL 使用指南：从入门到理解

这份文档会用通俗的语言，自顶向下地讲解 GABRIEL 这个工具是什么、能做什么、以及它内部是怎么运作的。

---

## 一、GABRIEL 是什么？

**GABRIEL** (Generalized Attribute Based Ratings Information Extraction Library) 是一个让 GPT 帮你做"批量判断"的工具。

想象一个场景：你是一个社会科学研究者，手上有 1000 篇政治演讲，你想给每篇演讲打分——"这篇演讲有多民粹？有多煽动仇外情绪？"

传统做法是雇一群人来读这些演讲，然后打分。这很贵、很慢、而且不同人打分标准不一样。

GABRIEL 的思路是：让 GPT 来当这个"打分员"。你只需要告诉它"什么是民粹"，它就能帮你把 1000 篇演讲全部打完分，而且标准一致。

GABRIEL 帮你处理了所有麻烦事：
- 自动把任务拆成小块并行处理
- 自动重试失败的请求
- 自动保存进度（中断了可以继续）
- 自动控制调用速度（不会被 OpenAI 限流）
- 自动估算费用

---

## 二、GABRIEL 能做什么？

GABRIEL 提供了 18 个核心功能，分成三大类：

### 2.1 测量类功能（给数据打分/分类）

| 功能 | 作用 | 举例 |
|------|------|------|
| `rate` | 给内容打 0-100 分 | 给演讲的"民粹程度"打分 |
| `classify` | 给内容贴标签 | 把新闻分成"政治/经济/体育" |
| `extract` | 从内容里提取信息 | 从产品描述里提取"公司名、CEO、成立年份" |
| `rank` | 两两比较，得出排名 | 哪个科技产品更"便携" |
| `discover` | 找出区分两组数据的特征 | 5 星评价和 1 星评价有什么区别 |

### 2.2 数据清洗类功能

| 功能 | 作用 | 举例 |
|------|------|------|
| `merge` | 模糊匹配两个数据集 | 把两个不同来源的职位名称对应起来 |
| `deduplicate` | 去重（概念上的重复） | 把"F-18"、"大黄蜂战斗机"、"f18"合并成一个 |
| `filter` | 用自然语言筛选数据 | 从 1000 万个维基百科标题里筛出"科技相关的" |
| `deidentify` | 脱敏（保护隐私） | 把真实姓名、地址替换成假的 |

### 2.3 辅助工具类功能

| 功能 | 作用 |
|------|------|
| `codify` | 在文本里高亮标注特定内容 |
| `compare` | 对比两个内容的异同 |
| `bucket` | 把很多东西自动分组 |
| `seed` | 生成多样化的样本 |
| `ideate` | 生成新想法并筛选最好的 |
| `whatever` | 跑任意自定义的 GPT 提示词 |

---

## 三、怎么用 GABRIEL？

### 3.1 最简单的例子：给菜品打分

```python
import gabriel
import pandas as pd

# 准备数据：4 道菜
data = pd.DataFrame({
    "dish": ["火鸡", "南瓜派", "烤玉米", "蔬菜沙拉"]
})

# 定义要打分的维度
attributes = {
    "咸味": "这道菜有多咸",
    "甜味": "这道菜有多甜",
    "热量": "这道菜热量有多高"
}

# 调用 GABRIEL
results = await gabriel.rate(
    df=data,
    column_name="dish",
    attributes=attributes,
    save_dir="./dish_ratings",
    model="gpt-4o-mini"
)

# 结果是一个 DataFrame
print(results)
```

输出类似：
```
       dish    咸味    甜味    热量
0      火鸡     65      5      70
1    南瓜派     10     85      60
2    烤玉米     40     25      45
3  蔬菜沙拉     20     10      15
```

### 3.2 分类例子：给新闻分类

```python
results = await gabriel.classify(
    df=news_df,
    column_name="headline",
    labels={
        "政治": "关于政府、选举、政策的新闻",
        "经济": "关于市场、企业、金融的新闻",
        "体育": "关于体育赛事、运动员的新闻",
        "科技": "关于技术、互联网、AI 的新闻"
    },
    save_dir="./news_classified"
)
```

### 3.3 提取信息例子：从产品描述提取结构化数据

```python
results = await gabriel.extract(
    df=products_df,
    column_name="description",
    fields={
        "brand": "品牌名称",
        "price": "价格（数字）",
        "category": "产品类别"
    },
    save_dir="./product_info"
)
```

---

## 四、GABRIEL 内部是怎么工作的？

当你调用 `gabriel.rate()` 时，内部发生了这些事情：

```
┌─────────────────────────────────────────────────────────┐
│                 1. 你调用 gabriel.rate()                │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│            2. API 层：参数验证和配置                     │
│   - 检查你的参数是否合法                                 │
│   - 创建一个配置对象（RateConfig）                       │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│            3. 任务层：准备提示词                          │
│   - 加载提示词模板（Jinja2 格式）                        │
│   - 把你的数据和属性填进模板里                           │
│   - 生成要发给 GPT 的完整提示词                          │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│            4. 调度层：批量调用 GPT                        │
│   - 检查之前有没有保存的进度（断点续传）                   │
│   - 估算费用，显示给你看                                 │
│   - 同时发起多个请求（比如 100 个并行）                   │
│   - 控制速度，不超过 OpenAI 的限制                       │
│   - 失败了自动重试                                       │
│   - 每处理 100 条就保存一次结果                          │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    5. OpenAI API                        │
│   - 接收提示词，返回 JSON 格式的评分                     │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│            6. 解析层：处理返回结果                        │
│   - 解析 JSON，提取评分                                  │
│   - 如果 JSON 格式有问题，尝试修复                       │
│   - 如果你设置了多次评分（n_runs=2），取平均             │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│            7. 返回结果：一个 DataFrame                    │
│   - 原始数据 + 新增的评分列                              │
│   - 同时保存到你指定的文件夹里                           │
└─────────────────────────────────────────────────────────┘
```

---

## 五、核心代码结构

GABRIEL 的代码组织得很清晰：

```
src/gabriel/
├── api.py              # 入口：你调用的 gabriel.rate() 等函数都在这里
├── tasks/              # 每种任务的具体实现
│   ├── rate.py         # 打分任务
│   ├── classify.py     # 分类任务
│   ├── extract.py      # 提取任务
│   └── ...             # 其他 15 种任务
├── prompts/            # 提示词模板（Jinja2 格式）
│   ├── ratings_prompt.jinja2
│   ├── classification_prompt.jinja2
│   └── ...
├── utils/
│   ├── openai_utils.py # 核心：批量调用、重试、限流、断点续传
│   └── parsing.py      # JSON 解析和错误恢复
└── core/
    ├── llm_client.py   # OpenAI 客户端封装
    └── prompt_template.py  # 模板渲染
```

### 5.1 入口层：api.py

这是你接触的第一层。`gabriel.rate()` 实际上是这样定义的：

```python
async def rate(
    df: pd.DataFrame,
    column_name: str,
    attributes: dict,
    save_dir: str,
    model: str = "gpt-4o-mini",
    n_runs: int = 1,
    n_parallels: int = 200,
    ...
) -> pd.DataFrame:
    # 1. 创建配置
    config = RateConfig(
        column_name=column_name,
        attributes=attributes,
        ...
    )

    # 2. 创建任务实例
    task = Rate(df=df, config=config)

    # 3. 运行任务
    return await task.run()
```

### 5.2 任务层：tasks/rate.py

每个任务都是一个类，核心是 `run()` 方法：

```python
class Rate:
    async def run(self):
        # 1. 去重：如果有重复的输入，只处理一次
        unique_items = self._deduplicate()

        # 2. 生成提示词
        prompts = self._render_prompts(unique_items)

        # 3. 调用 GPT（这里用到 openai_utils）
        responses = await get_all_responses(prompts, ...)

        # 4. 解析结果
        ratings = self._parse_responses(responses)

        # 5. 把结果合并回原始数据
        return self._merge_results(ratings)
```

### 5.3 调度层：utils/openai_utils.py

这是 GABRIEL 最核心的部分，大约 2400 行代码。它的 `get_all_responses()` 函数负责：

```python
async def get_all_responses(
    prompts: list,
    save_path: str,
    n_parallels: int = 200,
    ...
):
    # 1. 断点续传：检查之前有没有保存的结果
    if os.path.exists(save_path):
        completed = load_completed(save_path)
        prompts = [p for p in prompts if p.id not in completed]

    # 2. 费用估算
    estimated_cost = estimate_cost(prompts)
    print(f"预计费用：${estimated_cost:.2f}")

    # 3. 限流器：确保不超过 OpenAI 的速率限制
    limiter = AsyncLimiter(requests_per_minute=3500)

    # 4. 并行处理
    async with limiter:
        tasks = [call_openai(p) for p in prompts]
        results = await asyncio.gather(*tasks)

    # 5. 保存结果
    save_to_csv(results, save_path)

    return results
```

### 5.4 提示词模板：prompts/ratings_prompt.jinja2

GABRIEL 用 Jinja2 模板来生成发给 GPT 的提示词：

```jinja2
你的任务是对以下内容进行评分。

评分维度：
{% for attr, desc in attributes.items() %}
- {{ attr }}: {{ desc }}
{% endfor %}

待评分内容：
{{ content }}

请以 JSON 格式输出，每个维度给出 0-100 的分数：
{
    {% for attr in attributes.keys() %}
    "{{ attr }}": <0-100>{{ "," if not loop.last }}
    {% endfor %}
}
```

---

## 六、几个实用的设计

### 6.1 断点续传

如果你的任务跑到一半断了，不用担心：

```python
# 第一次运行：处理到 500 条时中断了
results = await gabriel.rate(df, ..., save_dir="./my_ratings")

# 第二次运行：会自动从第 501 条继续
results = await gabriel.rate(df, ..., save_dir="./my_ratings")
```

GABRIEL 会把已完成的结果保存在 `save_dir/xxx_raw_responses.csv`，下次运行时自动跳过。

### 6.2 多次评分取平均

GPT 的输出有一定随机性，多次评分取平均可以更稳定：

```python
results = await gabriel.rate(
    df,
    attributes=...,
    n_runs=3,  # 让 GPT 评 3 次
    save_dir="./ratings"
)
# 最终结果是 3 次评分的平均值
```

### 6.3 离线测试模式

不想花钱调 API？用 dummy 模式：

```python
results = await gabriel.rate(
    df,
    attributes=...,
    use_dummy=True,  # 不调真实 API，返回假数据
    save_dir="./test"
)
```

### 6.4 支持多种数据类型

不只是文本，GABRIEL 还支持图片、音频、网页搜索：

```python
# 给图片打分
results = await gabriel.rate(
    df,
    column_name="image_path",  # 这列是图片路径
    attributes={"美观程度": "图片有多好看"},
    modality="image"  # 告诉 GABRIEL 这是图片
)

# 让 GPT 先搜索网页再评分
results = await gabriel.rate(
    df,
    column_name="company_name",
    attributes={"市场声誉": "这家公司的市场声誉如何"},
    modality="web"  # GPT 会先搜索这家公司的信息
)
```

---

## 七、一个完整的流程示例

假设你要分析 100 篇政治演讲的民粹程度：

```python
import gabriel
import pandas as pd
import os

# 1. 设置 API Key
os.environ["OPENAI_API_KEY"] = "sk-..."

# 2. 加载数据
speeches = pd.read_csv("speeches.csv")
# speeches 长这样：
#    id  |  speaker  |  text
#    1   |  张三     |  "我们要为人民服务..."
#    2   |  李四     |  "精英们不懂老百姓..."

# 3. 定义评分维度
attributes = {
    "民粹程度": "演讲中是否强调'人民 vs 精英'的对立",
    "煽动性": "演讲的情绪煽动程度",
    "具体政策": "演讲中提到了多少具体政策"
}

# 4. 运行评分
results = await gabriel.rate(
    df=speeches,
    column_name="text",
    attributes=attributes,
    save_dir="./speech_analysis",
    model="gpt-4o-mini",
    n_runs=2,  # 评 2 次取平均
    n_parallels=50  # 50 个请求并行
)

# 5. 查看结果
print(results.head())
#    id  |  speaker  |  text                    |  民粹程度  |  煽动性  |  具体政策
#    1   |  张三     |  "我们要为人民服务..."    |   35       |   20     |   65
#    2   |  李四     |  "精英们不懂老百姓..."    |   85       |   70     |   15

# 6. 保存结果
results.to_csv("./speech_analysis/final_results.csv")
```

运行时你会看到类似这样的输出：
```
检测到 100 条数据
去重后：98 条（2 条重复）
预计费用：$0.15
预计时间：2 分钟
正在处理... [████████████████████] 100%
完成！结果已保存到 ./speech_analysis/
```

---

## 八、详细功能介绍

下面逐一介绍 GABRIEL 的每个核心功能，包括它们的用途、参数和使用示例。

---

### 8.1 `rate` - 评分功能

**用途**：给内容打 0-100 分，可以同时评估多个维度。

**典型场景**：
- 给演讲的"民粹程度"打分
- 评估推文的"毒性"
- 给产品图片的"高端感"打分

**核心参数**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `df` | 包含待评分内容的 DataFrame | 必填 |
| `column_name` | 要评分的列名 | 必填 |
| `attributes` | 评分维度，格式：`{"维度名": "描述"}` | 必填 |
| `save_dir` | 结果保存目录 | 必填 |
| `model` | 使用的模型 | "gpt-4o-mini" |
| `n_runs` | 评分次数（取平均） | 1 |
| `n_parallels` | 并行请求数 | 650 |
| `n_attributes_per_run` | 每次请求最多评几个维度 | 8 |
| `modality` | 数据类型："text"/"image"/"audio"/"web" | "text" |
| `additional_instructions` | 额外的评分说明 | None |

**完整示例**：

```python
import gabriel
import pandas as pd

# 准备数据
tweets = pd.DataFrame({
    "id": [1, 2, 3],
    "content": [
        "今天天气真好，心情愉快！",
        "这个产品太烂了，浪费我的钱！",
        "刚看完一部电影，还行吧。"
    ]
})

# 定义评分维度
attributes = {
    "情绪积极程度": "内容表达的情绪有多积极正面",
    "攻击性": "内容是否带有攻击性或负面情绪",
    "主观性": "内容有多主观（vs 客观陈述事实）"
}

# 运行评分
results = await gabriel.rate(
    df=tweets,
    column_name="content",
    attributes=attributes,
    save_dir="./tweet_ratings",
    model="gpt-4o-mini",
    n_runs=2,  # 评 2 次取平均，结果更稳定
    additional_instructions="请基于中文语境理解内容"
)

# 结果
#    id | content                    | 情绪积极程度 | 攻击性 | 主观性
#    1  | 今天天气真好，心情愉快！     |     85      |   5    |   70
#    2  | 这个产品太烂了，浪费我的钱！ |     10      |   75   |   85
#    3  | 刚看完一部电影，还行吧。     |     50      |   10   |   60
```

**多模态评分示例**：

```python
# 给图片打分
image_results = await gabriel.rate(
    df=product_images,
    column_name="image_url",  # 图片 URL 或本地路径
    attributes={
        "专业感": "图片看起来有多专业",
        "吸引力": "图片有多吸引人"
    },
    modality="image",  # 声明这是图片
    save_dir="./image_ratings"
)

# 让 GPT 先搜索再评分
web_results = await gabriel.rate(
    df=companies,
    column_name="company_name",
    attributes={
        "市场声誉": "这家公司的市场声誉如何",
        "创新能力": "这家公司被认为有多创新"
    },
    modality="web",  # GPT 会先搜索相关信息
    save_dir="./company_ratings"
)
```

---

### 8.2 `classify` - 分类功能

**用途**：给内容贴标签，支持多标签分类。

**典型场景**：
- 把新闻分成"政治/经济/体育/科技"
- 给客服工单分类
- 给图片打多个标签

**核心参数**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `df` | 待分类的 DataFrame | 必填 |
| `column_name` | 要分类的列名 | 必填 |
| `labels` | 类别定义，格式：`{"类别名": "描述"}` | 必填 |
| `save_dir` | 结果保存目录 | 必填 |
| `min_frequency` | 多次分类时，标签出现频率阈值 | 0.6 |
| `differentiate` | 是否启用对比分类模式 | False |

**示例**：

```python
# 新闻分类
news = pd.DataFrame({
    "headline": [
        "央行宣布降息 0.25 个百分点",
        "国足 2:1 击败对手晋级",
        "新款 AI 手机发布，销量火爆",
        "两国领导人举行会谈"
    ]
})

results = await gabriel.classify(
    df=news,
    column_name="headline",
    labels={
        "政治": "关于政府、外交、政策的新闻",
        "经济": "关于金融、市场、企业的新闻",
        "体育": "关于体育赛事、运动员的新闻",
        "科技": "关于技术、互联网、产品的新闻"
    },
    save_dir="./news_classified",
    n_runs=3,  # 分类 3 次
    min_frequency=0.6  # 至少 2/3 次被打上这个标签才算
)

# 结果会有每个类别的布尔列 + 一个 predicted_classes 列
#    headline                    | 政治  | 经济  | 体育  | 科技  | predicted_classes
#    央行宣布降息...              | False | True  | False | False | ["经济"]
#    国足 2:1 击败对手...         | False | False | True  | False | ["体育"]
#    新款 AI 手机发布...          | False | True  | False | True  | ["经济", "科技"]
```

**对比分类模式**：

```python
# 对比两篇文章的差异
results = await gabriel.classify(
    df=paired_articles,
    circle_column_name="article_a",  # 第一篇
    square_column_name="article_b",  # 第二篇
    labels={
        "更乐观": "哪篇文章语气更乐观",
        "更详细": "哪篇文章内容更详细"
    },
    differentiate=True,  # 启用对比模式
    save_dir="./article_comparison"
)
```

---

### 8.3 `extract` - 信息提取功能

**用途**：从非结构化文本中提取结构化信息。

**典型场景**：
- 从产品描述提取"品牌、价格、类别"
- 从简历提取"姓名、学校、工作经历"
- 从新闻提取"人物、地点、事件"

**核心参数**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `df` | 包含待提取内容的 DataFrame | 必填 |
| `column_name` | 要提取的列名 | 必填 |
| `attributes` | 要提取的字段，格式：`{"字段名": "描述"}` | 必填 |
| `types` | 字段类型约束（可选） | None |
| `save_dir` | 结果保存目录 | 必填 |

**示例**：

```python
# 从产品描述提取信息
products = pd.DataFrame({
    "description": [
        "苹果 iPhone 15 Pro，128GB，售价 7999 元，2023 年发布",
        "三星 Galaxy S24，256GB，售价 5999 元，旗舰拍照手机",
        "小米 14 Ultra，512GB，售价 6499 元，徕卡联名款"
    ]
})

results = await gabriel.extract(
    df=products,
    column_name="description",
    attributes={
        "brand": "品牌名称",
        "model": "具体型号",
        "storage": "存储容量",
        "price": "价格（纯数字）",
        "highlight": "主要卖点"
    },
    types={
        "price": "int"  # 强制转换为整数
    },
    save_dir="./product_info"
)

# 结果
#    description | brand | model         | storage | price | highlight
#    苹果 iPhone | 苹果  | iPhone 15 Pro | 128GB   | 7999  | None
#    三星 Galaxy | 三星  | Galaxy S24    | 256GB   | 5999  | 旗舰拍照手机
#    小米 14...  | 小米  | 14 Ultra      | 512GB   | 6499  | 徕卡联名款
```

**提取多个实体**：

```python
# 从一段文本提取多个人物
text_df = pd.DataFrame({
    "article": [
        "会议上，张三发表了讲话，李四提出了反对意见，王五表示支持。"
    ]
})

results = await gabriel.extract(
    df=text_df,
    column_name="article",
    attributes={
        "person": "人物姓名",
        "action": "这个人做了什么"
    },
    save_dir="./people_extracted"
)

# 如果一段文本有多个实体，会自动展开成多行
#    article     | person | action
#    会议上...   | 张三   | 发表了讲话
#    会议上...   | 李四   | 提出了反对意见
#    会议上...   | 王五   | 表示支持
```

---

### 8.4 `rank` - 排名功能

**用途**：通过两两比较，得出一组内容的相对排名。

**原理**：类似 ELO 评分系统，GABRIEL 会随机配对两个内容让 GPT 比较，然后用 Bradley-Terry 模型计算出每个内容的综合得分。

**典型场景**：
- 给科技产品按"便携性"排名
- 给设计方案按"美观程度"排名
- 给论文摘要按"创新性"排名

**核心参数**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `df` | 待排名的 DataFrame | 必填 |
| `column_name` | 要比较的列名 | 必填 |
| `attributes` | 排名维度 | 必填 |
| `n_rounds` | 比赛轮数 | 5 |
| `matches_per_round` | 每轮每个项目比几场 | 3 |
| `power_matching` | 是否智能配对（让实力接近的对手比赛） | True |
| `initial_rating_pass` | 是否先做一轮初步评分 | True |

**示例**：

```python
# 给笔记本电脑按便携性排名
laptops = pd.DataFrame({
    "name": ["MacBook Air", "ThinkPad X1", "ROG 幻 16", "Surface Pro"],
    "specs": [
        "13.6 寸，1.24kg，M2 芯片",
        "14 寸，1.12kg，商务轻薄本",
        "16 寸，2.5kg，游戏本",
        "13 寸，0.88kg，平板二合一"
    ]
})

results = await gabriel.rank(
    df=laptops,
    column_name="specs",
    attributes={
        "便携性": "考虑重量、尺寸、是否方便携带",
        "性能": "处理器性能、适合的使用场景"
    },
    n_rounds=3,  # 3 轮比赛
    matches_per_round=2,  # 每轮每台电脑比 2 场
    save_dir="./laptop_ranking"
)

# 结果是 z-score（标准分），正数表示高于平均
#    name          | specs         | 便携性_zscore | 性能_zscore
#    Surface Pro   | 13 寸，0.88kg | 1.5           | -0.8
#    ThinkPad X1   | 14 寸，1.12kg | 0.8           | 0.2
#    MacBook Air   | 13.6 寸...    | 0.3           | 0.5
#    ROG 幻 16     | 16 寸，2.5kg  | -2.6          | 1.8
```

**递归排名**（适合大规模数据）：

```python
# 1000 个产品，用递归方式逐步淘汰
results = await gabriel.rank(
    df=large_product_df,
    column_name="description",
    attributes={"质量": "产品质量如何"},
    recursive=True,  # 启用递归模式
    recursive_fraction=0.5,  # 每轮淘汰一半
    recursive_min_remaining=50,  # 剩下 50 个时停止
    save_dir="./product_ranking"
)
```

---

### 8.5 `deduplicate` - 去重功能

**用途**：把"概念上相同但表述不同"的内容合并。

**典型场景**：
- 把 "F-18"、"Super Hornet"、"f18 大黄蜂" 合并成一个
- 把不同拼写的公司名统一
- 合并同义的标签

**核心参数**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `df` | 待去重的 DataFrame | 必填 |
| `column_name` | 要去重的列名 | 必填 |
| `n_runs` | 去重轮数 | 3 |
| `use_embeddings` | 是否用向量相似度预筛选 | True |
| `group_size` | 每批处理多少个 | 500 |

**示例**：

```python
# 去重战斗机名称
aircraft = pd.DataFrame({
    "name": [
        "F-18", "Super Hornet", "f18 大黄蜂",
        "F-22", "Raptor", "猛禽战斗机",
        "苏-27", "Su-27", "侧卫"
    ]
})

results = await gabriel.deduplicate(
    df=aircraft,
    column_name="name",
    additional_instructions="这些是战斗机名称，请识别指代同一款机型的名称",
    save_dir="./aircraft_dedup"
)

# 结果会多一列 mapped_name，显示规范化后的名称
#    name          | mapped_name
#    F-18          | F-18
#    Super Hornet  | F-18
#    f18 大黄蜂    | F-18
#    F-22          | F-22
#    Raptor        | F-22
#    猛禽战斗机    | F-22
#    苏-27         | 苏-27
#    Su-27         | 苏-27
#    侧卫          | 苏-27
```

---

### 8.6 `merge` - 模糊匹配功能

**用途**：把两个数据集按相似内容匹配起来（类似模糊版的 JOIN）。

**典型场景**：
- 匹配两个来源的职位名称
- 把专利标题和产品名称对应起来
- 跨数据集的实体链接

**核心参数**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `df_left` | 左表 | 必填 |
| `df_right` | 右表 | 必填 |
| `left_on` | 左表匹配列 | 必填 |
| `right_on` | 右表匹配列 | 必填 |
| `how` | 匹配方向："left" 或 "right" | "left" |
| `use_embeddings` | 是否用向量预筛选候选 | True |
| `auto_match_threshold` | 自动确认匹配的置信度阈值 | 0.75 |

**示例**：

```python
# 两个来源的职位名称匹配
source_a = pd.DataFrame({
    "job_title_a": ["软件工程师", "产品经理", "数据分析师", "UI 设计师"]
})

source_b = pd.DataFrame({
    "job_title_b": ["Software Engineer", "PM", "Data Analyst", "UX Designer", "Backend Dev"]
})

results = await gabriel.merge(
    df_left=source_a,
    df_right=source_b,
    left_on="job_title_a",
    right_on="job_title_b",
    how="left",  # 以左表为准
    save_dir="./job_matching"
)

# 结果
#    job_title_a   | job_title_b
#    软件工程师    | Software Engineer
#    产品经理      | PM
#    数据分析师    | Data Analyst
#    UI 设计师     | UX Designer
```

---

### 8.7 `filter` - 筛选功能

**用途**：用自然语言条件快速筛选大量数据。

**典型场景**：
- 从 1000 万个维基百科标题里筛出"科技相关的"
- 从产品列表里筛出"适合送礼的"
- 快速过滤不相关的数据

**核心参数**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `df` | 待筛选的 DataFrame | 必填 |
| `column_name` | 要筛选的列名 | 必填 |
| `condition` | 筛选条件（自然语言） | 必填 |
| `entities_per_call` | 每次请求处理多少个 | 150 |
| `threshold` | 保留阈值（0-1） | 0.5 |
| `n_runs` | 筛选轮数 | 1 |

**示例**：

```python
# 从维基百科标题筛选科技相关的
wiki_titles = pd.DataFrame({
    "title": [
        "量子计算", "清朝历史", "机器学习", "莎士比亚",
        "5G 网络", "法国大革命", "区块链", "印象派绑画"
    ]
})

results = await gabriel.filter(
    df=wiki_titles,
    column_name="title",
    condition="是否与科技、技术、互联网、计算机相关",
    save_dir="./tech_filter"
)

# 结果：只保留符合条件的
#    title      | keep_score
#    量子计算   | 0.95
#    机器学习   | 0.98
#    5G 网络    | 0.92
#    区块链     | 0.88
```

---

### 8.8 `seed` - 样本生成功能

**用途**：生成多样化、有代表性的样本数据。

**典型场景**：
- 生成 1000 个代表美国人口分布的虚拟人物
- 生成多样化的测试用例
- 为研究创建初始数据集

**核心参数**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `instructions` | 描述要生成什么样的样本 | 必填 |
| `num_entities` | 目标数量 | 1000 |
| `entities_per_generation` | 每次请求生成多少个 | 50 |
| `deduplicate` | 是否自动去重 | False |

**示例**：

```python
# 生成多样化的虚拟用户画像
results = await gabriel.seed(
    instructions="""
    生成代表中国城市年轻人（18-35岁）的虚拟人物画像。

    每个人物应包含：
    - 姓名（常见中文名）
    - 年龄
    - 城市
    - 职业
    - 兴趣爱好

    确保多样性：不同城市、不同职业、不同兴趣的分布要合理。
    """,
    num_entities=100,
    entities_per_generation=20,
    deduplicate=True,  # 自动去重
    save_dir="./user_personas"
)

# 结果是一个包含生成人物的 DataFrame
```

---

### 8.9 `ideate` - 创意生成功能

**用途**：生成大量创意想法，并自动筛选出最好的。

**典型场景**：
- 围绕某个主题生成 1000 个理论假设
- 生成产品创意并排名
- 头脑风暴 + 自动筛选

**核心参数**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `topic` | 创意主题 | 必填 |
| `n_ideas` | 目标创意数量 | 1000 |
| `evaluation_mode` | 评估方式："recursive_rank"/"rank"/"rate"/"none" | "recursive_rank" |
| `attributes` | 评估维度 | None |
| `rank_attribute` | 用哪个维度排名 | None |

**示例**：

```python
# 生成关于"提高远程工作效率"的创意
results = await gabriel.ideate(
    topic="提高远程工作效率的方法",
    n_ideas=100,
    evaluation_mode="rank",  # 用排名方式筛选
    attributes={
        "可行性": "这个想法有多容易实施",
        "创新性": "这个想法有多新颖",
        "影响力": "这个想法能带来多大改变"
    },
    rank_attribute="影响力",  # 按影响力排名
    save_dir="./remote_work_ideas"
)

# 结果：排序后的创意列表
#    idea                           | 可行性 | 创新性 | 影响力 | rank
#    建立虚拟办公室社交空间          |  0.7   |  0.8   |  0.9   |  1
#    引入 AI 会议助手自动记录要点    |  0.8   |  0.7   |  0.85  |  2
#    ...
```

---

### 8.10 `discover` - 特征发现功能

**用途**：自动发现区分两组数据的特征。

**典型场景**：
- 发现 5 星评价和 1 星评价的区别
- 找出成功案例和失败案例的差异
- 探索性数据分析

**工作原理**：
1. 先用 `codify` 标注文本中的特征片段
2. 再用 `bucket` 把特征聚类成类别
3. 最后用 `classify` 验证这些特征是否真的能区分两组数据

**示例**：

```python
# 发现好评和差评的区别
reviews = pd.DataFrame({
    "good_review": [
        "服务态度很好，物流很快，产品质量不错",
        "包装精美，送货准时，客服很耐心",
        # ...
    ],
    "bad_review": [
        "等了一个月都没发货，客服不理人",
        "收到是坏的，退货还要自己付运费",
        # ...
    ]
})

results = await gabriel.discover(
    df=reviews,
    circle_column_name="good_review",  # 好评
    square_column_name="bad_review",   # 差评
    bucket_count=10,  # 发现约 10 个区分特征
    save_dir="./review_discovery"
)

# 结果是一个字典，包含：
# - "codify": 标注了哪些特征片段
# - "buckets": 特征聚类成了哪些类别
# - "classification": 这些特征对区分两组数据的效果
# - "summary": 总结报告
```

---

### 8.11 `codify` - 文本标注功能

**用途**：在文本中找到并标注特定内容。

**典型场景**：
- 在演讲中标注"经济不安全感"相关的句子
- 在访谈中标注"压力来源"的片段
- 定性研究的编码工作

**示例**：

```python
# 在访谈记录中标注压力来源
interviews = pd.DataFrame({
    "text": [
        "最近工作压力很大，每天加班到很晚。房贷也是个负担，每月还款占收入一大半...",
        # ...
    ]
})

results = await gabriel.codify(
    df=interviews,
    column_name="text",
    categories={
        "工作压力": "与工作相关的压力，如加班、任务重",
        "经济压力": "与金钱相关的压力，如房贷、开销",
        "人际压力": "与人际关系相关的压力，如家庭、同事"
    },
    save_dir="./interview_coding"
)

# 结果会标注出每个类别在文本中出现的位置
```

---

### 8.12 `bucket` - 自动分组功能

**用途**：把一堆东西自动聚类成几个组。

**典型场景**：
- 把 HR 收到的投诉分成几类
- 把用户反馈按主题分组
- 从标签列表中归纳出主要类别

**示例**：

```python
# 把投诉内容分组
complaints = pd.DataFrame({
    "complaint": [
        "工资发放延迟", "办公室太冷", "加班没有加班费",
        "电脑太旧了", "同事太吵", "年假太少",
        "报销流程太慢", "会议太多", "绩效考核不公平"
    ]
})

results = await gabriel.bucket(
    df=complaints,
    column_name="complaint",
    bucket_count=4,  # 分成约 4 类
    save_dir="./complaint_buckets"
)

# 结果：自动归纳出的类别
# - "薪酬福利"：工资发放延迟、加班没有加班费、年假太少
# - "办公环境"：办公室太冷、电脑太旧了、同事太吵
# - "流程效率"：报销流程太慢、会议太多
# - "管理制度"：绩效考核不公平
```

---

### 8.13 `compare` - 对比功能

**用途**：对比两个内容的异同。

**示例**：

```python
# 对比两个产品
products = pd.DataFrame({
    "product_a": ["iPhone 15：A16 芯片，6.1 寸屏幕，4800 万像素"],
    "product_b": ["Pixel 8：Tensor G3 芯片，6.2 寸屏幕，5000 万像素"]
})

results = await gabriel.compare(
    df=products,
    circle_column_name="product_a",
    square_column_name="product_b",
    attributes={
        "性能": "哪个性能更强",
        "拍照": "哪个拍照更好",
        "性价比": "哪个性价比更高"
    },
    save_dir="./product_comparison"
)
```

---

### 8.14 `deidentify` - 脱敏功能

**用途**：把敏感信息（姓名、地址等）替换成假的，但保持文本可读性。

**典型场景**：
- 分享访谈记录前去除真实姓名
- 发布数据集前脱敏
- 保护隐私

**示例**：

```python
# 脱敏访谈记录
interviews = pd.DataFrame({
    "person_id": [1, 1, 2],
    "text": [
        "我是张三，在阿里巴巴工作，住在杭州西湖区。",
        "张三补充说，他的同事李四也有类似经历。",
        "我叫王五，在腾讯工作，深圳南山区住了 5 年。"
    ]
})

results = await gabriel.deidentify(
    df=interviews,
    column_name="text",
    grouping_column="person_id",  # 同一个人的名字要一致替换
    save_dir="./deidentified"
)

# 结果
#    text_deidentified
#    我是陈六，在字节跳动工作，住在北京朝阳区。
#    陈六补充说，他的同事刘七也有类似经历。
#    我叫周八，在华为工作，上海浦东新区住了 5 年。
```

---

### 8.15 `paraphrase` - 改写功能

**用途**：按照指定要求改写文本。

**典型场景**：
- 摘要化长文本
- 去除特定信息后改写
- 风格转换

**示例**：

```python
# 简化财报摘要
reports = pd.DataFrame({
    "text": [
        "苹果公司 2024 年 Q1 财报显示，iPhone 收入同比增长 5%，达到 697 亿美元..."
    ]
})

results = await gabriel.paraphrase(
    df=reports,
    column_name="text",
    instructions="用简单的语言总结主要数据，去掉具体公司名称，控制在 50 字以内",
    save_dir="./paraphrased"
)
```

---

### 8.16 `whatever` - 万能功能

**用途**：运行任意自定义的 GPT 提示词，利用 GABRIEL 的批量处理能力。

**典型场景**：
- 现有功能都不满足需求时
- 快速实验自定义提示词
- 集成到自定义流程中

**示例**：

```python
# 自定义翻译任务
texts = pd.DataFrame({
    "chinese": ["今天天气真好", "我喜欢编程", "机器学习很有趣"]
})

results = await gabriel.whatever(
    df=texts,
    column_name="chinese",
    prompts="请把以下中文翻译成英文，只输出翻译结果：{chinese}",
    save_dir="./translations"
)

# 或者直接传入提示词列表
prompts = [
    "1+1 等于几？",
    "中国的首都是哪里？",
    "水的化学式是什么？"
]

results = await gabriel.whatever(
    prompts=prompts,
    save_dir="./qa_results"
)
```

---

### 8.17 `view` - 结果查看器

**用途**：交互式查看和检查结果。

**示例**：

```python
# 查看评分结果
gabriel.view(
    df=rating_results,
    column_name="text",
    attributes=["民粹程度", "煽动性"],
    max_passages=100
)
# 会打开一个交互式 HTML 界面
```

---

## 九、通用参数说明

大多数功能都支持以下通用参数：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `save_dir` | 结果保存目录 | 必填 |
| `model` | 使用的模型 | "gpt-4o-mini" |
| `n_parallels` | 并行请求数 | 650 |
| `n_runs` | 重复次数（取平均/投票） | 1 |
| `use_dummy` | 是否用假数据测试（不调 API） | False |
| `reset_files` | 是否重新开始（忽略之前的进度） | False |
| `additional_instructions` | 额外的提示词说明 | None |
| `modality` | 数据类型 | "text" |

---

## 十、总结

GABRIEL 的核心价值是：**让你专注于研究问题，把工程细节交给它**。

你只需要：
1. 准备好数据（一个 DataFrame）
2. 用自然语言描述你要测量什么
3. 调用一个函数

GABRIEL 帮你处理：
- 提示词的构造
- API 调用的批量化和并行化
- 速率限制和重试
- 断点续传
- 费用估算
- 结果的解析和聚合

这让原本需要写几百行代码的工作，变成了几行代码就能完成。
